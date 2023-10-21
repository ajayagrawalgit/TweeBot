import requests
import time
import bot_src.tweetformatter as tweetformatter
import random

def get_fun_fact():
    url = "https://useless-facts.sameerkumar.website/api"
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data["data"]
        except requests.exceptions.RequestException:
            pass
        time.sleep(1) 


def fun_fact_formatted():
    with open("POSTED_TWEETS/funfacts.txt", "r") as f:
        posted_facts = f.read().splitlines()
    
    fact = get_fun_fact()
    while fact in posted_facts:
        fact = get_fun_fact()
        
    with open("POSTED_TWEETS/funfacts.txt", "a") as f:
        f.write(fact + "\n")
    
    hashtags = "#funfact #didyouknow #triviatime #randomfacts #factcheck #fascinatingfacts #knowledgebomb #wowfact #funfactoid #curiousminds #factfinder #funfactsonly #mindblown #amazinginfo #discoveries #factoftheday #weirdbuttrue #unbelievable #quirkyinfo #interestingstats #surprisingfacts #funfactwednesday #strangebutfascinating #mindbendingfacts"
    
    hashtags_to_post = tweetformatter.get_hashtags(hashtags, 20)
    
    surprising_emojis = [
    "😲", "🤯", "😮", "😱", "😧", "🙀", "😵", "🤔", "🧐", "🤓",
    "😎", "🤩", "🤪", "😜", "😝", "🤑", "🤗", "🤭", "🤫", "🤔",
    "🧐", "😯", "🤤", "😳", "🤭"
    ]
    
    emoji_to_add = random.choice(surprising_emojis)

    
    fun_fact_to_post = f"{emoji_to_add} Fun Fact Time !\n{fact}\n\n{hashtags_to_post}"
    
    return fun_fact_to_post
