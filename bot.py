from time import sleep
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import praw

# Information about the bot and its account
reddit = praw.Reddit(user_agent='CDA_bot (by /u/QLZX)', client_id='*', client_secret='*', username='CDA_bot', password='*')

while True:
    # Get the website of local news sources
    cdaPress = BeautifulSoup(get('https://www.cdapress.com/news/local-news').text, features='html.parser')
    spokesmanReview = BeautifulSoup(get('https://www.spokesman.com/idaho').text, features='html.parser')
    krem2 = BeautifulSoup(get('https://www.krem.com/section/news/local/kootenai-county').text, features='html.parser')
    khq = BeautifulSoup(get('https://www.khq.com/news').text, features='html.parser')

    # Get a bulletin headline from each news source
    cdaPressHeadline = str(cdaPress.find('div', class_='headlines-section').h1)
    spokesmanReviewHeadline = str(spokesmanReview.find('h1', class_='lh-solid f4 f3-l mt0 mb1 sans-serif fw8 f2-l nt1-l').text)
    krem2Headline = str(krem2.find('div', class_='story-snapshot-with-abstract__mobile-title dot-ellipsis dot-height-135').text)
    khqHeadline = str(khq.find('div', class_='card-headline').text)

    # Get a link to the bulletin articles
    cdaPressLink = str(cdaPress.find('p', class_='read-more').a)
    spokesmanReviewLink = str(spokesmanReview.find('h1', class_='lh-solid f4 f3-l mt0 mb1 sans-serif fw8 f2-l nt1-l').a)
    krem2Link = str(krem2.find('div', class_='story-snapshot-with-abstract__headline').a)
    khqLink = str(khq.find('div', class_='card-headline').a)

    # Set the title of the post
    title = "Today's News (" + datetime.now().strftime('%a, %x') + ")"

    # Set the body text of the post
    text = "CDA Press: [" + cdaPressHeadline[4:-5] + "](https://www.cdapress.com" + cdaPressLink[9:-15] + ")\n\n"
    text += "Spokesman-Review: [" + spokesmanReviewHeadline + "](https://www.spokesman.com" + spokesmanReviewLink[42:-(len(spokesmanReviewHeadline) + 6)] + ")\n\n"
    text += "KREM2: [" + krem2Headline[26:-22] + "](https://www.krem.com" + krem2Link[117:-((len(krem2Headline) * 2) + 190)] + ")\n\n"
    text += "KHQ: [" + khqHeadline[33:] + "](https://www.khq.com/news" + khqLink[32:-(len(khqHeadline) + 5)] + ")\n\n"

    # Add a "disclaimer" to the post
    text += "^^I ^^am ^^a ^^bot. ^^To ^^report ^^a ^^bug ^^or ^^make ^^a ^^suggestion, ^^just ^^make ^^a ^^comment. ^^View ^^my ^^source ^^code ^^[here](https://github.com/homeless-field/CDA_bot)\n\n"
    text += "^^Version ^^1.0, ^^Timestamp: " + datetime.now().strftime('^^%x, ^^%H:%M:%S')

    # Remove any non-ascii characters from the headlines
    text = ''.join((c for c in text if 0 < ord(c) < 127))

    # Make the post in r/coeurdalene
    subreddit = reddit.subreddit('coeurdalene')
    subreddit.submit(title, text)
    sleep(86400)
