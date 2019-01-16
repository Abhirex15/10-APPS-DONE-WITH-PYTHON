from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=SUNPHARMA&illiquid=0&smeFlag=0&itpFlag=0")

volume=driver.find_element_by_xpath('//*[@id="totalSellQuantity"]')


print(volume)
