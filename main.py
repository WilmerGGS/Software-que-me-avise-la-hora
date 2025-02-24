from datetime import datetime
from tkinter import messagebox
from tkinter import Tk
import time
import winsound

def sonido_peekman_dialogo(hora_dada_hora_minuto, sound_file):
    root = Tk()
    root.withdraw()
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)
    messagebox.showinfo(message= f"DEBES IRTE YA ES LA HORA DEL ALMUERZO: {hora_dada_hora_minuto} PM")
    root.destroy()
    return

def saber_hora():
    while True:
        hora_actual = datetime.now()
        hora_hora_minuto = str(hora_actual.hour)+ ":" + str(hora_actual.minute)
        hora_dada_hora_minuto = "17:30" #Aqui puedes controlar la hora que quieres que se active la alarma
        if hora_hora_minuto == hora_dada_hora_minuto:
            sonido_peekman_dialogo(hora_dada_hora_minuto, sound_file="Que-hay-de-nuevo-perr4_-Jesse-pinkman_MP3_320K_.wav")
            break
        else:
            time.sleep(10)  # Verificar cada 20 segundos

if __name__ == "__main__":
    saber_hora()