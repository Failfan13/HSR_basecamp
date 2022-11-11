class Converter:
    def __init__(self, length, numeric):
        self.length = length
        self.numeric = numeric
        self.numerics = {
            'inches': self.length/25.4,
            'feet': self.length/304.8,
            'yards': self.length/914.4,
            'miles': self.length/1609344,
            'kilometers': self.length/1000000,
            'meters': self.length/1000,
            'centimeters': self.length/10,
            'millimeters': self.length,
        }

    def inches(self):
        return self.numerics[self.numeric]*25.4
    
    def feet(self):
        return self.numerics[self.numeric]*304.8

    def yards(self):
        return self.numerics[self.numeric]*914.4

    def miles(self):
        return self.numerics[self.numeric]*1609344

    def kilometers(self):
        return self.numerics[self.numeric]*1000000

    def meters(self):
        return self.numerics[self.numeric]*1000

    def centimeters(self):
        return self.numerics[self.numeric]*10

    def millimeters(self):
        return self.numerics[self.numeric]