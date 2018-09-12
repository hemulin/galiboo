
def smart_search(client, q):
  tracks = client.track.smart_search(q)
  if not tracks['success']:
    return []
  results = []
  for track in tracks['results']:
      results.append({
          'id': track['_id'],
          'artist': track['artists'][0]['name'],
          'title': track['title'],
          'spotifyId': track['external_ids']['spotify'],
          'audioUrl': track['audio_url'],
      })
  return results

def tracks_search(client, track_q):
  tracks = client.track.get(track=track_q)
  if not tracks['success']:
    return []
  results = []
  for track in tracks['results']:
      results.append({
          'id': track['_id'],
          'artist': track['artists'][0]['name'],
          'title': track['title'],
          'spotifyId': track['external_ids']['spotify'],
          'audioUrl': track['audio_url'],
      })
  return results

def tracks_by_artist_search(client, artist_q):
  tracks = client.track.get(artist=artist_q)
  if not tracks['success']:
    return []
  results = []
  for track in tracks['results']:
      results.append({
          'id': track['_id'],
          'artist': track['artists'][0]['name'],
          'title': track['title'],
          'spotifyId': track['external_ids']['spotify'],
          'audioUrl': track['audio_url'],
      })
  return results

def similiar_search(client, track_id):
  tracks = client.track.search_by_similar(track_id)
  if not tracks['success']:
    return []
  results = []
  for track in tracks['results']:
      results.append({
          'id': track['_id'],
          'artist': track['artists'][0]['name'],
          'title': track['title'],
          'spotifyId': track['external_ids']['spotify'],
          'audioUrl': track['audio_url'],
      })
  return results