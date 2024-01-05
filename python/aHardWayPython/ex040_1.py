import ex040mystuff
ex040mystuff.apple()
print(ex040mystuff.tangerine)
import ex039_state_abbrev
ex039_state_abbrev.find_state("广东省")

class Mystuff(object):
    def __init__(self) :
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print("I am an apple")

thing = Mystuff()
thing.apple()
print(thing.tangerine)