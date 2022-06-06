from pet import Pet

class Horse(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, None, tricks)

    def noise(self):
        print("nayyy!")
        return self
