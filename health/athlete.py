class Athlete():
    def __init__(self, name, DOB):
        self.name = name
        self.DOB = DOB
        #print('(Initialized Member: {})'.format(self.name))

class Swimmer(Athlete): # Swimmer subclass, represents a swimmer
    def __init__(self, name, DOB, height, weight, fatherheight, motherheight):
        Athlete.__init__(self, name, DOB)
        self.height = int(height)
        self.weight = int(weight)
        self.fatherheight = fatherheight
        self.motherheight = motherheight
        print('(Initialized Swimmer: {})'.format(self.name))

class Powerlifter(Athlete): # Powerlifter subclass, represents a Power lifter
    def __init__(self, name, DOB, height, weight, fatherheight, motherheight):
        Athlete.__init__(self, name, DOB)
        self.height = height
        self.weight = weight
        self.fatherheight = fatherheight
        self.motherheight = motherheight
        print('(Initialized powerlifter: {})'.format(self.name))

