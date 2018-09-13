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

client = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def youtube_search(q, max_results=7):
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = client.search().list(
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

# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]

      # For properties that have array values, convert a name like
      # "snippet.tags[]" to snippet.tags, and set a flag to handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True

      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

def playlist_items_insert(properties, **kwargs):
  # See full sample for function
  resource = build_resource(properties)

  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlistItems().insert(
    body=resource,
    **kwargs
  ).execute()

#   return response
  print(response)

def insert_items_to_playlist(playlist_id, items):
    for item in items:
        playlist_items_insert(client,
            {'snippet.playlistId': playlist_id,
            'snippet.resourceId.kind': 'youtube#video',
            'snippet.resourceId.videoId': item.videoId,
            'snippet.position': ''},
            part='snippet',
            onBehalfOfContentOwner='')
    return True