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

def explain_usage():
    print("choose your first number and then how you want to use it using the options given\n")

def show_menu():
    print("\n1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. clear")
    print("6. end \n")

def first_num():
    fnum = int(input("enter first number: "))
    return fnum

def choose_option(result):
    choice = input("choose: ")
    if choice == "1":
        num = int(input("one number: "))
        result = addition(result, num)
    elif choice == "2":
        num = int(input("one number: "))
        result = subtraction(result, num)
    elif choice == "3":
        num = int(input("one number: "))
        result = multiplication(result, num)
    elif choice == "4":
        num = int(input("one number: "))
        result = division(result, num)
    elif choice == "5":
        result = first_num()
    elif choice == "6":
        print("stopping")
        return False
    else:
        print("\ninvalid option\n")
    return True, result

def addition(num1, num2):
    answer = num1 + num2
    print(f"\nanswer: {answer}\n")
    return answer

def subtraction(num1, num2):
    answer = num1 - num2
    print(f"\nanswer: {answer}\n")
    return answer

def multiplication(num1, num2):
    answer = num1 * num2
    print(f"\nanswer: {answer}\n")
    return answer

def division(num1, num2):
    answer = num1 / num2
    print(f"\nanswer: {answer}\n")
    return answer


explain_usage()
result = first_num()
while True:
    show_menu()
    go_on, result = choose_option(result)
    if not go_on:
        break
