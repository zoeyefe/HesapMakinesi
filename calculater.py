import tkinter as tk
from tkinter import messagebox

def toplama():
    if number1.get().isdigit() and number2.get().isdigit():
        n1 = float(number1.get())
        n2 = float(number2.get())
        sonuc.configure(text=str(n1+n2))
def çıkarma():
    if number1.get().isdigit() and number2.get().isdigit():
        n1 = float(number1.get())
        n2 = float(number2.get())
        sonuc.configure(text=str(n1-n2))
def çarpma():
    if number1.get().isdigit() and number2.get().isdigit():
        n1 = float(number1.get())
        n2 = float(number2.get())
        sonuc.configure(text=str(n1*n2))
def bölme():
    if number1.get().isdigit() and number2.get().isdigit():
        n1 = float(number1.get())
        n2 = float(number2.get())
        sonuc.configure(text=str(n1/n2))
def bilgilen():
    messagebox.showinfo("Bilgilendirme", "Proje ne zaman üretildi 16.02.2023 15.15")
    messagebox.showinfo("Bilgilendirme", "Kim tarafından üretildi: Mehmet Efe Servili")


pencere = tk.Tk()
pencere.title('Hesap Makinesi | Created by AGO Roboteam')
ekrangenis=pencere.winfo_screenwidth()//2-160
ekranyuksek=pencere.winfo_screenheight()//2-150
pencere.geometry("485x285+{}+{}".format(ekrangenis, ekranyuksek))
pencere['background']='#d4d1d1'


sonuc = tk.Label(pencere, bg='#d4d1d1',text="Sonuç",font="Times 12", width=30, justify="center")
sonuc.place(x=-50, y=20)
number1 = tk.Entry(pencere, font="Courier 14 bold", width=15, justify="right")
number1.place(x=70, y=50)
number2 = tk.Entry(pencere, font="Courier 14 bold", width=15, justify="right")
number2.place(x=70, y=80)

tus1 = tk.Button(pencere, text="+", font="Courier 14 bold", width=10, command=toplama)
tus1.place(x=90, y=110)
tus2 = tk.Button(pencere, text="-", font="Courier 14 bold", width=10, command=çıkarma)
tus2.place(x=90, y=150)
tus3 = tk.Button(pencere, text="*", font="Courier 14 bold", width=10, command=çarpma)
tus3.place(x=90, y=190)
tus4 = tk.Button(pencere, text="/", font="Courier 14 bold", width=10, command=bölme)
tus4.place(x=90, y=230)
bilgilendirme = tk.Button(pencere, text="Bilgilendirme İçin Tıklayınız", font="Times 12", width=20, command=bilgilen)
bilgilendirme.place(x=300, y=0)
ago = tk.Label(pencere, bg='#d4d1d1',text="AGO ROBOTEAM",font="Times 12", width=30, justify="center")
ago.place(x=250, y=250)

number1.focus()

pencere.mainloop()