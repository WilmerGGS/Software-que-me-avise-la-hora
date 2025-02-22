from datetime import datetime
from tkinter import messagebox

def main():
    while True:

        hora_actual = datetime.now()
        hora_hora_minuto = str(hora_actual.hour)+ ":" + str(hora_actual.minute)
        hora_dada_hora_minuto = "12:20"

        if hora_hora_minuto == hora_dada_hora_minuto:
            messagebox.showinfo(message= f"DEBES IRTE YA ES LA HORA DEL ALMUERZO: {hora_dada_hora_minuto} PM")
            break
        else:
            pass


if __name__ == "__main__":
    main()