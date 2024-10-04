import praw

# Initialize Reddit API
reddit = praw.Reddit(
    client_id='mhY1T0Ir_s6iWarCXs8aDA',
    client_secret='iw33SyG3q_MhEE18oc3jR2UpSeDDDA',
    user_agent='WebScraping'
)

# scrape subreddit titles
def scrape_subreddits(subreddits):
    with open('Texts/reddit_titles.txt', 'a', encoding='UTF-8') as file:
        for redditname in subreddits:
            subreddit = reddit.subreddit(redditname)
            print(f'Scraping {redditname}...')
            for submission in subreddit.top(time_filter='week', limit=500):
                file.write(f"{submission.title}\n")

# List of subreddits to scrape
subreddits = [
    'worldnews', 'funny', 'AskReddit', 'gaming', 'movies', 'aww', 
    'Music', 'science', 'politics', 'legaladvice', 'space', 
    'Showerthoughts', 'philosophy', 'history'
]

scrape_subreddits(subreddits)
