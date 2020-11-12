# Annotations Topics

This sample code pulls contextual information for a given user, based on their recent Tweets (past 7 days, max 100 Tweets). 

Specifically, this code uses: 
* [The Twitter API v2 recent search endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)
* [Tweet annotations](https://developer.twitter.com/en/docs/twitter-api/annotations)

Each user's Tweets are analysed, and the top most frequent context annotations detected in their Tweets are returned in order of frequency. 

In addition, when present, Tweet entities are also analysed. This means that specific people, places, products, organizations, or other topics that have been mentioned by the user in the past week are displayed. These entities topics are only displayed if they have been categorized with a confidence score of 0.5 or higher.

## Environment variables

To run this script, you first need to export your keys and tokens for your Twitter API App. Make sure to use an App that has access to the Twitter API v2. 

In the command line, type the following lines of code. Replace each placeholder with your own credentials (without the `<>`).

```
export 'API_KEY'='<your_api_key>'
export 'API_SECRET'='<your_api_secret>'
export 'API_TOKEN'='<your_api_token>'
export 'API_TOKEN_SECRET'='<your_api_token_secret>'
```

To run the script:

```
python3 main.py
```