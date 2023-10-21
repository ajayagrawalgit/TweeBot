import wikipedia
import random
import bot_src.tweetformatter as tweetformatter


def get_a_wiki_topic():
    with open("POSTED_TWEETS/wikiposts.txt", "r") as f:
        posted_wikis = f.read().splitlines()
    
    # Generate a New Topic
    random_title = wikipedia.random()
    
    # Generate the URL for this now
    random_url = wikipedia.page(random_title).url
    
    while random_title in posted_wikis:
        random_title = wikipedia.random()
        random_url = wikipedia.page(random_title).url
    
    wiki_summary = wikipedia.summary(random_title, sentences = 2)
    
    with open("POSTED_TWEETS/wikiposts.txt", "a") as f:
        f.write(random_title + "\n")
    
    return random_title, random_url, wiki_summary


def final_wiki_post():
    wiki_topic, wiki_url, wiki_summary = get_a_wiki_topic()
    geeky_emojis = ["😀", "😎", "🤓", "👓", "🔬", "🔭", "🖥️", "📱", "💻", "📚", "📝", "🔍", "🕹️", "💡", "🔋", "🛠️", "👩‍💻", "👨‍💻", "🚀", "🌌", "🔮", "📡", "⚙️", "🔧", "🔩", "🖱️", "⌨️", "📺", "🎮", "💾", "💿", "📼", "📹", "🎧", "📷", "📸", "🎞️", "💡", "🎥", "🎬"]
    
    starter_lines = [
    "🔍 Check out this Wikipedia page!",
    "🤓 Fascinating find on Wikipedia!",
    "🔥 Interesting Wikipedia discovery!",
    "👀 Captivating Wikipedia page!",
    "📚 Informative find on Wikipedia!",
    "💡 Thought-provoking Wikipedia page!",
    "🔎 Engaging discovery on Wikipedia!",
    "🔍 Intriguing Wikipedia find!",
    "😍 Fascinating Wikipedia page!",
    "😃 Enjoyable discovery on Wikipedia!",
    "🔬 Interesting Wikipedia topic!",
    "🔍 Intriguing Wikipedia page!",
    "📖 Informative find on Wikipedia!",
    "🔥 Check out this captivating Wikipedia page!",
    "😲 Surprising discovery on Wikipedia!",
    "🚀 Fascinating Wikipedia topic!",
    "💭 Thought-provoking find on Wikipedia!",
    "🔍 Interesting Wikipedia page!",
    "😍 Captivating discovery on Wikipedia!",
    "🔎 Check out this intriguing Wikipedia page!"
    ]
    
    hashtags = "#Wikipedia #Wiki #KnowledgeIsPower #WikipediaWednesday #WikiLove #FactCheck #OpenKnowledge #CitationNeeded #WikipediaEditing #WikiCommunity #FreeKnowledge #Wikiquote #Wikimedia #WikipediaPage #WikiResearch #WikipediaFact #WikiTrivia #WikipediaArticles #WikiProject #WikipediaCitations"
    
    final_wiki_post = random.choice(starter_lines) + "\n" + wiki_topic + ": " + wiki_summary + "\n\n" + random.choice(geeky_emojis) + "Read More: " + tweetformatter.make_this_url_tiny(wiki_url) + "\n\n" + tweetformatter.get_hashtags(hashtags, 8)
    
    return final_wiki_post
    

