from tw33t import app
import json, requests, datetime, sys, os, uuid, re, time

from flask import jsonify
from flask import request


TWEET_POINT = 'https://api.twitter.com/2/'
BEARER_TOKEN ='cFZvMlBZamNjTm45QzViVEZ0RnJmRkI5Z1pqUU9MSEh0SENldkc5MzhYYWgwOjE2NTEwMjk2MTg1NDg6MToxOmF0OjE'
headers = {'Authorization': 'Bearer ' + BEARER_TOKEN}


def get_me():
    url = TWEET_POINT + 'users/me'
    r = requests.get(url=url, headers=headers, data={})
    return r.json()


def search_tweets(username, text=''):
    params = '?query=from:{}%20{}&tweet.fields=id,created_at&max_results=10'.format(username, text)
    url = TWEET_POINT + 'tweets/search/recent' + params
    r = requests.get(url=url, headers=headers, data={})
    return r.json()


def log_file(username, params, data):
    app.logger.info("----- GET TWEETS--------")
    app.logger.info("User {} get tweets".format(username))
    if params:
        app.logger.info("Params {}".format(params))
    app.logger.info("Data: {}".format(data))
    app.logger.info("----- END --------")


@app.route("/me", methods=['GET'])
def index():
    user = get_me()
    return user


@app.route("/get_tweets", methods=['GET'])
def get_tweets():
    search = request.args.get('search', '')
    username = get_me()['data']['username']
    response = search_tweets(username, search)
    log_file(username, { 'search': search }, response)
    return response
