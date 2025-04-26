class Tax:
    def __init__(self, name: str, rate: float, category: str, description: str = ""):
        self.name = name        
        self.rate = rate        
        self.category = category
        self.description = description

    def calculate(self, amount: float) -> float:
        return round(amount * (self.rate / 100), 2)

    def __repr__(self):
        return f"<Tax {self.name}: {self.rate}% ({self.category})>"
