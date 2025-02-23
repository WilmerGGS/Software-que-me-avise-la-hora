from datetime import datetime
from tkinter import messagebox
from tkinter import Tk
import time

def main():
    while True:

        hora_actual = datetime.now()
        hora_hora_minuto = str(hora_actual.hour)+ ":" + str(hora_actual.minute)
        hora_dada_hora_minuto = "12:25"

        if hora_hora_minuto == hora_dada_hora_minuto:
            root = Tk()
            root.withdraw()
            messagebox.showinfo(message= f"DEBES IRTE YA ES LA HORA DEL ALMUERZO: {hora_dada_hora_minuto} PM")
            root.destroy()
            break
        else:
            time.sleep(20)  # Verificar cada 20 segundos


if __name__ == "__main__":
    main()