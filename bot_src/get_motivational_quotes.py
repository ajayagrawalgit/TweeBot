import requests
from bot_src.tweetformatter import *
import random

def get_a_quote(url):
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        for line in data:
            quote = line["q"]
            author = line["a"]
            return quote, author
    else:
        print("Uh Oh! Something went wrong !!!")


def get_quotes_and_author():
    with open("POSTED_TWEETS/posted_motivational_quotes.txt", "r") as f:
        posted_quotes = f.read().splitlines()

    url = "https://zenquotes.io/api/quotes"
    quote, author = get_a_quote(url)
    while quote in posted_quotes:
        quote, author = get_a_quote(url)
    
    with open("POSTED_TWEETS/posted_motivational_quotes.txt", "a") as f:
        f.write(quote + "\n")
    
    motivational_emojis = ["💪", "🔥", "🌟", "👏", "🚀", "💼", "📈", "💯", "👍", "💡", "⭐", "🙌", "🌈", "👊", "😊", "🎯", "🔝", "🌞", "📚", "💹", "🎉", "💰", "🤗", "🏆", "😇", "👑", "💵", "👩‍💻", "👨‍💻", "📝", "🔑", "💭", "✨", "👣", "📉", "⏳", "🚪", "💡", "👩‍🏫", "👨‍🏫", "🌱", "🎓", "🎈", "📆", "💬", "🔍", "🔭", "🌍", "🌎", "🌏", "🌴", "🎓", "💖", "🔥", "👩‍🔬", "👨‍🔬", "🔬", "🔭", "📊", "🔝", "🎓", "💪", "🌟", "🔥", "📚", "📖", "💡", "🔍", "🌈", "💭", "🌞", "🔑", "📝", "👩‍💻", "👨‍💻", "🎯", "🎉", "🏆", "💰", "🔝", "🌱", "👣", "💡", "🔥", "👩‍🔬", "👨‍🔬", "💼", "📈", "🌱", "🔍", "🌍", "🌎", "🌏", "🌴", "💖", "🔥", "👩‍🏫", "👨‍🏫", "🌈", "📆", "🔭"]

    hashtags = "#inspirationalthoughts #positivequotes #inspirations #inspireothers #successmindset #motivationalquotesoftheday #motivations #motivationmonday #motivationalquote #motivational #grandaspirationblessings #grandaspirationi #inspirational #thewritersco #motivation #inspirationalquotes #motivational #quotes #love #motivationalquotes #success #inspire #life #quote #quoteoftheday #entrepreneur #positivevibes #positivity #quotestoliveby #lifequotes #instagram #instagood #follow #business #happiness #positive #successquotes #hustle #happy #goodmorning #goodnight #quotestolivebyfollow #spreadpositivity #instapreneuracademy #motivationoftheday #positivityiskey #mindsetmatters #inspiration #keytosuccess #mindsetcoach #mindsetshift #mindsetiseverything #successtips #motivationalquotesoftheday #inspirationalquote #inspirations #motivation101 #successmindset #morningmotivation #powerofpositivity #successfulmindset #mentalaspect #mentalhealth #mentalhealthquotes #instapreneur"

    random_emoji = random.choice(motivational_emojis)
    hashtags_to_post = get_hashtags(hashtags, 20)

    quote_and_author = f"{quote} {random_emoji}\n- by {author}\n\n{hashtags_to_post}"
    return quote_and_author
