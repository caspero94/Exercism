from datetime import datetime, date, time, timedelta

def siguiente_dia_habil(fecha):
    while fecha.weekday() >= 5:
        fecha += timedelta(days=1)
    return fecha

def ultimo_dia_habil_mes(ano, mes):
    if mes == 12:
        siguiente_mes = datetime(ano+1, 1, 1)
    else:
        siguiente_mes = datetime(ano,mes+1, 1)
    fecha = siguiente_mes - timedelta(days=1)
    while fecha.weekday() >= 5:
        fecha -= timedelta(days=1)
    return fecha

def delivery_date(start, description):
    start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    if description == "NOW":
        dt = start + timedelta(hours=2)

    elif description == "ASAP":
        if start.hour < 13:
            dt = start.replace(hour=17, minute=0, second = 0)
        else:
            dt = (start + timedelta(days=1)).replace(hour=13, minute=0)
            
    elif description == "EOW":
        dia_semana = start.weekday()
        if dia_semana <= 2:
            dias_hasta_viernes = 4 - dia_semana
            dt = (start + timedelta(days=dias_hasta_viernes)).replace(hour=17, minute=0)
        else:
            dias_hasta_domingo = 6 - dia_semana
            dt = (start + timedelta(days=dias_hasta_domingo)).replace(hour=20, minute=0)

    elif description.endswith("M"):
        n = int(description[:-1])
        if start.month < n:
            dt = datetime(start.year, n, 1, 8, 0)
        else:
            dt = datetime(start.year+1, n, 1, 8, 0)
        dt = siguiente_dia_habil(dt)

    elif description.startswith("Q"):
        n = int(description[1:])
        trimestre_actual = (start.month -1) // 3 +1
        mes_final = n*3
        if start.month <= n*3 and trimestre_actual <= n:
            dt = ultimo_dia_habil_mes(start.year, mes_final).replace(hour=8, minute=0)
        else:
            dt = ultimo_dia_habil_mes(start.year+1, mes_final).replace(hour=8, minute=0)
            
    
    return dt.strftime("%Y-%m-%dT%H:%M:%S")

