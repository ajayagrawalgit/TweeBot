import requests
import random
import pyshorteners
from bot_src.creds import news_data_io_API

# Define the list of queries
query_list = [
    "bollywood", "bollywoodgossip", "indian actress", "trending in india", "actress trending on twitter",
    "twitter trend", "artificial intelligence", "machine learning", "python", "india", "indian movies",
    "Bollywood movie release", "Celebrity fitness", "Celebrity fashion"
]

# Function to make a URL tiny
def make_this_url_tiny(long_url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    return short_url

# Function to get hashtags
def get_hashtags(hashtags_list):
    hashtags_split = hashtags_list.split()
    random.shuffle(hashtags_split)
    return ' '.join(hashtags_split[:8])

# Function to fetch news data
def get_news_data(api_key, query):
    url = f"https://newsdata.io/api/1/news?apikey={api_key}"
    params = {"q": query}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error {response.status_code}: {response.reason}")
        return []

# Function to get the latest news
def get_latest_news(api_key, query_list):
    with open("POSTED_TWEETS/news.txt", "r") as f:
        posted_news = set(f.read().splitlines())
    
    while True:
        query = random.choice(query_list)
        news_data = get_news_data(api_key, query)
        
        if not news_data:
            continue
        
        news_item = news_data[0]
        title = news_item.get('title', '')
        
        if title not in posted_news:
            return title, make_this_url_tiny(news_item.get('link', '')), query

# Function to generate news to post
def generate_news_to_post():
    news_title, news_link, query = get_latest_news(news_data_io_API, query_list)
    
    starter_list = [
        "👀 Hey, here's a news for you:", "🗞️ Have you heard the latest news?", "🚨 Breaking news!",
        "🔊 Listen up, I have some news for you.", "🤔 I just read some interesting news.",
        "📰 Guess what's in the news today?", "👉 In case you missed it, there's some big news.",
        "📣 Can I share some news with you?", "🆕 This just in...", "⚠️ Attention, there's some news that you should know.",
        "📢 Here's the latest news:", "💥 News flash!", "🎉 Exciting news!", "🚨 Important news alert!",
        "📢 Just announced:", "🚀 Breaking development:", "😱 Can you believe the news?", "🤯 Here's a shocker:",
        "⚠️ Heads up, here's the news.", "🌟 This just happened:"
    ]

    hashtags_list = "#trending #news #interesting #india #artificialintelligence #ai #breakingnews #important #mickbot #discovery #headlines #todaysnews #newsreporter #updatenews #newstoday #newsoftheday #newsupdate #latestnews #dailynews #breakingnews #news #moda #tudolindo #instafashion #fashion #vendasonline #juizdefora #minasgerais #modafeminina #colecaolinda #looksfemininos #looksestilosos #modaeestilo #bomgostoin #shoponlline #carpediembelvederemais #correprosite #asnovidadesnaoparam #shopnow #donadokahidden #eagles #update #sport #workout #nflfantasy #nfl100 #nflhighlights #lamarjackson #fantasyfootball #nike #sports #nfldraft #espnnews #nflupdates #breakingnews #football #espn #nfllive #nfl #nflnetwork #nflfootballneste #contrahomofobia #diainternacionalcontraahomofobia #respeito #somostodosiguais #lovewins #pride🌈 #orgulho #tolerancia #diversidade #inclusao #coexist #diversity #andrealmada"

    hashtags_to_post = get_hashtags(hashtags_list)
    starter = random.choice(starter_list)
    news_to_post = f"{starter}\n{news_title}\nRead More: {news_link}\n\n#{query} {hashtags_to_post}"

    with open("POSTED_TWEETS/news.txt", "a") as f:
        f.write(news_title + "\n")
    
    return news_to_post

