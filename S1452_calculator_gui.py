""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
Send derefter denne Teams-besked til din lærer: `<filnavn> færdig`
Fortsæt derefter med den næste fil."""

import tkinter as tk


current = 0

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.configure(state="normal")
    entry3.delete(0, tk.END)
    entry3.configure(state="readonly")

def addition():
    plus = tk.Label(frame2, text="+")
    plus.grid(row=1, column=1)
    global current
    current = 1

def subtraction():
    minus = tk.Label(frame2, text="-")
    minus.grid(row=1, column=1)
    global current
    current = 2

def multiplication():
    multiply = tk.Label(frame2, text="*")
    multiply.grid(row=1, column=1)
    global current
    current = 3
def division():
    divide = tk.Label(frame2, text="/")
    divide.grid(row=1, column=1)
    global current
    current = 4

def calculate():
    if current == 1:
        entry3.configure(state="normal")
        entry3.delete(0, tk.END)
        entry3.insert(1, f"{int(entry1.get()) + int(entry2.get())}")
        entry3.configure(state="readonly")
    elif current == 2:
        entry3.configure(state="normal")
        entry3.delete(0, tk.END)
        entry3.insert(1, f"{int(entry1.get()) - int(entry2.get())}")
        entry3.configure(state="readonly")
    elif current == 3:
        entry3.configure(state="normal")
        entry3.delete(0, tk.END)
        entry3.insert(1, f"{int(entry1.get()) * int(entry2.get())}")
        entry3.configure(state="readonly")
    elif current == 4:
        entry3.configure(state="normal")
        entry3.delete(0, tk.END)
        entry3.insert(1, f"{int(entry1.get()) / int(entry2.get())}")
        entry3.configure(state="readonly")


main_window = tk.Tk()
main_window.title("calculator")


container = tk.LabelFrame(main_window, text="Calculator")
container.grid(row=0, column=0, padx=3, pady=2)
frame1 = tk.Frame(container)
frame1.grid(row=0, pady=5)
frame2 = tk.Frame(container)
frame2.grid(row=1, padx=18, pady=4)
frame3 = tk.Frame(container)
frame3.grid(row=2, padx=18, pady=15)

label1 = tk.Label(frame2, text="=")
label1.grid(row=1, column=3)

entry1 = tk.Entry(frame2, width=4)
entry1.grid(row=1, column=0, padx=8)
entry2 = tk.Entry(frame2, width=4)
entry2.grid(row=1, column=2, padx=8)
entry3 = tk.Entry(frame2, width=4, state="readonly")
entry3.grid(row=1, column=4, padx=8)

button1 = tk.Button(frame3, text="Addition", command=addition)
button1.grid(row=2, column=0, padx=8)
button2 = tk.Button(frame3, text="Subtraction", command=subtraction)
button2.grid(row=2, column=1, padx=8)
button3 = tk.Button(frame3, text="Multiplication", command=multiplication)
button3.grid(row=2, column=2, padx=8)
button4 = tk.Button(frame3, text="Division", command=division)
button4.grid(row=2, column=3, padx=8)
button5 = tk.Button(frame3, text="Clear", command=clear)
button5.grid(row=2, column=4, padx=8)
button6 = tk.Button(frame3, text="Calculate", command=calculate)
button6.grid(row=3, columnspan=5, pady=8)


main_window.mainloop()
