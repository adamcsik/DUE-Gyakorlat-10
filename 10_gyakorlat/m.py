from tkinter import *
import objektumok


def jelszokiiras():
    try:
        p.jelszohossz = int(hossz.get())
    except:
        '''
        jelszo_ertek['state'] = NORMAL
        jelszo_ertek.delete(1.0, END)
        jelszo_ertek.insert(END, 'Nem szám')
        jelszo_ertek.grid(row=0, column=1)
        jelszo_ertek['state'] = DISABLED
        '''
        hibaablak = Toplevel(ablak)
        ablak.geometry('300x200')
        hibauzenet = Label(hibaablak, text='Csak számot adhat meg!', fg='red')
        hibauzenet.pack()
        ok = Button(hibaablak, text="OK", command=hibaablak.destroy)
        ok.pack()
    else:
        p.van_szamjegy = szamjegy.get()
        p.van_irasjel = irasjel.get()
        p.jelszogenerator()
        jelszo.set(p.jelszo)
        jelszo_ertek['state'] = NORMAL
        jelszo_ertek.delete(1.0, END)
        jelszo_ertek.insert(END, p.jelszo)
        jelszo_ertek.grid(row=0, column=1)
        jelszo_ertek['state'] = DISABLED


p = objektumok.Jelszoobjektum()

ablak = Tk()
ablak.title('Jelszógenerálás')
ablak.geometry('600x400')
ablak.minsize(width=300, height=120)
jelszo = StringVar()

jelszo_cimke = Label(ablak, text='Jelszó:')
jelszo_cimke.grid(row=0, column=0, sticky=E)

jelszo_ertek = Text(ablak, height=1, width=20, state=DISABLED)
jelszo_ertek.grid(row=0, column=1)

jelszo_hossza = Label(ablak, text='Jelszó hossza:')
jelszo_hossza.grid(row=1, column=0, sticky=E)

hossz = Entry(ablak, width=10)
hossz.insert(0, '8')
hossz.grid(row=1, column=1, sticky=W)

szamjegy = BooleanVar()
szamjegy_pipa = Checkbutton(ablak, text='Kell számjegy?', variable=szamjegy)
szamjegy_pipa. grid(row=2, column=0)

irasjel = BooleanVar()
irasjel_pipa = Checkbutton(ablak, text='Kell írásjel?', variable=irasjel)
irasjel_pipa.grid(row=2, column=1)

jelszo_gomb = Button(ablak, text='Generálás', command=jelszokiiras)
jelszo_gomb.grid(row=3, column=0)

lezaro_gomb = Button(ablak, text='Lezárás', command=ablak.destroy)
lezaro_gomb.grid(row=3, column=1)

mainloop()
