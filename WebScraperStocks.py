#Description: This programm scraps big indexes stock tickers and their company name from a website

#Import the dependencies
from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from selenium import webdriver


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')


#Create empty lists for Name, DayBefore, Bid, Ask, Percentage, gain/loss, time
company_name = []
stock_bid = []
stock_ask = []
stock_Daybefore = []
percentage = []
gainLoss = []
time = []

while(True): 
     time.clear()
     DRIVER_PATH = 'C:\\Users\\wollenha\\WebScraper\\chromedriver.exe'
     driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
     index = 'dax'
     driver.get('https://www.finanzen.net/aktien/'+index+'-realtimekurse')
     page_source = driver.page_source
     soup = BeautifulSoup(page_source, 'lxml')
     table = soup.find('form' , attrs={'id':'realtime_chart_list'})
     rows = table.find_all('tr')
     driver.quit()

     #Scrapping the needed elements and putting them in the arrays
     for element in rows[1:-3]:
          i = element.find_all('td')
          company_name.append(i[1].text.strip()) #Company Name
          stock_Daybefore.append(i[3].text.strip()) #DayBefore
          stock_bid.append(i[4].text.strip()) #Bid
          stock_ask.append(i[5].text.strip()) #Ask
          percentage.append(i[6].text.strip()) #Percentage gained/lost
          gainLoss.append(i[7].text.strip()) #gain/loss
          time.append(i[8].text.strip()) #Time

     

     #Putting the scraped data in a data frame
     data = pd.DataFrame(columns=['Company Name','Premarket','Bid', 'Ask', '%', '+/-', 'time'])
     data['Company Name'] = company_name
     data['Premarket'] = stock_Daybefore
     data['Bid'] = stock_bid 
     data['Ask'] = stock_ask
     data['%'] = percentage
     data['+/-'] = gainLoss
     data['time'] = time

     #Clearing the arrays for the updated data
     company_name.clear()
     stock_Daybefore.clear()
     stock_bid.clear()
     stock_ask.clear()
     percentage.clear()
     gainLoss.clear()
     

     print(data)
     sleep(5)
     



