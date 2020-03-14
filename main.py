import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req_url
from twilio.rest import Client
from flask import Flask


app=Flask(__name__)

@app.route("/")
def home():
    return "App is up and running!"

@app.route('/read')
def read_news():
    url = 'https://news.google.com/?hl=en-US&gl=US&ceid=US:en'

    page = req_url(url)
    page_html = page.read()
    page.close()

    page_soup = soup(page_html,'html.parser')
    page_cotent = page_soup.findAll("h3",{'class':'ipQwMb ekueJc RD0gLb'})
    news_list = []
    for i in range (0,6):
        news = page_cotent[i].a.text
        news_list.append(news)
#print(news_list)
    print('Here are the headlines of the hour:', *news_list, sep='\n- ')
    return news_list

@app.route('/send')
def send_news():
    print('Sending message')
    new_list = read_news()
    client = Client('ACa59186dc614bf22dbe691648c64877e0','4d1a150ad768729f1d352e8ddcb1cd91')
    client.messages.create(to='+33752711105',
                           from_ = '+12029315762',
                           body = new_list)
    
    
if __name__ == "__main__":
    app.run()
