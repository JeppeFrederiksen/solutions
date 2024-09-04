"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

main_window = tk.Tk()
main_window.title("My first GUI")

container = tk.LabelFrame(main_window, text="Container")
container.grid(row=0, column=0, padx=8, pady=5, sticky=tk.N)
frame1 = tk.Frame(container)
frame1.grid(padx=26, pady=10)
frame2 = tk.Frame(frame1)
frame2.grid(pady=5)

label = tk.Label(frame2, text="Id")
label.grid(row=0, column=0)
entry = tk.Entry(frame2, width=4)
entry.grid(row=1, column=0, pady=8)
button = tk.Button(frame1, text="Create")
button.grid(row=2, column=0, pady=5)

main_window.mainloop()