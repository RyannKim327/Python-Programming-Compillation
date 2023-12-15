class CoffeeBean:
    def __init__(self, name: str, origin: str):
        self.name = name
        self.origin = origin

    def describe(self):
        return f"A {self.name} from {self.origin}"

class ArabicaCoffee(CoffeeBean):
    def __init__(self):
        super().__init__("Arabica", "United Arab Emerates")

    def acidity(self):
        return f"The {self.name} acidity is 99% with 1% alcohol"

    def describe(self):
        return f"A coffee na adik sayo"

class RobustaCoffee(CoffeeBean):
    def __init__(self):
        super().__init__("Robusta", "Robust")

    def strength(self):
        return f"{self.name} is a very strong coffee na kaya kang ipaglaban"
    
    def describe(self):
        return f"Ito ang kape na maaadik ka sa kanya"



