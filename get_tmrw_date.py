import datetime as dt
today = dt.date.today()
td = dt.timedelta(days=1)
tmrw = today + td
print(tmrw.isoformat())
