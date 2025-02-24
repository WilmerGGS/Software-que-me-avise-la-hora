from datetime import datetime
from tkinter import messagebox
from tkinter import Tk
import time

def saber_hora():
    while True:
        hora_actual = datetime.now()
        hora_hora_minuto = str(hora_actual.hour)+ ":" + str(hora_actual.minute)
        hora_dada_hora_minuto = "10:23" #Aqui puedes controlar la hora que quieres que se active la alarma
        if hora_hora_minuto == hora_dada_hora_minuto:
            main_ventana(hora_dada_hora_minuto)
            break
        else:
            time.sleep(20)  # Verificar cada 20 segundos

def main_ventana(hora_dada_hora_minuto):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(message= f"DEBES IRTE YA ES LA HORA DEL ALMUERZO: {hora_dada_hora_minuto} PM")
    root.destroy()


if __name__ == "__main__":
    saber_hora()