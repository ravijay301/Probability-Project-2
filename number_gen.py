class numberGen:

    def __init__(self):
        #Defines parameters of random number generator
        self.x = 1000
        self.A = 24693
        self.C = 3517
        self.K = 2**17
        self.n = 0

    #Gets the next random number in the sequence
    def getNext(self):
        self.x = (self.x * self.A + self.C) % self.K
        u = self.x/self.K
        return u

    #Gets a specified random number in the sequence at position c
    def getSpec(self, c):
        x0 = 1000
        for i in range(c):
            x0 = (x0 * self.A + self.C) % self.K
            
        u = x0/self.K
        return u

    


