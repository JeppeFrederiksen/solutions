"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Character:

    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attackpower = attackpower

    def __repr__(self):
        return f'Name: {self.name}, Health: {self._current_health}, Attackpower: {self.attackpower}, Status: {self.status()}'

    def alive(self):
        if self._current_health > 0:
            return True
        else:
            return False

    def status(self):
        if self.alive():
            return "Alive"
        else:
            return "Dead"

    def hit(self, other):
        other.get_hit(self)
        print(f'{self.name} hits {other.name}')
        for char in charlist:
            print(char)

    def get_hit(self, other):
        self._current_health -= other.attackpower

    def get_healed(self, other):
        self._current_health += other.healpower
        if self._current_health > self.max_health:
            self._current_health = self.max_health

class Healer(Character):

    def __init__(self, name, health, attackpower, healpower):
        super().__init__(name, health, attackpower)
        self.healpower = healpower

    def __repr__(self):
        return f'Name: {self.name}, Health: {self._current_health}, Healpower: {self.healpower}'

    def heal(self, other):
        if not other.alive():
            print(f"{other.name} is dead and cannot be healed.")
        else:
            other.get_healed(self)
            print(f'{self.name} heals {other.name}')
            for char in charlist:
                print(char)


char1 = Character("Alex", 110, 25)
char2 = Character("Andy", 100, 10)
char3 = Healer("Bob", 50, 0, 20)
charlist = ['', char1, char2, char3, '']
for char in charlist:
    print(char)
char1.hit(char2)
char3.heal(char2)
