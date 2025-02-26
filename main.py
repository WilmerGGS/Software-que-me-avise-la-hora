from datetime import datetime
import tkinter as tk
import time
import winsound

def saber_hora():
    while True:
        hora_actual = datetime.now()
        hora_hora_minuto = str(hora_actual.hour)+ ":" + str(hora_actual.minute)
        hora_dada_hora_minuto = "15:36" #Aqui puedes controlar la hora que quieres que se active la alarma
        if hora_hora_minuto == hora_dada_hora_minuto:
            ventana_jesse_peekman(hora_dada_hora_minuto, sound_file="Que-hay-de-nuevo-perr4_-Jesse-pinkman_MP3_320K_.wav")
            break
        else:
            time.sleep(10)  # Verificar cada 10 segundos

def ventana_jesse_peekman(hora_dada_hora_minuto, sound_file):
    ventana = tk.Tk()
    ventana.title("AVISO")
    # Centrar la ventana en la pantalla
    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()
    wventana = 400
    hventana = 50
    pwidth = round(wtotal/2 - wventana/2)
    pheight = round(htotal/2 - hventana/2)
    ventana.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")
    ventana.resizable(0, 0)
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)
    mensaje_label = tk.Label(text=f"DEBES IRTE YA ES LA HORA DEL ALMUERZO: {hora_dada_hora_minuto}PM")
    mensaje_label.pack()
    boton_continuar = tk.Button(text="CONTINUAR", command=ventana.destroy)
    boton_continuar.pack()
    ventana.mainloop()

if __name__ == "__main__":
    saber_hora()