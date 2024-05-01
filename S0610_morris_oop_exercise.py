"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner:

    def __init__(self, turn, sleepiness, thirst, hunger, whisky, gold):
        self.turn = turn
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whisky = whisky
        self.gold = gold

    def __repr__(self):
        return f"Turn: {self.turn}, Sleepiness: {self.sleepiness}, Thirst: {self.thirst}, Hunger: {self.hunger}, Whisky: {self.whisky}, Gold: {self.gold}"

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1

    def dead(self):
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100


morris = Miner(0, 0, 0, 0, 0, 0)

while not morris.dead() and morris.turn < 1000:
    morris.turn += 1
    if morris.sleepiness > 95:
        morris.sleep()
    elif morris.whisky == 0 and morris.gold > 0 and morris.whisky < 10:
        morris.buy_whisky()
    elif morris.thirst > 90 and morris.whisky > 0:
        morris.drink()
    elif morris.hunger > 90 and morris.gold > 1:
        morris.eat()
    else:
        morris.mine()
    print(morris)
