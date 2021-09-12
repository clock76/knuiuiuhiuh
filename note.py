from tkinter import *
from tkinter import filedialog as fd


def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

def child_window():
    win = Toplevel(root)
    x_entry = Entry(win)
    x_entry.pack()
    y_entry = Entry(win)
    y_entry.pack()


    def set_child_window():
        new_x = x_entry.get()
        new_y = y_entry.get()
        root.geometry(new_x + 'x' + new_y)

    Button(win, text = 'Ok', command = set_child_window).pack()

root = Tk()
mainmenu = Menu(root)
root.config(menu = mainmenu)
root.title('блокнот')

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = 'Сохранить', command = extract_text)
filemenu.add_command(label = 'Открыть', command = insert_text)


text = Text()
text.pack()

mainmenu.add_cascade(label = 'Файл', menu = filemenu)
mainmenu.add_command(label = 'Настройки', command = child_window)


root.mainloop()