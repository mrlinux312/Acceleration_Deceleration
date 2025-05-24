#Program displays acceleration and deceleration of a vehicle


print("Car Class")
print()
class Car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0 

    def get_speed(self):
        return self.speed


democar = Car("2019 Civic", "Honda", 5)

democar.accelerate()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("------------------")

democar.accelerate()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("--------------------")

democar.accelerate()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("---------------------")

democar.accelerate()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("------------------------")

democar.accelerate()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("--------------------------")

democar.brake()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("--------------------------")

democar.brake()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("--------------------------")

democar.brake()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("--------------------------")

democar.brake()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("--------------------------")

democar.brake()
print(f"{democar.year_model}, {democar.make}")
print( "\nCurrent Speed: ", democar.get_speed(),"mph")
print("--------------------------")