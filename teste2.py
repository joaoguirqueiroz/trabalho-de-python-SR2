import csv
import os
from datetime import datetime

def duraca_evento(horario_inicio, horario_fim) ->int:

    try:

        H_ini, Mnin = map ( int, horario_inicio.split(":"))
        H_fim, Mfim = map ( int, horario_fim.split(":")) 
        calc_tempo = (H_fim * 60 + Mfim) - (H_ini * 60 + Mnin)
        if calc_tempo <=0 :
            calc_tempo +=24 * 60
        return calc_tempo
    except (ValueError, AttributeError):
        
