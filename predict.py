import pandas as pd
import joblib
from feature_extraction import *  


model = joblib.load("phishing_model.pkl")


url = input("Enter URL to check: ")


parsed_url = urlparse(url)
domain = parsed_url.netloc

new_data = pd.DataFrame([{
    "Length": get_url_length(url),
    "Contains_IP": has_ip_address(url),
    "HTTPS": has_https(url),
    "Num_Dots": count_dots(url),
    "Num_Hyphens": count_hyphens(url),
    "Num_Subdomains": count_subdomains(url),
    "Domain_Age": get_domain_age(domain),
    "Alexa_Rank": get_alexa_rank(domain),
    "URL_Entropy": get_url_entropy(url),
    "Has_At": contains_at_symbol(url),
    "Has_Redirect": contains_redirect(url),
    "Num_Digits": count_digits(url),
}])


prediction = model.predict(new_data)[0]
print("🔴 Phishing URL!" if prediction == 1 else "🟢 Legitimate URL.")