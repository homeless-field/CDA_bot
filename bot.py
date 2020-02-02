from requests import get
from bs4 import BeautifulSoup
from datetime import date

# Get the headline article from the website of local news sources
cdaPress = str(BeautifulSoup(get('https://www.cdapress.com/news/local-news').text, features='html.parser').find('div', class_='headlines-section').h1)
spokesmanReview = str(BeautifulSoup(get('https://www.spokesman.com/idaho').text, features='html.parser').find('h1', class_='lh-solid f4 f3-l mt0 mb1 sans-serif fw8 f2-l nt1-l').text)
krem2 = str(BeautifulSoup(get('https://www.krem.com/section/news/local/kootenai-county').text, features='html.parser').find('div', class_='story-snapshot-with-abstract__mobile-title dot-ellipsis dot-height-135').text)
khq = str(BeautifulSoup(get('https://www.khq.com/news').text, features='html.parser').find('div', class_='card-headline').text)

# Get the 'read more' links of the headlines
cdaPressLink = str(BeautifulSoup(get('https://www.cdapress.com/news/local-news').text, features='html.parser').find('p', class_='read-more').a)
spokesmanReviewLink = str(BeautifulSoup(get('https://www.spokesman.com/idaho').text, features='html.parser').find('h1', class_='lh-solid f4 f3-l mt0 mb1 sans-serif fw8 f2-l nt1-l').a)
krem2Link = str(BeautifulSoup(get('https://www.krem.com/section/news/local/kootenai-county').text, features='html.parser').find('div', class_='story-snapshot-with-abstract__headline').a)
khqLink = str(BeautifulSoup(get('https://www.khq.com/news').text, features='html.parser').find('div', class_='card-headline').a)

# Print the title
print("Today's News (" + date.today().strftime('%a, %x') + ")")
print()
# Print the headlines and the link to the article
print("CDA Press: " + cdaPress[4:-5] + "(https://www.cdapress.com" + cdaPressLink[9:-15] + ")")
print("Spokesman-Review: " + spokesmanReview + "(https://www.spokesman.com" + spokesmanReviewLink[42:-(len(spokesmanReview) + 6)] + ")")
print("KREM2: " + krem2[26:-22] + "(https://www.krem.com" + krem2Link[117:-((len(krem2) * 2) + 190)] + ")")
print("KHQ: " + khq[33:] + "(https://www.khq.com/news" + khqLink[32:-(len(khq) + 5)] + ")")
print()
# Print the "watermark"
print("Disclaimer: News is rarely 100% accurate to reality")
print("I am a bot. To report a bug or make a suggestion, make a comment that includes 'u/QLZX' anywhere in it. View my source code here")
print("Version 1.0, Timestamp: " + date.today().strftime('%a, %x, %H:%M:%S'))
