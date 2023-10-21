import requests
import random

def get_an_activity():
    types_available = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
    type_choose = random.choice(types_available)
    url = f"http://www.boredapi.com/api/activity?type={type_choose}&price=0"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Kuch toh gadbad h bhai !\nError {response.status_code}: {response.reason}")

    return data['activity']



def create_bored_activity():

    with open("POSTED_TWEETS/activity_list.txt", "r") as f:
        posted_activities = f.read().splitlines()

    uniq_act = get_an_activity()
    while uniq_act in posted_activities:
        uniq_act = get_an_activity()

    sentences = [  "One activity that might interest you is...",  "How about trying out this fun activity:...",  "If you're in the mood for something new, you might enjoy...",  "Have you ever considered trying your hand at...",  "Here's an activity that can help you shake off boredom:...",  "Looking for something to do? Why not try...",  "Feeling bored? How about giving this activity a go:...",  "If you're looking for a new hobby, you might enjoy...",  "Why not challenge yourself with this activity:...",  "In the mood for something creative? Try...",  "Here's an activity that's both fun and relaxing:...",  "If you're feeling adventurous, you might enjoy trying...",  "Looking to improve a skill? Give this activity a try:...",  "If you're looking for a way to unwind, you might enjoy...",  "How about trying a new activity like...",  "Want to learn something new? Try this activity:...",  "Why not get outside and try this fun activity:...",  "If you're in the mood for a challenge, give this activity a shot:...",  "Here's an activity that's perfect for a lazy day:...",  "If you're feeling creative, you might enjoy trying..."]

    random_starter = random.choice(sentences)
    hashtags = "#influencer #tbt #hobby #tech #mickbot #api #today #motivation"

    full_sentence = f"{random_starter}\n{uniq_act}\n\n{hashtags}"

    with open("POSTED_TWEETS/activity_list.txt", "a") as f:
        f.write(uniq_act + "\n")

    return full_sentence

