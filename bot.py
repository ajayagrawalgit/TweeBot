import tweepy
import sys

# Import required modules and credentials
from bot_src.creds import *
from bot_src.tweetformatter import *

from bot_src.newsdataio import generate_news_to_post
from bot_src.boredapi_activities import create_bored_activity
from bot_src.spotify_trends import spotify_top_3
from bot_src.hacker_news import get_hacker_news_post
from bot_src.wikiposts import final_wiki_post
from bot_src.get_motivational_quotes import get_quotes_and_author
from bot_src.funfacts import fun_fact_formatted
from bot_src.tmdb_top_movie import get_movie_to_tweet
from bot_src.jokes import create_joke

def main():
    # Authenticate with the Twitter API
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get the command-line argument
    bot_active_arg = sys.argv[1]

    if bot_active_arg == "":
        print("No arguments provided.")
    elif bot_active_arg == "joke":
        # Post a joke
        joke = format_this(create_joke())
        client.create_tweet(text=f"{joke}")
    elif bot_active_arg == "activity":
        # Post an activity from the Bored API
        activity = format_this(create_bored_activity())
        client.create_tweet(text=f"{activity}")
    elif bot_active_arg == "news":
        # Post news from the newsdata.io API
        new_news = format_this(generate_news_to_post())
        client.create_tweet(text=f"{new_news}")
    elif bot_active_arg == "spotify_top_3":
        # Post the top 3 tracks from Spotify - India
        top_5_tracks = format_this(spotify_top_3())
        client.create_tweet(text=f"{top_5_tracks}")
    elif bot_active_arg == "hacker_news":
        # Get top Hacker News from YCombinator
        top_news = get_hacker_news_post()
        client.create_tweet(text=f"{top_news}")
    elif bot_active_arg == "wiki_post":
        # Get a random topic from Wikipedia
        wiki_tweet = format_this(final_wiki_post())
        client.create_tweet(text=f"{wiki_tweet}")
    elif bot_active_arg == "motivational_quote":
        # Get a random motivational quote from ZenQuotes
        motivational_quote = format_this(get_quotes_and_author())
        client.create_tweet(text=f"{motivational_quote}")
    elif bot_active_arg == "funfact":
        # Get a random fun fact
        funfact = format_this(fun_fact_formatted())
        client.create_tweet(text=f"{funfact}")
    elif bot_active_arg == "tmdb_top_movie":
        # Get a movie recommendation from TMDB (similar to IMDB)
        tmdb_top_mov = format_this(get_movie_to_tweet())
        client.create_tweet(text=f"{tmdb_top_mov}")
    else:
        print("Invalid argument provided.")

# Call the main function if the script is run as the main module
if __name__ == "__main__":
    main()

