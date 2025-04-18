class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = [] # Initialize the tricks list

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 3
            self.happiness += 1
            print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")
        else:
            print(f"{self.name} is not hungry.")

    def sleep(self):
        if self.energy < 10:
            self.energy += 5
            print(f"{self.name} is sleeping. Energy: {self.energy}")
        else:
            print(f"{self.name} is fully rested.")

    def play(self):
        if self.energy >= 2 and self.happiness < 10:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
            print(f"{self.name} is playing. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired or too happy to play.")

    def get_status(self):
        print(f"Status of {self.name}: Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}")
    def show_tricks(self):
        print(f"{self.name}'s tricks:")
        for trick in self.tricks:
            print(f"- {trick}")