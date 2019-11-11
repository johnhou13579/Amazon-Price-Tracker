import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Philips-Hue-Ambiance-LightStrip-Assistant/dp/B07GWKB1ZS/ref=pd_rhf_se_p_img_4?_encoding=UTF8&psc=1&refRID=Y3F9231X93HNFAEQESRT'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    print(converted_price)
    print(title.strip())

    if(converted_price < 70.00):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('houj@oxy.edu', '')

    subject = 'Price fell down!'
    body = 'Check Amazon link https://www.amazon.com/Philips-Hue-Ambiance-LightStrip-Assistant/dp/B07GWKB1ZS/ref=pd_rhf_se_p_img_4?_encoding=UTF8&psc=1&refRID=Y3F9231X93HNFAEQESRT'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'houj@oxy.edu',
        'houj@oxy.edu',
        msg
    )
    print('Email sent')
    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 24)