import re

class SystemBlock:
    def __init__(self, motherboard, processor, power_supply):
        self.set_motherboard(motherboard)
        self.set_processor(processor)
        self.set_power_supply(power_supply)

    def get_motherboard(self):
        return self._motherboard

    def set_motherboard(self, new_motherboard):
        if 20 <= len(new_motherboard) <= 150:
            self._motherboard = new_motherboard
        else:
            raise ValueError("Наименование материнской платы должно содержать не менее 20 и не более 150 символов")

    def get_processor(self):
        return self._processor

    def set_processor(self, new_processor):
        if re.match("^[A-Za-z0-9\-.;]+$", new_processor):
            self._processor = new_processor
        else:
            raise ValueError("Название процессора может состоять из символов: буквы, цифры, тире, точка, точка с запятой")

    def get_power_supply(self):
        return self._power_supply

    def set_power_supply(self, new_power_supply):
        if re.search(r'\d+W', new_power_supply):
            self._power_supply = new_power_supply
        else:
            raise ValueError("В наименовании блока питания должно присутствовать значение напряжения, например, '500W'")

# Создаем экземпляры класса SystemBlock
try:
    block1 = SystemBlock("ASUSROGStrixZ390-EGamingawdawdawd", "awdoawdoawdoawduawdpojawdawd", "Cawdoawdoawdoawduawdpojawdawd")
    block2 = SystemBlock("GigabyteB450AORUSMddddddd", "awdoawdoawdoawduawdpojawdawd", "awdoawdoawdoawduawdpojawdawd")
except ValueError as e:
    print("Ошибка при создании системного блока:", e)
else:
    # Выводим значения свойств объектов
    print("Свойства системного блока 1:")
    print("Материнская плата:", block1.get_motherboard())
    print("Процессор:", block1.get_processor())
    print("Блок питания:", block1.get_power_supply())

    print("\nСвойства системного блока 2:")
    print("Материнская плата:", block2.get_motherboard())
    print("Процессор:", block2.get_processor())
    print("Блок питания:", block2.get_power_supply())