"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en klassemetode ved navn wag_tail for Dog.
    Denne metode udskriver i konsollen noget i stil med
    "Hunden Snoopy vifter med sin 32 cm lange hale"
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google det først.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random


class Animal:

    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f'name: {self.name}, sound: {self.sound}, height: {self.height}, weight: {self.weight}, legs: {self.legs}, gender: {self._gender()}'

    def _gender(self):
        if self.female:
            return 'female'
        else:
            return 'male'

    def make_noise(self):
        print(self.sound)


class Dog(Animal):

    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep

    def wag_tail(self):
        if self.female:
            print(f"{self.name} wags her {self.tail_length} cm long tail")
        else:
            print(f"{self.name} wags his {self.tail_length} cm long tail")


def mate(mother, father):
    puppy = Dog('puppy', 'bork', random.randint(mother.height, father.height), random.randint(mother.weight, father.weight), mother.legs, random.randint(0, 1), random.randint(mother.tail_length, father.tail_length), False)
    print()
    if mother.female == True and father.female == False:
        print(f"{mother.name} and {father.name} mate:")
        print(puppy)
        puppy.wag_tail()
        puppy.make_noise()
    else:
        print(f"{mother.name} and {father.name} cannot mate.")


dog1 = Dog("Mr. Peanutbutter", "woof", 100, 40, 4, False, 20, False)
print(dog1)
dog1.wag_tail()
dog1.make_noise()

dog2 = Dog("Pickles", "bark", 75, 28, 4, True, 9, False)
print()
print(dog2)
dog2.wag_tail()
dog2.make_noise()

mate(dog2, dog1)
