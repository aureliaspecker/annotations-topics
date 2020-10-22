import sys
import os
import requests
from requests_oauthlib import OAuth1
import json

# To set your environmental variables in your terminal run the following lines:
# export 'API_KEY'='<your_api_key>'
# export 'API_SECRET'='<your_api_secret>'
# export 'API_TOKEN'='<your_api_token>'
# export 'API_TOKEN_SECRET'='<your_api_token_secret>'

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
api_token = os.environ.get("API_TOKEN")
api_token_secret = os.environ.get("API_TOKEN_SECRET")  

auth = OAuth1(api_key, api_secret, 
            api_token, api_token_secret)

url = "https://api.twitter.com/2/tweets/search/recent"

def get_username():
    username = input("Input username (e.g. bbcnews): ")
    if username[0] == "@":
        username = username[1:]
    return username

def make_payload(username): 
    payload = {"query": f"from:{username}", "tweet.fields": "context_annotations"}
    return payload

def connect_to_endpoint(url, auth, payload):
    try:
        response = requests.request("GET", url, params=payload, auth=auth)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
            print(response.text)
        return response.json()
    except: 
        print("Something went wrong. Make sure you exported your environment keys and tokens before running the script.")
        sys.exit()

def get_annotations(username, response):

    domain = []
    entity = []

    try: 
        for element in response["data"]:
            if "context_annotations" in element:
                for annotation in element["context_annotations"]: 
                    domain.append(annotation["domain"]["name"])
                    entity.append(annotation["entity"]["name"])

        domain_frequency = {d:domain.count(d) for d in domain} 
        entity_frequency = {e:entity.count(e) for e in entity}  
        domain_frequency_ordered = {k: v for k, v in sorted(domain_frequency.items(), key=lambda item: item[1], reverse=True)}
        entity_frequency_ordered = {k: v for k, v in sorted(entity_frequency.items(), key=lambda item: item[1], reverse=True)} 
        
    except: 
        print(f"No topics data to analyse for @{username} in the past week")
        sys.exit()

    return domain_frequency_ordered, entity_frequency_ordered

def topics_analysis(username, domains, entities): 
    domains_count = 0
    entities_count = 0

    for i in domains: 
        domains_count += 1
    
    for i in entities: 
        entities_count += 1

    if not domains and not entities: 
        print(f"""
        =====
        No topics to return for @{username} in the past week"
        =====
        """)
    
    elif domains_count >= 5 and entities_count >= 5:
        top_five_domains = list(domains.items())[:5]
        top_five_entities = list(entities.items())[:5] 
        print(f"""
        =====
        "Top five domain topics for @{username} in the past week: {top_five_domains}"
        ~~~~~
        "Top five entities topics for @{username} in the past week: {top_five_entities}" 
        =====
        """)
    
    elif domains_count >= 3 and entities_count >= 3: 
        top_three_domains = list(domains.items())[:3]
        top_three_entities = list(entities.items())[:3]
        print(f"""
        =====
        "Top three domain topics for @{username} in the past week: {top_three_domains}"
        ~~~~~
        "Top three entities topics for @{username} in the past week: {top_three_entities}" 
        =====
        """) 

    elif domains_count >= 1 and entities_count >= 1:
        print(f"""
        =====
        "Limited domain topics available for @{username} in the past week. This includes: {domains}"
        ~~~~~
        "Limited entities topics available for @{username} in the past week. This includes: {entities}" 
        =====
        """)  
    
    else: 
        print(f"""
        =====
        No topics to return for @{username} in the past week
        =====
        """)

def main():
    username = get_username() 
    payload = make_payload(username)
    json_response = connect_to_endpoint(url, auth, payload)
    domains, entities = get_annotations(username, json_response)
    analysis = topics_analysis(username, domains, entities)

if __name__ == "__main__":
    main()