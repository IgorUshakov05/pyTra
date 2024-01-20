class SystemBlock:
    def __init__(self, motherboard, processor, power_supply):
        self.motherboard = motherboard
        self.processor = processor
        self.power_supply = power_supply

    def get_motherboard(self):
        return self.motherboard

    def set_motherboard(self, new_motherboard):
        self.motherboard = new_motherboard

    def get_processor(self):
        return self.processor

    def set_processor(self, new_processor):
        self.processor = new_processor

    def get_power_supply(self):
        return self.power_supply

    def set_power_supply(self, new_power_supply):
        self.power_supply = new_power_supply

# Создаем экземпляры класса SystemBlock
block1 = SystemBlock("ASUS", "Intel Core i7", "Corsair 750W")
block2 = SystemBlock("Gigabyte", "AMD Ryzen 5", "EVGA 600W")

# Выводим значения свойств объектов
print("Свойства системного блока 1:")
print("Материнская плата:", block1.get_motherboard())
print("Процессор:", block1.get_processor())
print("Блок питания:", block1.get_power_supply())

print("\nСвойства системного блока 2:")
print("Материнская плата:", block2.get_motherboard())
print("Процессор:", block2.get_processor())
print("Блок питания:", block2.get_power_supply())