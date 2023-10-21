import requests
import random
from bot_src.creds import *
from bot_src.tweetformatter import *

def spotify_top_3():
    # Set up authentication with Spotify API
    client_id = spotify_client_id
    client_secret = spotify_client_secret
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    })
    access_token = auth_response.json()['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Get the "India Top 50" playlist
    playlist_id = '37i9dQZEVXbLZ52XmnySJg'
    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    playlist_response = requests.get(playlist_url, headers=headers)
    playlist_data = playlist_response.json()

    playlist_name = playlist_data["name"]
    playlist_desc = playlist_data["description"]
    playlist_link = playlist_data["external_urls"]["spotify"]

    all_track_details = playlist_data["tracks"]["items"]

    count=0
    track_count = 1
    track_list=""

    for tr in all_track_details:
        track_name = tr["track"]["name"]
        artist_details = tr["track"]["album"]["artists"]
        for ar in artist_details:
            artist_name = ar["name"]
        track_list = track_list + f"{track_count}. "+ f"{track_name} by {artist_name}\n"
        if count==2:
            break
        count += 1
        track_count += 1

    track_list = track_list.rstrip()


    # FORMATTING THE FINAL STRING HERE BELOW

    starters_list = [    "Guess what! 🤩",    "This is amazing! 😱",    "OMG! 🙀",    "This is insane! 🤯",    "I'm freaking out! 😬",    "This is so exciting! 🎉",    "I can't believe it! 😲",    "This is wild! 🤪",    "This is incredible! 😍",    "This is mind-blowing! 🤯",    "I'm ecstatic! 😁",    "This is unreal! 😮",    "This is unbelievable! 🤯",    "This is insane! 😜",    "I'm so pumped! 💪",    "This is awesome! 🤩",    "I'm over the moon! 🌙",    "This is phenomenal! 🤩",    "This is incredible news! 🎊",    "I'm so excited! 😆"]
    starter = random.choice(starters_list)

    hashtags_list = "#trending #music #musiclove #artist #bass #countrymusic #dance #dancemusic #deephouse #dj #djlife #dubstep #edm #edmfamily #edmlife #edmlifestyle #edmmusic #edmnation #electro #electrohouse #electronic #electronicmusic #festival #goodmusic #hiphop #hipphopmusic #house #housemusic #indiemusic #livemusic #music #musica #musicallyapp #musicaltheatre #musicclover #musicfestival #musicial #musician #musicians #musicislife #musicismylife #musiclife #musiclover  #musicphotography #musicproducer #musicproduction #musicvideo #newmusic #nightlife #party #partymusic #plur #popmusic #producer #progressivehouse #rave #rockmusic #summer #techhouse #techno #tomorrowland #trapmusic #beat #beats #bhfyp #dj #fashion #hiphop #hiphopartist #hiphopbeats #hiphopblog #hiphopculture #hiphopdance #hiphophead #hiphopheads #hiphopjunkie #hiphoplife hiphopmusic #hiphopnation #hiphopnews #instrumentals #mixtape #music #musicproducer #musicvideo #newmusic #party #producer #rap  #rapmusic #rapper #rappers #rnb #singer #song #songwriter #soundcloudrapper #studio #trap #trapmusic #unsignedartist #worldstar #music #video #musiclove #newmusic #nowplaying #radio #live #apple #life #hiphop #artist #musicartist #rock #music #musician #musicians #musicproducer #musicvideo #musicman #musicismylife #musicianlife #musicmonday #musicstudio #soundcloud #podcast #spotify #applemusic #tidal #musicstreaming #itunes"

    hashtags_to_post = get_hashtags(hashtags_list, 10)


    spotify_post_frame = f"{starter}\nIndia's Top 3 from @Spotify 🎵\n{track_list}\n({make_this_url_tiny(playlist_link)})\n\n{hashtags_to_post}"

    spotify_to_post = format_this(spotify_post_frame)
    if spotify_to_post[-1] == "#":
        spotify_to_post = spotify_to_post[0:len(spotify_to_post)-1]

    return spotify_to_post
