from datetime import datetime, date, time, timedelta

def delivery_date(start, description):
    start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    if description == "NOW":
        dt = start + timedelta(hours=2)
        
    elif description == "ASAP":
        if start.hour < 13:
            dt = start + timedelta(hours=(17-start.hour), minutes=-start.minute)
        else:
            dt = start + timedelta(days=1, hours=(13-start.hour), minutes=-start.minute)
    

    elif description == "EOW":
        dia_semana = start.weekday()
        print(dia_semana)
        if (dia_semana == 3 or dia_semana == 4):
            dt = start + timedelta(days=(6-dia_semana), hours=(20-start.hour), minutes=-start.minute)
        else:
            dt = start + timedelta(days=(4-dia_semana), hours=(17-start.hour), minutes=-start.minute)

    elif "M" in description:
        n_description = int(description.replace("M",""))
        if n_description <= start.month:
            dt = datetime(start.year+1, n_description, 1, 8,0)
            while dt.isoweekday()> 5:
                dt = dt + timedelta(days=1)
        if n_description > start.month:
            dt = datetime(start.year, n_description, 1, 8,0)


    elif "Q" in description:
        n_description = int(description.replace("Q",""))
        if n_description > start.month//3:
            dt = datetime(start.year, n_description*3, 30, 8,0)
            print(dt)
            while dt.isoweekday()> 5:
                dt = dt + timedelta(days=1)
        if n_description <= start.month//3:
            dt = datetime(start.year+1, n_description*3, 29, 8,0)

        
    return dt.strftime("%Y-%m-%dT%H:%M:%S")

