import abc

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("brand: ", self.brand, ", price: ", self.price)

class Criteria:
    def __init__(self):
        self.ResultList = []

    @abc.abstractmethod
    def meetCriteria(self, cars):
        pass

class BrandCriteria(Criteria):
    def __init__(self, brand):
        super().__init__()
        self.brand = brand

    def meetCriteria(self, cars):
        for car in cars:
            if car.brand==self.brand:
                self.ResultList.append(car)
        return self.ResultList

class PriceCriteria(Criteria):
    def __init__(self, price, isHigher=True):
        super().__init__()
        self.price = price
        self.isHigher = isHigher

    def meetCriteria(self, cars):
        for car in cars:
            if car.price>=self.price if self.isHigher else car.price<=self.price:
                self.ResultList.append(car)
        return self.ResultList

cars = [Car("Audi" if i%3==0 else "Benz", i*100) for i in range(10)]

audiFilter = BrandCriteria("Benz")
lowerThan500Filter = PriceCriteria(500, False)

print("Benzs:")
for car in audiFilter.meetCriteria(cars):
    car.display()
print("Price lower than 500:")
for car in lowerThan500Filter.meetCriteria(cars):
    car.display() 