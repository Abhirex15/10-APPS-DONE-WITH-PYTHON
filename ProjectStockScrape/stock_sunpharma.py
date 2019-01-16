from pandas_datareader import data
from pandas_datareader.data import get_quote_yahoo
import datetime

start = datetime.date.today()
end = datetime.date.today()
df = data.DataReader(name="SUNPHARMA.NS",data_source="yahoo",start=start,end=end)
print(df)

print(get_quote_yahoo('SUNPHARMA.NS'))
