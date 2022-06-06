from pet import Pet

class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, None, tricks)

    def noise(self):
        print("woof!")
        return self
