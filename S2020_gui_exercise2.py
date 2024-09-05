""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

def empty_entry():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    print("Cleared Entry boxes")


main_window = tk.Tk()
main_window.title("my first GUI")

container = tk.LabelFrame(main_window, text="Container")
container.grid(row=0, column=0, padx=7, pady=2)
frame1 = tk.Frame(container)
frame1.grid(row=0, padx=18, pady=4)
frame2 = tk.Frame(container)
frame2.grid(row=1, padx=18, pady=15)

label1 = tk.Label(frame1, text="Id")
label1.grid(row=0, column=0, pady=9)
label2 = tk.Label(frame1, text="Weight")
label2.grid(row=0, column=1)
label3 = tk.Label(frame1, text="Destination")
label3.grid(row=0, column=2)
label4 = tk.Label(frame1, text="Weather")
label4.grid(row=0, column=3)

entry1 = tk.Entry(frame1, width=4)
entry1.grid(row=1, column=0, padx=8)
entry2 = tk.Entry(frame1, width=8)
entry2.grid(row=1, column=1, padx=8)
entry3 = tk.Entry(frame1, width=20)
entry3.grid(row=1, column=2, padx=8)
entry4 = tk.Entry(frame1, width=14)
entry4.grid(row=1, column=3, padx=8)

button1 = tk.Button(frame2, text="Create")
button1.grid(row=2, column=0, padx=8)
button2 = tk.Button(frame2, text="Update")
button2.grid(row=2, column=1, padx=8)
button3 = tk.Button(frame2, text="Delete")
button3.grid(row=2, column=2, padx=8)
button4 = tk.Button(frame2, text="Clear Entry Boxes", command=empty_entry)
button4.grid(row=2, column=3, padx=8)

main_window.mainloop()
