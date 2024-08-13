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
import random

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
        if other.alive():
            other.get_hit(self)
        else:
            print(f"{other.name} is dead and cannot be hit.")

    def get_hit(self, other):
        random1 = random.randint(1, 20)
        self._current_health -= other.attackpower + random1
        if self._current_health < 0:
            self._current_health = 0
        print(f'{other.name} hits {self.name} for {other.attackpower + random1} damage')

    def get_healed(self, other):
        self._current_health += other.healpower
        if self._current_health > self.max_health:
            self._current_health = self.max_health

    def get_reveived(self):
        self._current_health = self.max_health


class Hero(Character):

    def __init__(self, name, health, attackpower):
        super().__init__(name, health, attackpower)
        self.shield_status = False

    def __repr__(self):
        return f'Name: {self.name}, Class: Hero, Health: {self._current_health}, Attackpower: {self.attackpower}, Shield: {self.get_shield_status()}, Status: {self.status()}'

    def swordswing(self, other):
        if self.shield_status:
            print(f'{self.name} has their shield up and cannot attack.')
        else:
            print(f'{self.name} swings their sword at {other.name}.\n')
            self.hit(other)

    def shield(self):
        if self.shield_status:
            print(f'{self.name} puts down their shield.')
            self.shield_status = False
        else:
            print(f'{self.name} puts up their shield')
            self.shield_status = True

    def get_shield_status(self):
        if self.shield_status:
            return 'up'
        else:
            return 'down'

    def get_hit(self, other):
        random1 = random.randint(1, 20)
        if self._current_health < 0:
            self._current_health = 0
        if self.shield_status:
            print(f"{other.name} tries to hit {self.name}, but their attack is blocked by {self.name}'s shield.")
        else:
            self._current_health -= other.attackpower + random1
            print(f'{other.name} hits {self.name} for {other.attackpower + random1} damage')

class Crusader(Character):

    def __init__(self, name, health, attackpower, armor_durability, armor_protection):
        super().__init__(name, health, attackpower)
        self.armor_durability = armor_durability
        self.armor_protection = armor_protection

    def __repr__(self):
        return f'Name: {self.name}, Class: Crusader, Health: {self._current_health}, Attackpower: {self.attackpower}, Armor durability: {self.armor_durability}, Armor protection: {self.armor_protection}, Status: {self.status()}'

    def armor_broken(self):
        if self.armor_durability <= 0:
            return True
        else:
            return False

    def get_hit(self, other):
        random1 = random.randint(1, 20)
        attack_dmg = (other.attackpower + random1) - self.armor_protection
        if attack_dmg < 0:
            attack_dmg = 0
        if self.armor_broken():
            self._current_health -= other.attackpower + random1
            print(f'{other.name} hits {self.name} for {other.attackpower + random1} damage')
        else:
            self._current_health -= attack_dmg
            self.armor_durability -= other.attackpower
            if self.armor_durability < 0:
                self.armor_durability = 0
            print(f'{other.name} hits {self.name} for {attack_dmg} damage because of their armor.')

    def greatsword_swing(self, other):
        print(f"{self.name} swings their greatsword at {other.name}.\n")
        self.hit(other)


class Spellcaster(Character):

    def __init__(self, name, health, attackpower, mana):
        super().__init__(name, health, attackpower)
        self.max_mana = mana
        self._current_mana = mana
        self.mana_recovered = 15

    def recover_mana(self):
        if self._current_mana < self.max_mana:
            self._current_mana += self.mana_recovered
            if self._current_mana > self.max_mana:
                self._current_mana = self.max_mana
            print(f'{self.name} recovers some mana.')
        else:
            print(f'{self.name} tries to recover some mana, but it is already full.')


class Healer(Spellcaster):

    def __init__(self, name, health, healpower, mana):
        super().__init__(name, health, 0, mana)
        self.healpower = healpower
        self.heal_mana = 10
        self.revive_mana = 35

    def __repr__(self):
        return f'Name: {self.name}, Class: Healer, Health: {self._current_health}, Healpower: {self.healpower}, Mana: {self._current_mana}, Status: {self.status()}'

    def heal(self, other):
        if other.alive():
            other.get_healed(self)
            self._current_mana -= self.heal_mana
            print(f'{self.name} heals {other.name}')
        else:
            print(f"{other.name} is dead and cannot be healed.")

    def revive(self, other):
        if other.alive():
            print(f"{other.name} is still alive and cannot be revived.")
        else:
            other.get_reveived()
            self._current_mana -= self.revive_mana
            print(f'{self.name} revives {other.name}.')


class Mage(Spellcaster):

    def __init__(self, name, health, attackpower, mana):
        super().__init__(name, health, attackpower, mana)
        self.fireballs_mana = 10
        self.debuff_mana = 15

    def __repr__(self):
        return f'Name: {self.name}, Class: Mage, Health: {self._current_health}, Attackpower: {self.attackpower}, Mana: {self._current_mana}, Status: {self.status()}'

    def fireballs(self, other1, other2, other3):
        self._current_mana -= self.fireballs_mana
        print(f'{self.name} casts Fireballs on {other1.name}, {other2.name} and {other3.name}.\n')
        self.hit(other1)
        self.hit(other2)
        self.hit(other3)

    def debuff(self, other):
        self._current_mana -= self.debuff_mana
        other.attackpower -= int(other.attackpower / 2)
        print(f'{self.name} casts Debuff on {other.name}')

    def recover_mana(self):
        if self._current_mana < self.max_mana:
            self._current_mana += 15
            if self._current_mana > self.max_mana:
                self._current_mana = self.max_mana
            print(f'{self.name} recovers some mana.')
        else:
            print(f'{self.name} tries to recover some mana, but it is already full.')


class Dragon(Character):

    def swing(self, other):
        print(f"{self.name} swings it's claws at {other.name}")
        self.hit(other)

    def fire_breath(self, other1, other2, other3):
        print(f"{self.name} spews fire from it's mouth.")
        self.hit(other1)
        self.hit(other2)
        self.hit(other3)


char1 = Hero("Kazuma", 110, 30)
char2 = Crusader("Darkness", 100, 15, 50, 50)
char3 = Healer("Aqua", 50, 20, 50)
char4 = Mage("Megumin", 75, 30, 100)
enemy1 = Dragon("The Dragon", 500, 50)
charlist = ['', char1, char2, char3, char4, '']
for char in charlist:
    print(char)
char1.shield()
for char in charlist:
    print(char)
char1.swordswing(char2)
for char in charlist:
    print(char)
char2.greatsword_swing(char1)
for char in charlist:
    print(char)
char1.shield()
for char in charlist:
    print(char)
char2.greatsword_swing(char1)
for char in charlist:
    print(char)
char1.swordswing(char2)
for char in charlist:
    print(char)