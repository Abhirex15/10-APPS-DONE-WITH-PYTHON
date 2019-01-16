from nsetools import Nse
from pprint import pprint
from time import sleep

nse = Nse()

q = nse.get_quote('SUNPHARMA')




for i in q:
    sleep(2)
    pprint(q[:3])
