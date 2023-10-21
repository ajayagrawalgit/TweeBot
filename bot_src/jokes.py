from dadjokes import Dadjoke
import random


# Define function to post tweet
def create_joke():
    # Load posted jokes from file
    with open("POSTED_TWEETS/jokes.txt", "r") as f:
        posted_jokes = f.read().splitlines()

    # Generate new joke
    dadjoke = Dadjoke()
    joke = dadjoke.joke
    
    while joke in posted_jokes:
        joke = dadjoke.joke

    # Create a Formatted Post
    laugh_emojis = [  "😂", "🤣", "😆", "😅", "😄", "😊", "😁", "😀", "😃", "😝",  "😜", "😛", "😹", "🤪", "🤩", "😎", "😜", "🤓", "😸", "😹"]
    random_laugh = random.choice(laugh_emojis)
    joke_to_be_posted = f"{joke} {random_laugh}\n\n#mickbot #pyjokes #funnytweets #funny #daily #memes #memesdaily"

    # Save posted joke to file
    with open("POSTED_TWEETS/jokes.txt", "a") as f:
        f.write(joke + "\n")
    
    return joke_to_be_posted

