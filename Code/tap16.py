"""
This is a module that created a car store, that collects and presents items from a Car Factory.
"""

class Car:
    """
    This is the superclass for the different types of cars.
    """
    def __init__(self):
        """
        This is the constructor for the Car class.

        :param self: The instance of this object.
        :type self: Car

        """
        self.type = ""
        self.model = ""
        self.wheels = 4
        self.doors = 3
        self.seets = 5

    def print_model(self):
        """
        Prints out the model of the current car. It uses self.model and self.type

        :param self: The instance of this object.
        :type self: Car

        :return: Nothing
        :rtype: None
        """
        print("This car is a {model}: {type}, Wow!".format(model=self.model,type= self.type))

    def print_space(self):
        """
        Prints how many doors and seats in the current car. It uses self.doors and self.seets.

        :param self: The instance of this object.
        :type self: Car

        :return: Nothing
        :rtype: None
        """
        print("The car has {0} doors and {1} seets".format(self.doors, self.seets))

    def __str__(self):
        """
        Prints:
        This car is a {s.model}: {s.type}, Wow!
        The car has {s.doors} doors and {s.seets} seats

        :return: Returns the custom string that shows what model it is and the capacity of the car.
        """
        return """
This car is a {s.model}: {s.type}, Wow!
The car has {s.doors} doors and {s.seets} seets""".format(s=self)


class BMW(Car):
    def __init__(self, **arg):
        """
                Creates BMW class.
                Inherits Car class.

                :param arg: Contains info about BMW car.
                :type arg: dict

                :param type: What type of car it is. It is part of arg, the key is type.
                :type type: str

                :param doors: How many doors the car has. It is part of arg, the key is doors.
                :type doors: int

                :param fuel: What type of fuel it uses. It is part of arg, the key is fuel.
                :type fuel: Fuel

        """
        Car.__init__(self)
        self.model = "BMW"
        self.type = "{} Series".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Mercedes(Car):
    def __init__(self, **arg):
        """
                Creates BMW class.
                Inherits Car class.

                :param arg: Contains info about BMW car.
                :type arg: dict

                :param type: What type of car it is. It is part of arg, the key is type.
                :type type: str

                :param doors: How many doors the car has. It is part of arg, the key is doors.
                :type doors: int

                :param fuel: What type of fuel it uses. It is part of arg, the key is fuel.
                :type fuel: Fuel

        """

        Car.__init__(self)
        self.model = "Mercedes"
        self.type = "{} Class".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Fuel:

    """
    The fuel of a car.
    """

    def __init__(self, **arg):

        """

        :param arg: Contains info about the fuel of a car.
        :type arg: dict

        :param liters: How many litres a car uses.
        :type liters: int

        :param type: What type of fuel the car uses. It is a part of arg, the key is type.
        :type type: str

        """

        self.liters = arg.get("liters")
        self.type = arg.get("type")

    def __str__(self):

        """
        Prints:
        It uses {s.liters}L of {s.type}¢.

        :return: Returns a custom string that shows how many litres of a fuel a car uses.
        """

        return """It uses {s.liters}L of {s.type}¢.""".format(s=self)


class CarFactory:
    """
    The car factory class.
    """
    def __init__(self, **kwargs):
        """
        Creates a self.car variable from kwargs.

        :param kwargs: Gathers info needed to store into self.car
        :type kwargs: dict

        :param car_type: The model of a car.
        :type type: str

        :param doors: How many doors the car has.
        :type doors: int

        :param fuel: The type of fuel it uses.
        :type fuel: Fuel
        """
        self.car = kwargs.get("type")(type=kwargs.get("car_type"),doors=kwargs.get("doors"),fuel=Fuel(liters=kwargs.get("liters"),type=kwargs.get("fuel_type")))

    def get_car(self):
        """
        Returns the self.car dictionary.
        :return: self.car
        """
        return self.car


class CarStore:
    """
    The Car Store class.
    """
    inventory = []

    def __init__(self, **kwargs):

        """
        Creates a dictionary called self._car_factory from kwargs.

        :param kwargs: Gathers info needed for the dictionary.
        :type kwargs: dict

        :param CarFactory: Uses the class CarFactory, and passes the kwargs through here. See CarFactory for the kwargs needed.
        :type CarFactory: CarFactory
        """

        self._car_factory = CarFactory(type=kwargs.get("type"), car_type=kwargs.get("car_type"),doors=kwargs.get("doors"),liters=kwargs.get("liters"),fuel_type=kwargs.get("fuel_type"))
        self.inventory.append(self._car_factory.get_car())

    def show_car(self, car=None):

        """
        Shows a car and what fuel it uses.
        If the is no car specified, it will get one from the factory.

        :param car: A car to be displayed. Default: None
        :type car: Car

        :return: Nothing
        :rtype: None
        """

        if not car:
            car = self._car_factory.get_car()

        print(car)
        print(car.fuel)

    def show_inventory(self):
        """
        Goes through the inventory, and uses the show_car function to display all cars in inventory.
        :return: Nothing
        :rtype: None
        """
        for i in self.inventory:
            self.show_car(i)

    def __str__(self):

        """

        :return: Returns a custom string for all the cars in inventory.
        """

        return "".join([str(i) for i in self.inventory])


store = CarStore(type=Mercedes, car_type= "E", doors=2, liters = 2,fuel_type = "Disel")
store2 = CarStore(type=Mercedes, car_type= "C", doors=4, liters = 2,fuel_type = "Disel")
store3 = CarStore(type=BMW, car_type="1", doors= 3, liters= 2.5, fuel_type = "Gasoline")
store.show_inventory()

print("\n","-"*100)


class Lada(Car):
    def __init__(self, **arg):
        """
                Creates BMW class.
                Inherits Car class.

                :param arg: Contains info about BMW car.
                :type arg: dict

                :param type: What type of car it is. It is part of arg, the key is type.
                :type type: str

                :param doors: How many doors the car has. It is part of arg, the key is doors.
                :type doors: int

                :param fuel: What type of fuel it uses. It is part of arg, the key is fuel.
                :type fuel: Fuel

        """

        Car.__init__(self)
        self.model = "Lada"
        self.type = "{}".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


store = CarStore(type=Lada, car_type="VAZ-2107",doors=2,liters=1.2,fuel_type="Octane Gasoline")

store.show_inventory()