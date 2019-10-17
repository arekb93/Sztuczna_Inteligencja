
import numpy
import pandas as pd
import requests
import matplotlib.pyplot as plt

def getCurrency(currency, startDate, endDate):
    
    currency_req = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/'+currency+'/'+startDate+'/'+endDate+'/')
    currency_data = currency_req.json()
    currency_data['rates']
    
    exchange_rate = pd.DataFrame.from_dict(currency_data['rates'])
    exchange_rate
    exchange_rate.head()
    
    return (exchange_rate.set_index(['effectiveDate'])['mid'])
    
# wczytanie pierwszej waluty    
usd = (getCurrency('usd','2019-09-01','2019-10-06'))
plt.plot(usd, label='USD')
#wczytanie drugiej waluty
eur = (getCurrency('eur','2019-09-01','2019-10-06'))
plt.plot(eur, label='EUR')
#wykres obu walut  
plt.legend()  
plt.show()

#korelacja dwóch kursów
ratesCorr = numpy.corrcoef(usd,eur)
print('Korelacja obu kursów:')
print(ratesCorr[0])