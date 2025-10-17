from collections import defaultdict

def tally(historial_partidos):
    tabla = defaultdict(lambda: {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})
    
    for partido in historial_partidos:
        e1, e2, r = partido.split(";")
        tabla[e1]["MP"] += 1
        tabla[e2]["MP"] += 1
        if r == "win": tabla[e1]["W"] += 1; tabla[e1]["P"] += 3; tabla[e2]["L"] += 1
        elif r == "loss": tabla[e2]["W"] += 1; tabla[e2]["P"] += 3; tabla[e1]["L"] += 1
        else: tabla[e1]["D"] += 1; tabla[e1]["P"] += 1; tabla[e2]["D"] += 1; tabla[e2]["P"] += 1
    
    resultado = ["Team                           | MP |  W |  D |  L |  P"] + [
        f"{e.ljust(30)} |  {d['MP']} |  {d['W']} |  {d['D']} |  {d['L']} | {d['P']:>2}"
        for e, d in sorted(tabla.items(), key=lambda x: (-x[1]['P'], x[0]))]
    
    return resultado