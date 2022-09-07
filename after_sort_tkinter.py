from tkinter import *
from tkinter import ttk


def start():
    alist = enter.get().split()
    alist = [int(i) for i in alist]

    if len(lab_list) > 0:
        for i in range(len(lab_list)):
            lab_list[0].after(1, lab_list[0].destroy())
            lab_list.pop(0)

    for i in range(len(alist)):
        a = Label(mainframe, text=str(alist[i]))
        a.grid(column=1, row=3 + i, sticky=W)
        lab_list.append(a)
    button.state(["disabled"])
    enter_entry.state(["disabled"])
    root.after(1, step(alist))


def step(alist, i=0):  # ['2', '-1', '3']
    if i < len(alist):

        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

        for k in range(len(lab_list)):
            lab_list[k].configure(text=str(alist[k]))
        i += 1

        root.update_idletasks()
        root.after(1000)
        root.after(1, lambda: step(alist, i))

    if i == len(alist):
        button.state(["!disabled"])
        enter_entry.state(["!disabled"])
        for k in range(len(alist)):
            lab_list[k].configure(background="#99ff99")
        return


root = Tk()
root.title("Графика")
root.geometry('400x400')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Label(mainframe, text='ввод: ').grid(column=1, row=1, sticky=W)

enter = StringVar()
enter_entry = ttk.Entry(mainframe, width=7, textvariable=enter)
enter_entry.grid(column=2, row=1, sticky=(W, E))

button = ttk.Button(mainframe, text="сортировать", command=start)
button.grid(column=2, row=2, sticky=W)

lab_list = []

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
