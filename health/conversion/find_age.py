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


