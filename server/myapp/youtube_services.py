#!/usr/bin/python

###########################################
### USAGE: python search.py --q beatles ###
###########################################

import json
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = os.getenv("YOUTUBE_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(q, max_results=7):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=q,
        part="id,snippet",
        type='video',
        order='viewCount',
        # order='relevance',
        maxResults=max_results
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        videos.append({
            'title': search_result['snippet']['title'],
            'thumbnail': search_result['snippet']['thumbnails']['high']['url'],
            'videoId': search_result['id']['videoId'],
            'url': 'https://www.youtube.com/watch?v={}'.format(search_result['id']['videoId'])
        })

    # print('done', json.dumps(videos, indent=4))
    return videos