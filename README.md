# Annotations Topics

This sample code pulls contextual information for given users, based on their recent Tweets (past 7 days, max 100 Tweets), including: 
* Context annotations (annotation domains and annotation entities)
* Entity annotations

Specifically, this code uses: 
* [The Twitter API v2 recent search endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)
* [Tweet annotations](https://developer.twitter.com/en/docs/twitter-api/annotations)

Each user's Tweets are analysed, and the top most frequent annotation topics detected in their Tweets are returned in order of frequency. 

There are two scripts: 
* `main.py` returns both context annotations and entitiy annotations through the command line interface;
* `get_data.py` returns context annotations data in a csv file.

## Environment variables

To run this, you will first need to export your keys and tokens for your Twitter API App. Make sure to use an App that has access to the Twitter API v2. 

In the command line, type the following lines of code. Replace each placeholder with your own credentials (without the `<>`).

```
export 'API_KEY'='<your_api_key>'
export 'API_SECRET'='<your_api_secret>'
export 'API_TOKEN'='<your_api_token>'
export 'API_TOKEN_SECRET'='<your_api_token_secret>'
```

## `main.py`

This script returns context annotations in the command line interface for a given username.

In addition, when present, entity annotations are also analysed and returned. This means that specific people, places, products, organizations, or other topics that have been mentioned in the user's Tweets in the past week are displayed. These entities are only displayed if they have been categorized with a confidence score of 0.5 or higher.

To run the script:

```
python3 main.py
```

## `get_data.py`

This script returns context annotations data in a csv file for a list of given usernames. 

To pass in the usernames for which to pull annotations data: create a file entitled `Twitter_handles.csv` and populate it with the desired handles/usernames (see `sample.csv` as an example).

This script does **not** return entity annotations.

By default, this script will return rows, each of which contains: 
* Given username
* Number of Tweets sent in the past week
* Top 5 context annotation domains (and the number of times each of these was mentioned)
* Top 5 context annotation entities (and the number of times each of these was mentioned) 

You can change the number of top results returned towards the bottom of the script: 

```
    max_count = 5   # Change number of top results displayed here
```

To run the script:

```
python3 get_data.py
```