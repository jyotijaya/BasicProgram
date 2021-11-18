#Code to fetch previous date in dd-month-year
from datetime import date,timedelta
from mftool import Mftool

today = date.today()

yesterday=today-timedelta(days=1)
# Month abbreviation, day and year
yesterday_date = yesterday.strftime("%d-%b-%Y")
print("yes_date =", yesterday_date)

#Instantiate mftool.
mf = Mftool()
quote=mf.get_scheme_quote('122639')
print(quote)

print(quote['last_updated'])

if quote['last_updated']==str(yesterday_date):
    day_before_yesterday = today - timedelta(days=2)

    day_beforeyesterday_date = day_before_yesterday.strftime("%d-%b-%Y")
    print("day_before_yesterday_date =", day_beforeyesterday_date)
    his_nav=mf.get_scheme_historical_nav('122639')
    print(his_nav['data'][1])

    # dd/mm/YY
    d1 = today- timedelta(days=2)
    d2 = d1.strftime("%d/%m/%Y")
    print("d1 =", d2)
    if str(d2)==str(his_nav['data'][1]['date']):
        back_nav= his_nav['data'][1]['nav']
        print(back_nav)