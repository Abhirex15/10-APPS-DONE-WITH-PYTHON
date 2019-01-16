import requests, bs4
for x in range(233570,233580):
	res = requests.get('https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=SUNPHARMA&illiquid=0&smeFlag=0&itpFlag=0#'+str(x)+'&en=en')
	res.raise_for_status()
	exampleSoup = bs4.BeautifulSoup(res.text,"html.parser")
	with open("ross.txt", "a") as f:
		elems = exampleSoup.select('#txtsubdiv')
		t=(str(elems[0])).split("value",1)[1]
		f.write(t[2:-3] + ',')


		elems = exampleSoup.select('#txtphno')
		t=(str(elems[0])).split("value",1)[1]
		f.write(t[2:-3] + ',')


		elems = exampleSoup.select('#txtRRNO')
		t=(str(elems[0])).split("value",1)[1]
		f.write(t[2:-3] + ',')



		elems = exampleSoup.select('#txtemailid')
		t=(str(elems[0])).split("value",1)[1]
		f.write(t[2:-3] + ',')


		elems = exampleSoup.select('#txtConnectionID')
		t=(str(elems[0])).split("value",1)[1]
		f.write(t[2:-3] + ',')

		elems = exampleSoup.select('#txtBillTotal')
		t=(str(elems[0])).split("value",1)[1]
		f.write(t[2:-3] + ',')

		elems = exampleSoup.select('#txtCustomerName')
		t=(str(elems[0])).split("rows",4)[1]
		f.write(t[6:-11] + ',')
