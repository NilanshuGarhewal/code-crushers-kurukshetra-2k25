# importing dependencies
import pandas as pd
import joblib
import re
import tldextract
from collections import Counter
from scipy.stats import entropy
from urllib.parse import urlparse
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the trained model
try:
    predictmodel = joblib.load("main_model.pkl")
    expected_features = list(predictmodel.feature_names_in_)
    print(f"Model Loaded. Expected Features: {expected_features}")
except Exception as e:
    print(f"Error loading model: {e}")
    predictmodel = None
    expected_features = None

# API routes
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/phishshield", methods=["POST"])
def phishshield():
    if request.content_type == "application/json":
        data = request.get_json()
        url = data.get("url")
    else:
        url = request.form.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400
    if not predictmodel:
        return jsonify({"error": "Model failed to load"}), 500

    # Extract features
    features_df = extract_features(url)

    print(f"Extracted Features: {list(features_df.columns)}")

    missing_features = set(expected_features) - set(features_df.columns)
    extra_features = set(features_df.columns) - set(expected_features)

    if missing_features:
        return jsonify({"error": f"Missing features: {missing_features}"}), 500
    if extra_features:
        return jsonify({"error": f"Unexpected features: {extra_features}"}), 500

    # Ensure correct feature order
    features_df = features_df[expected_features]

    prediction = predictmodel.predict(features_df)[0]
    return render_template("result.html", result=url, prediction=prediction)


def extract_features(url):
    # Extract domain information

    parsed_url = urlparse(url)
    domain_info = tldextract.extract(url)

    # List of suspicious keywords
    suspicious_keywords = [
        "login", "bank", "secure", "update", "verify",
        "free", "click", "password", "account"
    ]

    # List of dangerous TLDs
    dangerous_tlds = {"tk", "ml", "ga", "cf", "gq"}

    features = {
        "Number of dots": url.count("."),
        "Number of slashes": url.count("/"),
        "Percentage of numerical characters": sum(c.isdigit() for c in url) / max(len(url), 1),
        "Dangerous characters": int(bool(re.search(r"[!@#$%^&*(),?\":{}|<>]", url))),
        "Dangerous TLD": int(domain_info.suffix in dangerous_tlds),
        "IP Address": int(bool(re.search(r"[0-9]+(?:\.[0-9]+){3}", url))),
        "Domain name length": len(domain_info.domain),
        "Suspicious keywords": int(any(word in url.lower() for word in suspicious_keywords)),
        "Repetitions": int(bool(re.search(r"(.)\1{2,}", domain_info.domain))),
        "Redirections": int(url[7:].find("//") != -1),
        "Entropy and length (PCA)": len(url) * calculate_entropy(url)
    }

    df = pd.DataFrame([features])

    return df


def calculate_entropy(text):
    frequency = Counter(text)
    probability = [frequency[i] / len(text) for i in frequency]
    return entropy(probability, base=2)


if __name__ == "__main__":
    app.run(debug=True)
