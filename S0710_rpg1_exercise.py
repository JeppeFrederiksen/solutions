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
        self.current_attackpower = attackpower
        self.max_attackpower = attackpower
        self.debuffed = False

    def __repr__(self):
        return f'Name: {self.name}, Health: {self._current_health}, Attackpower: {self.current_attackpower}{self.check_debuff()}, Status: {self.status()}'

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
            print(f"{other.name} is dead and cannot be hit.\n")

    def get_hit(self, other):
        random1 = random.randint(1, 20)
        self._current_health -= other.current_attackpower + random1
        if self._current_health < 0:
            self._current_health = 0
        print(f'{other.name} hits {self.name} for {other.current_attackpower + random1} damage\n')

    def get_healed(self, other):
        self._current_health += other.healpower
        if self._current_health > self.max_health:
            self._current_health = self.max_health

    def get_reveived(self):
        self._current_health = self.max_health

    def check_debuff(self):
        if self.debuffed:
            return '(Debuffed)'
        else:
            return ''


class Hero(Character):

    def __init__(self, name, health, attackpower):
        super().__init__(name, health, attackpower)
        self.shield_status = False

    def __repr__(self):
        return f'Name: {self.name}, Class: Hero, Health: {self._current_health}, Attackpower: {self.current_attackpower}, Shield: {self.get_shield_status()}, Status: {self.status()}'

    def swordswing(self, other):
        if self.shield_status:
            print(f'{self.name} has their shield up and cannot attack.\n')
        else:
            print(f'{self.name} swings their sword at {other.name}.\n')
            self.hit(other)

    def shield(self):
        if self.shield_status:
            print(f'{self.name} puts down their shield.\n')
            self.shield_status = False
        else:
            print(f'{self.name} puts up their shield\n')
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
            print(f"{other.name} tries to hit {self.name}, but their attack is blocked by {self.name}'s shield.\n")
        else:
            self._current_health -= other.current_attackpower + random1
            print(f'{other.name} hits {self.name} for {other.current_attackpower + random1} damage\n')


class Crusader(Character):

    def __init__(self, name, health, attackpower, armor_durability, armor_protection):
        super().__init__(name, health, attackpower)
        self.armor_durability = armor_durability
        self.armor_protection = armor_protection

    def __repr__(self):
        return f'Name: {self.name}, Class: Crusader, Health: {self._current_health}, Attackpower: {self.current_attackpower}, Armor durability: {self.armor_durability}, Armor protection: {self.armor_protection}, Status: {self.status()}'

    def armor_broken(self):
        if self.armor_durability <= 0:
            return True
        else:
            return False

    def get_hit(self, other):
        random1 = random.randint(1, 20)
        attack_dmg = (other.current_attackpower + random1) - self.armor_protection
        if attack_dmg < 0:
            attack_dmg = 0
        if self.armor_broken():
            self._current_health -= other.current_attackpower + random1
            print(f'{other.name} hits {self.name} for {other.current_attackpower + random1} damage\n')
        else:
            self._current_health -= attack_dmg
            self.armor_durability -= other.current_attackpower
            if self.armor_durability < 0:
                self.armor_durability = 0
            print(f'{other.name} hits {self.name} for {attack_dmg} damage because of their armor.\n')

    def greatsword_swing(self, other):
        print(f"{self.name} swings their greatsword at {other.name}.\n")
        self.hit(other)

    def heavy_hit(self, other):
        self.current_attackpower += (self.current_attackpower * 2)
        self.hit(other)
        self.current_attackpower = self.max_attackpower

    def heavy_swing(self, other):
        if not self.armor_broken():
            print(f"{self.name} swings their greasword with a lot of force at {other.name}, breaking their armor slightly in the process.\n")
            self.heavy_hit(other)
            self.armor_durability -= 10
            if self.armor_durability < 0:
                self.armor_durability = 0
        else:
            print(f"{self.name} swings their greasword with a lot of force at {other.name}.\n")
            self.heavy_hit(other)

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
            print(f'{self.name} recovers some mana.\n')
        else:
            print(f'{self.name} tries to recover some mana, but it is already full.\n')


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
            print(f'\n{self.name} heals {other.name}\n')
        else:
            print(f"{other.name} is dead and cannot be healed.\n")

    def revive(self, other):
        if other.alive():
            print(f"{other.name} is still alive and cannot be revived.\n")
        else:
            other.get_reveived()
            self._current_mana -= self.revive_mana
            print(f'{self.name} revives {other.name}.\n')


class Mage(Spellcaster):

    def __init__(self, name, health, attackpower, mana):
        super().__init__(name, health, attackpower, mana)
        self.fireballs_mana = 10
        self.debuff_mana = 15

    def __repr__(self):
        return f'Name: {self.name}, Class: Mage, Health: {self._current_health}, Attackpower: {self.current_attackpower}, Mana: {self._current_mana}, Status: {self.status()}'

    def fireballs(self, other1, other2, other3):
        self._current_mana -= self.fireballs_mana
        print(f'{self.name} casts Fireballs on {other1.name}, {other2.name} and {other3.name}.\n')
        self.hit(other1)
        self.hit(other2)
        self.hit(other3)

    def debuff(self, other):
        if other.debuffed:
            print(f"\n{other.name} is already debuffed.\n")
        else:
            self._current_mana -= self.debuff_mana
            print(f'\n{self.name} casts Debuff on {other.name}\n')
            other.current_attackpower -= int(self.current_attackpower / 2)
            other.debuffed = True


