#?sayaç uygulaması
import tkinter as tk

sayac = 0
form = tk.Tk()
form.geometry("350x300+500+150")
form.title("sayaç Uygulaması")
form.config(bg="yellow")
x = tk.IntVar()

giris = tk.Entry(form,textvariable=x)
giris.place(x=60,y=50)
giris_lbl = tk.Label(text="Giriş",bg="yellow",font="consoles 11 bold")
giris_lbl.place(x=10,y=50)

def cevir():
    global sayac
    sayac=sayac+int(x.get())
def ilerisay():
    global sayac
    if sayac>=0:
        sayım_lbl.config(text=sayac)
        sayac=sayac+1
        sayım_lbl.after(200,ilerisay)
def gerisay():
    global sayac
    if sayac>=0:
        sayım_lbl.config(text=sayac)
        sayac=sayac-1
        sayım_lbl.after(200,gerisay)
buton1 = tk.Button(form,text="Geri Say",activebackground="red",command=gerisay)
buton1.place(x=60,y=90)
buton2 = tk.Button(form,text="İleri Say",activebackground="red",command=ilerisay)
buton2.place(x=130,y=90)
buton3 = tk.Button(form,text="Cevir",activebackground="red",command=cevir)
buton3.place(x=200,y=90)


sayım_lbl = tk.Label(bg="white",font="times 40 bold")
sayım_lbl.place(x=150,y=200)
form.mainloop()