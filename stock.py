import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web

style.use("ggplot")
start = dt.datetime(2006, 1, 1)
end = dt.datetime(2018, 2, 1)

data_source = 'yahoo'
# df = web.get_data_yahoo("AAPL", start, end)
# df2 = web.get_data_yahoo("MSFT", start, end)

tickers = ['AAPL', 'SNAP']
start_date = '2010-01-01'
end_date = '2018-02-08'
panel_data = web.DataReader(tickers, data_source, start_date, end_date)
close = panel_data.ix['Close']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
close = close.reindex(all_weekdays)
close.head(10)
# plt.show()
print("Apple" + " is red and" + "Microsoft" + " is blue")
