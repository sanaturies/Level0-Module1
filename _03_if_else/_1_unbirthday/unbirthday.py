
from datetime import date
today=date.today()
today2=today.strftime('%B %d')
print(today2)
day=input('when is your birthday? ')
if day==today2:
    print('happy birthday!')
else:
    print('happy unbirthday!')
