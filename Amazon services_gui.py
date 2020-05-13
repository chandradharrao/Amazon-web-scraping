import requests
from bs4 import BeautifulSoup as BS
import smtplib
import PySimpleGUI as gui

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72"}


def send_mail():
    print("send mail called")
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()#establishing the server connection between two gmails
    server.starttls()
    server.ehlo()
    server.login("danceboyyaya@gmail.com","fxemwpnckrcnrawj")
    subject = "Your product is lower than excpected price!"
    body = "Check the amazo link:https://www.amazon.in/Redux-Analogue-Brown-Watch-RWS0200S/dp/B07D9G1GHB/ref=sr_1_1?dchild=1&keywords=offer&qid=1588998564&sr=8-1"
    msg = f"Subject: {subject} \n\nBody: {body}"
    server.sendmail(
        "danceboyyaya@gmail.com",
        "chandradhar.rao@gmail.com",
        msg
    )
    print("Email sent Successfully!")
    server.quit()



def check_price(url,heads):
    print("check prices called")
    page = requests.get(url,headers = heads)
    soup = BS(page.content,"html.parser")
    prod_title_array = soup.find(id = "productTitle").get_text().split()
    prod_title = " ".join(map(str,prod_title_array))
    prod_price_array = soup.find(id = "priceblock_ourprice").get_text().split()
    prod_price_str= " ".join(map(str,prod_price_array))
    prod_price = float(prod_price_str[2::])
    #print("Enter the price of your choice:")
    #comp_price = float(input())
    comp_price = 400.00
    if (comp_price >= prod_price):
        send_mail()

#GUI
gui.theme("DarkAmber")
layout =    [
    [gui.Text("Welcome to Amazon Product Notification")],
    [gui.Text("Enter website URL"),gui.InputText()],
    [gui.Button("Enter"),gui.Button("Exit")]
            ]
window = gui.Window("APN",layout)  #creating window for the layout
#event loop
while True:
    event,values = window.Read()
    if event == None or event == "Exit":
        break
    else:
        check_price(values[0],header)
window.Close()