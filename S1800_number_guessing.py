""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random

class Numbers:

    def __init__(self, num1, num2, num3, num4, won=False):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.black_coins = 0
        self.white_coins = 0
        self.guess_count = 0
        self.won = won

    def __repr__(self):
        return f'4 numbers have been randomly generated, You have to guess what the numbers are. \nafter each guess you get some coins, A black coin means a correct number in the right position \nand a white coin means a correct number in the wrong position.\n'

    def win(self):
        if self.black_coins < 4:
            self.won = False
        else:
            print(f'You Win! \nYou won in {self.guess_count} guesses')
            self.won = True

    def guess(self):
        num_list = [self.num1, self.num2, self.num3, self.num4]
        guess = list(map(int, input(f'Your guess: ').split()))
        if len(guess) > 4:
            print('Too many numbers, there are only 4 numbers.')
        elif len(guess) < 4:
            print('Not enough numbers, there are 4 numbers')
        else:
            for i in range(4):
                if guess[i] == num_list[i]:
                    self.black_coins += 1
                elif guess[i] in num_list:
                    self.white_coins += 1
            print(f'Black coins: {self.black_coins} \nWhite coins: {self.white_coins}')
            self.guess_count += 1
            self.win()
            self.black_coins = 0
            self.white_coins = 0


game = Numbers(random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9))

print(game)
while game.won is False:
    game.guess()