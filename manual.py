import re
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from email import train_model
from urllib.parse import urlparse

def predict_email(model):
    account_name = input("Enter the copied text of the email:").strip()
    
    try:
        account_age = input("Enter the copied text of the email:").strip()
    except ValueError:
        print("Invalid input. Please enter integer values for age, posts, followers, and following.")
        return None

    input_vector = [["Email Type", "Email Text"]]
    prediction = model.predict(input_vector)
    result = "Safe" if prediction[0] == 1 else "Malware found"
    print(f"The account is predicted to be a {result}")
def main():
    # Train the model using the CSV dataset
    model = train_model()
    if model is None:
        print("Model training failed. Please check your dataset.")
        return

    # Predict account authenticity based on user input
    predict_email(model)

if __name__ == "__main__":
    main()