from datetime import date
from datetime import datetime

def year_to_age(name,bdate): #enter a string in form yyyy-mm-dd
    today = datetime.now()
    # Calculate age
    try:
        dt = datetime.date(datetime.strptime(bdate, "%Y-%m-%d"))
        age = today.year - dt.year
        return age
    except: 
        print("Invaild DOB format!")

a1 = Swimmer('Kim','1987-04',76,178,75,68)
year_to_age(a1.name,a1.DOB)
