
![TWEEBOT](https://github.com/ajayagrawalgit/TweeBot/assets/94609372/5e96de4e-ca4f-43ca-abf1-6cb2b12ea5c3)


TweeBot is an open-source Twitter bot framework that empowers users to create and deploy their own Twitter bots. It leverages various APIs to curate and post intriguing content on Twitter. The live version of TweeBot, represented as **@mickbotsays** on Twitter, demonstrates its capabilities by sharing entertaining jokes, insightful Hacker News posts, trending news, fun facts, and more. This documentation serves as a comprehensive guide for implementing TweeBot's functionality and enhancing your Twitter experience.

<br>
<br>

## Prerequisites

Before using TweeBot, ensure your system meets these prerequisites:

1. **Python 3.10 or Higher**: TweeBot relies on Python for executing its scripts and interacting with various APIs.

2. **Reliable Task Scheduler**: To schedule tasks, use tools like Cron, Anacron on Linux-based systems, and Windows Task Scheduler on Windows.

3. **Twitter Developer Account**: Obtain the following API keys from your Twitter Developer Dashboard:

    - Consumer Key
    - Consumer Secret Key
    - Access Token
    - Access Token Secret
    - Bearer Token

    If you require assistance with creating a developer account and obtaining these keys, please refer to the official Twitter Developer Documentation or available YouTube tutorials.

4. **API Keys from Other Platforms**:
   While TweeBot uses multiple API endpoints that are free and don't require sign-ups, the following platforms offer data-related features that require registration:

    - Newsdata.io API Key: Register for an API key at [https://newsdata.io/register](https://newsdata.io/register).
    - Spotify Developer Account: Obtain API keys after signing up for "Spotify for Developers" at [https://developer.spotify.com/](https://developer.spotify.com/).
    - themoviedb.org API Key: Get API keys after registering with themoviedb at [https://developer.themoviedb.org/docs](https://developer.themoviedb.org/docs).

<br>
<br>

## Features

TweeBot offers a diverse range of features, allowing you to post a variety of engaging content on your Twitter account. These features include:

1. **Jokes**: Share humor and entertain your followers with witty jokes sourced from the dadjokes library.

2. **Activity Suggestions**: Provide your audience with engaging activities to beat boredom using the Bored API, helping them discover interesting pastimes.

3. **Latest News Updates**: Keep your followers informed with the latest news on a wide range of topics, such as Bollywood, trending subjects in India, Python, AI, ML, and more. TweeBot sources this news from the newsdata.io API, ensuring your audience stays updated and engaged.

4. **Top 3 Trending Songs**: Curate music content for your followers by sharing the top three trending songs in India. TweeBot fetches this data from the Spotify for Developers API, catering to music enthusiasts among your audience.

5. **Tech and Startup News**: Keep your followers up-to-date with the latest tech and startup news. TweeBot achieves this by web scraping news from [https://news.ycombinator.com/](https://news.ycombinator.com/), providing your audience with valuable insights.

6. **Random Wikipedia Topics**: Spark curiosity and expand your audience's knowledge by posting random Wikipedia topics along with brief explanations. This feature is powered by the Wikipedia library.

7. **Motivational Quotes**: Inspire and uplift your audience by sharing motivational quotes that resonate with them.

8. **Fun Facts**: Add an element of excitement to your followers' timelines with interesting and surprising fun facts that they'll enjoy.

9. **Movie Recommendations**: Get random movie recommendations from TMDB, a platform similar to IMDB. TweeBot helps you discover your next movie night pick.

TweeBot offers an array of cool features, and there are more exciting updates on the horizon. Expect ongoing improvements and new features to keep TweeBot evolving and enhancing your Twitter experience. Stay tuned for updates and additional fun features coming your way!


<br>
<br>

## Usage

To use the bot and post content on Twitter, run the script with one of the following command-line arguments:

- To post a random joke, use the following command:
  ```bash
  python3 bot.py joke
  ```

- To post a fun activity suggestion from the Bored API, use the command:
  ```bash
  python3 bot.py activity
  ```

- To post the latest news from the newsdata.io API, use the command:
  ```bash
  python3 bot.py news
  ```

- To share the top 3 tracks from Spotify (India), use the command:
  ```bash
  python3 bot.py spotify_top_3
  ```

- To retrieve and post the top news from YCombinator's Hacker News, use the command:
  ```bash
  python3 bot.py hacker_news
  ```

- To share a random topic or post from Wikipedia, use the command:
  ```bash
  python3 bot.py wiki_post
  ```

- To post a motivational quote from ZenQuotes, use the command:
  ```bash
  python3 bot.py motivational_quote
  ```

- To share a random fun fact, use the command:
  ```bash
  python3 bot.py funfact
  ```

- To recommend a top movie from TMDB (similar to IMDB), use the command:
  ```bash
  python3 bot.py tmdb_top_movie
  ```

Replace the command in the examples with the desired operation you want to perform. Make sure you have configured your API credentials in `bot_src/creds.py` before running the script.

<br>
<br>

## Contributing
Contributions to TweeBot are welcome! If you have ideas for improvements, bug fixes, or new features, please submit an issue or create a pull request.


<br>
<br>

## License
Tweebot is released under the [GNU General Public License v3.0](LICENSE).


<br>
<br>

 ## 🧑🏻 Know Me More
Developer - <b> Ajay Agrawal </b>
<br>
- 🌌 [Profile](https://github.com/ajayagrawalgit "Ajay Agrawal")
- 🏮 [Email](mailto:ajayagrawalhere@gmail.com?subject=Hi%20from%20<repo-email> "Hi!")
- 👨‍💻 [Linkedin](https://www.linkedin.com/in/theajayagrawal)
- 🐦 [Twitter Bot (@mickbotsays)](https://twitter.com/mickbotsays)


<br>
<h2 align="center"> 🤝 Support Me 🤝 <h2>
<p align="center">
<a href="https://www.buymeacoffee.com/ajayagrawal" title="Buy me a Coffee"><img src="https://user-images.githubusercontent.com/94609372/232127833-d03502af-baf2-46e3-a045-0f7c84531a61.png" alt="Buy me a Coffee"/></a>
</p>
<br><br>
<h4>
<br>
<p align="center"> Made with ♥️ in India </p>
<br>

