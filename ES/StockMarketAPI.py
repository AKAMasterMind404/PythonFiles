import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info

# get historical market data
hist = msft.history(period="max")
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
k=msft.info
# for i in k:
#     # if i[0].lower()=='p' or i[0].lower()=='b':
#         print(i,':',k[i])

# k=msft.balance_sheet
for i in k:
    if i[0].lower() in ['f']:#'c','d','f','s'
        print(i,':',k[i])

# with open('testing.py','w+') as f:
#     f.write('dictionaryform=')
#     response=list(k)
#     for i in range(len(response)):
#         if ''.join(response[i:i+5])=='true}':
#             response[i]='T'
#     f.write(''.join(response))
"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}
"""
Theattributes=[
    'priceToBook',
    'profitMargins',
    'payoutRatio',
    'previousClose',
    'priceHint',
    'pegRatio',
    'dividendRate',
    'dayHigh',
    'dayLow',
    'dividendYield',
    'fiftyTwoWeekHigh',
    'fiftyTwoWeekLow',
    'forwardPE',
    ]
# get historical market data, here max is 5 years.
msft.history(period="max")