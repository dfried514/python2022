from pet import Pet

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, None, tricks)

    def noise(self):
        print("meow!")
        return self
