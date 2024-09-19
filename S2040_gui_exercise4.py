""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk
from tkinter import ttk


def empty_entry():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    print("Cleared Entry boxes")


def read_table(tree):
    count = 0
    for record in test_data_list:
        if count % 2 == 0:
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1

def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    entry1.delete(0, tk.END)
    entry1.insert(0, values[0])
    entry2.delete(0, tk.END)
    entry2.insert(0, values[1])
    entry3.delete(0, tk.END)
    entry3.insert(0, values[2])


main_window = tk.Tk()
main_window.title("my first GUI")

container = tk.LabelFrame(main_window, text="Container")
container.grid(row=0, column=0, padx=3, pady=2)
frame1 = tk.Frame(container)
frame1.grid(row=0, pady=5)
frame2 = tk.Frame(container)
frame2.grid(row=1, padx=18, pady=4)
frame3 = tk.Frame(container)
frame3.grid(row=2, padx=18, pady=15)

test_data_list = []
test_data_list.append(("1", 1000, "oslo"))
test_data_list.append(("2", 2000, "chicago"))
test_data_list.append(("3", 3000, "milano"))
test_data_list.append(("4", 4000, "amsterdam"))

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#eeeeee", foreground="black", rowheight=24, fieldbackground="#eeeeee")
style.map('Treeview', background=[('selected', "#5c5c5c")])

tree_1_scrollbar = tk.Scrollbar(frame1)
tree_1_scrollbar.grid(row=5, column=6, pady=4, sticky='ns')
tree_1 = ttk.Treeview(frame1, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=5, column=5, padx=0, pady=4)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("col1", "col2", "col3")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=40)
tree_1.column("col2", anchor=tk.E, width=80)
tree_1.column("col3", anchor=tk.W, width=200)

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("col1", text="Id", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)

tree_1.tag_configure('oddrow', background="#dddddd")
tree_1.tag_configure('evenrow', background="#cccccc")

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))

label1 = tk.Label(frame2, text="Id")
label1.grid(row=0, column=0, pady=9)
label2 = tk.Label(frame2, text="Weight")
label2.grid(row=0, column=1)
label3 = tk.Label(frame2, text="Destination")
label3.grid(row=0, column=2)
label4 = tk.Label(frame2, text="Weather")
label4.grid(row=0, column=3)

entry1 = tk.Entry(frame2, width=4)
entry1.grid(row=1, column=0, padx=8)
entry2 = tk.Entry(frame2, width=8)
entry2.grid(row=1, column=1, padx=8)
entry3 = tk.Entry(frame2, width=20)
entry3.grid(row=1, column=2, padx=8)
entry4 = tk.Entry(frame2, width=14)
entry4.grid(row=1, column=3, padx=8)

button1 = tk.Button(frame3, text="Create")
button1.grid(row=2, column=0, padx=8)
button2 = tk.Button(frame3, text="Update")
button2.grid(row=2, column=1, padx=8)
button3 = tk.Button(frame3, text="Delete")
button3.grid(row=2, column=2, padx=8)
button4 = tk.Button(frame3, text="Clear Entry Boxes", command=empty_entry)
button4.grid(row=2, column=3, padx=8)

read_table(tree_1)

main_window.mainloop()
