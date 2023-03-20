from django.shortcuts import render
from .models import Match
from datetime import date
import time
from time import mktime
from dateutil.relativedelta import relativedelta



# Create your views here.


def home(request):
    present = date.today()+ relativedelta(days=+3)
    my_date = ["01/03/2023", "05/03/2023", "12/03/2023", "19/03/2023",
               "26/03/2023", "02/04/2023", "10/04/2023", "17/04/2023",
               "24/04/2023", "01/05/2023", "08/05/2023", "15/05/2023",
               "22/05/2023", "29/05/2023", "05/06/2023", "12/06/2023",
               "19/06/2023", "26/06/2023"]
    print(present)

    new_converted_date = []
    for d in range(16):
        new_converted_date.append(time.strptime(my_date[d], "%d/%m/%Y"))

    new_date = []
    for nd in range(16):
        new_date.append(date.fromtimestamp(mktime(new_converted_date[nd])))

    leagues = []
    kolejka = []
    for liga in range(10):
        leagues.append(f"leagues{liga}")
        for gw in range(16):
            kolejka.append(f"kolejka{gw}")
            if new_date[gw-1] < present <= new_date[gw]:
                leagues[liga] = Match.objects.filter(league=liga).filter(kolejka=gw)
            else:
                gw += 1

    return render(request, 'ktogra/html.html',
                  {'3liga': leagues[3], '4liga': leagues[4], '5liga': leagues[5], 'okregowka': leagues[6],
                   'aklasa': leagues[7], 'bklasa1': leagues[8], 'bklasa2': leagues[9],})



'''    my_date = ["01/03/2023", "20/03/2023", "27/03/2023", "03/04/2023",
               "10/04/2023", "17/04/2023", "24/04/2023", "01/05/2023",
               "08/05/2023", "15/05/2023", "22/05/2023", "29/05/2023",
               "05/06/2023", "12/06/2023", "19/06/2023", "26/06/2023"]'''