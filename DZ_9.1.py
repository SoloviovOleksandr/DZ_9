class Car:
    def __init__(self, marka, color, v):
      self.marka = marka
      self.color = color
      self.v = v

    def ixatuvpered(self):
        return "ixatu vpered"
    def ixatunazad(self):
        return "ixatu nazad"
class Turn(Car):
    def __init__(self):
        Car.__init__(self)
    def ixatuleft(self):
        return "ixatu v livo"
    def ixaturight(self):
        return "ixatu v pravo"







