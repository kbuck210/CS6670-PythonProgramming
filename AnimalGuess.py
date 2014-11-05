class Animal:
    allHints = ["1: I have exceptional memory",
                "2: I am the largest land-living mammal in the world",
                "3: I have ivory tusks and a trunk",
                "1: I am the biggest cat",
                "2: I come in black and white or orange and black",
                "3: I am the mascot for Frosted Flakes",
                "1: I use echo-location",
                "2: I can fly",
                "3: I see well in the dark"]
	
    def __init__(self, name):
        self.name = name
        if name.lower() == "elephant":
            i = 0
        elif name.lower() == "tiger":
            i = 3
        elif name.lower() == "bat":
            i = 6

        self.hints = (self.allHints[i+0],
                 self.allHints[i+1],
                 self.allHints[i+2])                    
            
    def guess_who_am_i(self):
        print("I will give you 3 hints, guess what animal I am")
        count = 0
        guessed = False
        while (count < 3 and guessed == False):
            print(self.hints[count])
            guess = input("Who am I?:")
            if guess.strip().lower() == self.name:
                print("You got it! I am ", self.name)
                guessed = True
            else:
                print("Nope, try again!")
            count += 1
        
        if not guessed:
            print("I'm out of hints! The answer is: ", self.name)

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()

