from tkinter  import *

root =Tk()
root .title ('Супер! Пупер! Шмупер! Хаус! КЛИИКЕРРРРР!!!')
root.geometry ('500x200')
count = 0
nagrada = 1



def click():
    print('НАЖАТА КНОПКА 1')
    global  count
    count  += nagrada
    schetchik .config (text = str (count) +'$')


def func_x10():
    print('нажата кнопка 2')
    global count
    if  count  >= 100:

         count  -= 100
         global  nagrada
         nagrada  = 10
    schetchik.config (text=str(count ) + '$')


def  func_x100():
    global  count


    if count  >= 7000:
        count  -= 7000
        global  nagrada
        nagrada = 100


schetchik = Label (root , text='0$')
schetchik.pack()

knopka =Button (root, text='НАЖМИ МЕНЯ!!!', command=click)
knopka.pack ()

knopka_x10= Button(root , text='x10 (100$)', command=func_x10)
knopka_x10.pack ()

knopka_x100= Button (root , text='x100 (10000$)',command=func_x100)
knopka_x100.pack ()

root.mainloop()