class Dragon(Character):

    def __repr__(self):
        return f'{self.name}, Health: {self._current_health}, Attackpower: {self.current_attackpower}, Status: {self.status()}\n'

    def swing(self, other):
        print(f"\n{self.name} swings it's claws at {other.name}\n")
        self.hit(other)

    def fire_breath(self, other1, other2, other3):
        print(f"\n{self.name} spews fire from it's mouth.\n")
        self.hit(other1)
        self.hit(other2)
        self.hit(other3)

    def roar(self):
        if self.debuffed:
            print(f'\n{self.name} roars loudly, removing all debuffs.\n')
            self.current_attackpower = self.max_attackpower
            self.debuffed = False
        else:
            print(f'\n{self.name} roars loudly but nothing happened.\n')

    def rndmove(self):
        random2 = random.randint(1, 10)
        if 1 <= random2 <= 5:
            return self.fire_breath(random.choice(charlist), random.choice(charlist), random.choice(charlist))
        elif 6 <= random2 <= 9:
            return self.swing(random.choice(charlist))
        else:
            return self.roar()


def start_game(p1, p2, p3, p4):
    print("a deadly dragon stands in your party's way")
    print(f"your party consist of {p1.name}, {p2.name}, {p3.name} and {p4.name}.\n")


def gameover():
    if char1.alive() is False and char2.alive() is False and char3.alive() is False and char4.alive() is False:
        print("\nEveryone died. GAME OVER")
        return True
    elif enemy1.alive() is False:
        print("\nYou killed the Dragon. YOU WIN!")
        return True
    elif char1.alive() or char2.alive() or char3.alive() or char4.alive():
        return False


def hero_turn(hero):
    if hero.alive():
        hmovelist = ['1 swing sword', '2 shield']
        print(f"\n{hero.name}'s moves: {hmovelist}")
        inp = input(f"What does {hero.name} do?\n")
        if inp in hmovelist[0]:
            return hero.swordswing(enemy1)
        elif inp in hmovelist[1]:
            return hero.shield()
        else:
            return ''
    else:
        print(f"{hero.name} is dead\n")


def crusader_turn(crusader):
    if crusader.alive():
        cmovelist = ['1 swing greatsword', '2 Heavy swing']
        print(f"\n{crusader.name}'s moves: {cmovelist}")
        inp = input(f"What does {crusader.name} do?\n")
        if inp in cmovelist[0]:
            return crusader.greatsword_swing(enemy1)
        elif inp in cmovelist[1]:
            return crusader.heavy_swing(enemy1)
        else:
            return ''
    else:
        print(f"{crusader.name} is dead\n")


def healer_turn(healer):
    if healer.alive():
        hmovelist = ['1 hit', '2 recover mana', f'3 heal({healer.heal_mana})', f'4 revive({healer.revive_mana})']
        partylist = ['1 Kazuma', '2 Darkness', '3 Aqua', '4 Megumin']
        print(f"\n{healer.name}'s moves: {hmovelist}")
        inp1 = input(f"What does {healer.name} do?\n")
        if inp1 in hmovelist[0]:
            return healer.hit(enemy1)
        elif inp1 in hmovelist[1]:
            return healer.recover_mana()
        elif inp1 in hmovelist[2]:
            healinp = input(f"who does {healer.name} cast heal on? {partylist}\n")
            if healinp in partylist[0]:
                return healer.heal(char1)
            elif healinp in partylist[1]:
                return healer.heal(char2)
            elif healinp in partylist[2]:
                return healer.heal(char3)
            elif healinp in partylist[3]:
                return healer.heal(char4)
        elif inp1 in hmovelist[3]:
            revinp = input(f"Who does {healer.name} cast revive on? {partylist}\n")
            if revinp in partylist[0]:
                return healer.revive(char1)
            elif revinp in partylist[1]:
                return healer.revive(char2)
            elif revinp in partylist[2]:
                return healer.revive(char3)
            elif revinp in partylist[3]:
                return healer.revive(char4)
        else:
            return ''
    else:
        print(f"{healer.name} is dead\n")

def mageturn(mage):
    if mage.alive():
        mmovelist = [f'1 fireballs({mage.fireballs_mana})', f'2 debuff({mage.debuff_mana})', '3 recover mana']
        print(f"\n{mage.name}'s moves: {mmovelist}")
        inp = input(f"What does {mage.name} do?\n")
        if inp in mmovelist[0]:
            return mage.fireballs(enemy1, enemy1, enemy1)
        elif inp in mmovelist[1]:
            return mage.debuff(enemy1)
        elif inp in mmovelist[2]:
            return mage.recover_mana()
        else:
            return ''
    else:
        print(f"{mage.name} is dead\n")


char1 = Hero("Kazuma", 110, 30)
char2 = Crusader("Darkness", 140, 15, 50, 50)
char3 = Healer("Aqua", 100, 55, 50)
char4 = Mage("Megumin", 105, 40, 100)
enemy1 = Dragon("The Dragon", 1000, 50)
charlist = [char1, char2, char3, char4, ]

start_game(char1, char2, char3, char4)
for char in charlist:
    print(char)
while True:
    if gameover():
        break
    hero_turn(char1)
    print(enemy1)
    crusader_turn(char2)
    print(enemy1)
    healer_turn(char3)
    print(enemy1)
    mageturn(char4)
    print(enemy1)
    enemy1.rndmove()
    for char in charlist:
        print(char)
