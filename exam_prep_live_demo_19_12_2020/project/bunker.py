class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @staticmethod
    def filter_or_raise(list_to_filter, type_name, exc_message):
        result = [el for el in list_to_filter if el.__class__.__name__ == type_name]
        if not result:
            raise IndexError(exc_message)
        return result

    @property
    def food(self):
        return Bunker.filter_or_raise(self.supplies, "FoodSupply", "There are no food supplies left!")

    @property
    def water(self):
        return Bunker.filter_or_raise(self.supplies, "WaterSupply", "There are no water supplies left!")
    
    @property
    def painkillers(self):
        return Bunker.filter_or_raise(self.medicine, "Painkiller", "There are no painkillers left!")

    
    @property
    def salves(self):
        return Bunker.filter_or_raise(self.medicine, "Salve", "There are no salves left!")

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        to_remove_medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        if survivor.needs_healing:
            self.medicine.remove(to_remove_medicine)
            to_remove_medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        to_remove_supply = [m for m in self.supplies if m.__class__.__name__ == sustenance_type][-1]
        if survivor.needs_sustenance:
            self.supplies.remove(to_remove_supply)
            to_remove_supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")


from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor
from project.medicine.painkiller import Painkiller
b = Bunker()
b.supplies = [WaterSupply()]

print(b.food)
