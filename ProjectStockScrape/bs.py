import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

mu_url = 'https://en.wikipedia.org/wiki/Hello_(Adele_song)'

#opening the connection for fetching the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#If the file you are fetching is huge then you should parse it here.
page_soup = soup(page_html, "html.parser")
#page_soup.h1
#page_soup.h3
containers = page_soup.findAll("div",{"class":"mw-body-content"})
