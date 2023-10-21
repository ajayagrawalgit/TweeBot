import pyshorteners
import re
import random

def format_this(tweet):
    if len(tweet) <= 279:
        return tweet
    else:
        trimmed_tweet = tweet[:279]
        return trimmed_tweet

def make_this_url_tiny(long_url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    return short_url


def remove_the_spaces(variable):
    list_to_join = variable.split()
    removed_spaces = "".join(list_to_join)
    complete_clean_string = re.sub(r'[^a-zA-Z0-9]', '', removed_spaces)
    return complete_clean_string

def get_hashtags(hashtags, num):
    hashtahs_split = hashtags.split()
    random.shuffle(hashtahs_split)
    hashtahs_to_return_list = hashtahs_split[:num]
    selected_hashtags_str = ' '.join(hashtahs_to_return_list)
    return selected_hashtags_str

