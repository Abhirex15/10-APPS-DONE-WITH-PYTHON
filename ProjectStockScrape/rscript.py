import requests, bs4
for x in range(233570,233580):
	res = requests.get('http://bescom.org/bescompay/sample.php?ConnectionID='+str(x)+'&en=en')
	res.raise_for_status()
	exampleSoup = bs4.BeautifulSoup(res.text,"html.parser")
	with open("result.txt", "a") as f:
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
