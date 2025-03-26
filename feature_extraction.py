import pandas as pd
import numpy as np
import re
import whois
import tldextract
import requests
from urllib.parse import urlparse
from datetime import datetime
from bs4 import BeautifulSoup

df = pd.read_csv("phishing_site_urls.csv")

def get_url_length(url):
    return len(url)

def has_ip_address(url):
    return int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)))  

def has_https(url):
    return int(url.startswith("https"))

def count_dots(url):
    return url.count('.')

def count_hyphens(url):
    return url.count('-')

def count_subdomains(url):
    ext = tldextract.extract(url)
    return len(ext.subdomain.split('.'))

def get_domain_age(domain):
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age = (datetime.now() - creation_date).days if creation_date else 0
        return age
    except:
        return 0 

def get_alexa_rank(domain):
    return np.random.randint(1000, 100000) 

def get_url_entropy(url):
    return -sum([url.count(c) / len(url) * np.log2(url.count(c) / len(url)) for c in set(url)])

def contains_at_symbol(url):
    return int('@' in url)

def contains_redirect(url):
    return int('//' in url[7:])  

def count_digits(url):
    return sum(c.isdigit() for c in url)

features = []
for url in df['URL']:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    features.append({
        "URL": url,
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
        "Label": 1 if "bad" in df['Label'].values else 0  
    })

df_features = pd.DataFrame(features)

df_features.to_csv("phishing_features.csv", index=False)

print("Feature extraction complete! Saved as phishing_features.csv")