import requests
from bs4 import BeautifulSoup
from datetime import datetime

from bot_src.tweetformatter import *

def get_response_from_hackernews():
    url = "https://news.ycombinator.com/news"
    response = requests.get(url)
    soup_obj = BeautifulSoup(response.text,"html.parser")
    return soup_obj


def sort_this(hacker_news_list):
    return sorted(hacker_news_list, key=lambda k:k['score'], reverse=True)

def get_hackernews_details(soup_object):
    hacker_news_list = []
    links_and_title = soup_object.select(".titleline")
    scores = soup_object.select(".score")
    for idx, i in enumerate(links_and_title):
        news_title = links_and_title[idx].getText()
        try:
            news_score = int((scores[idx].getText()).replace(" points", ""))
        except IndexError:
            news_score = 0

        news_link = links_and_title[idx].find("a").get('href', None)
        if news_link.startswith("item"):
            news_link = "https://news.ycombinator.com/" + news_link

        if news_score > 100:
            hacker_news_list.append({'title': news_title, 'score': news_score, 'link': news_link})
    # sorted_news_list = sort_this(hacker_news_list)
    return hacker_news_list


def get_hacker_news_post():
    soup_obj = get_response_from_hackernews()
    news_list = get_hackernews_details(soup_obj)

    hashtags_list = "#technews #technology #tech #pro #technologynews #gadgets #techtoday #oneplus #smartphone #iphone #android #techie #techworld #g #innovation #gadget #apple #mobile #techlover #techupdates #news #techno #samsung #techy #engineering #techgadgets #electronics #techgeek #technologies #realme #xiaomi #newtechnology #technologythesedays #smartphones #twitternews #google #futuretech #bhfyp #redminote #twittertechnology #mi #india #twitter #phone #techtrends #ios #techblogger #plus #s #technologyrocks #techies #redmi #business #technewsindia #series #h #techblog #futuretechnology #t #science #hacker #hackernews"

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    top_news = f"In the Tech Now [ {dt_string} IST ] !\n{news_list[0]['title']} ({news_list[0]['score']} points) - {make_this_url_tiny(news_list[0]['link'])}\n\nSource: https://news.ycombinator.com/news \n@ycombinator @newsycbot\n\n{get_hashtags(hashtags_list, 10)}"

    top_news_post = format_this(top_news)
    return top_news_post

