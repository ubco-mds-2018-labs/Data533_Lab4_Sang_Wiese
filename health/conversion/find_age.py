from datetime import date
from datetime import datetime

def year_to_age(name,bdate): #enter a string in form yyyy-mm-dd
    today = datetime.now()
    # Calculate age
    dt = datetime.date(datetime.strptime(bdate, "%Y-%m-%d"))
    age = today.year - dt.year
    if today.month < dt.month or (today.month == dt.month and today.day < dt.day):
        age = age - 1   # Handle case when have not had birthday yet
    #print("%s Age: %s" %(name,age))
    return age
