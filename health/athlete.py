class athlete():
    def __init__(self, name, DOB):
        self.name = name
        self.DOB = DOB
        print('(Initialized Member: {})'.format(self.name))

class swimmer(athlete): # Swimmer subclass, represents a swimmer
    def __init__(self, name, DOB, height, weight, fatherheight, motherheight):
        athlete.__init__(self, name, DOB)
        self.height = int(height)
        self.weight = int(weight)
        print('(Initialized Swimmer: {})'.format(self.name))

    def display(self):
        athlete.display(self)
        print('Height: "{:d}"'.format(self.height))
        print('Weight: "{:d}"'.format(self.weight))

class powerlifter(athlete):
    def __init__(self, name, DOB, height, weight, fatherheight, motherheight):
        athlete.__init__(self, name, DOB)
        self.height = height
        self.weight = weight
        print('(Initialized powerlifter: {})'.format(self.name))
    def display(self):
        athlete.display(self)
        print('Height: "{:d}"'.format(self.height))
        print('Weight: "{:d}"'.format(self.weight))
