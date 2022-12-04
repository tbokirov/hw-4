class Hero:
    def __init__(self, name, power=True):
        self.name = name
        self.power = power


class Hero_super(Hero):
    def __str__(self):
        self.name = str

    def pr(self):
        print(f'{self.name} it is super_hero')