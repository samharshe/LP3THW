# number of cars
cars = 100

# spaces per car
space_in_a_car = 4

# number of drivers
drivers = 30

# number of passengers
passengers = 90

# number of cars that remain unused due to a driver shortage 
cars_not_driven = cars - drivers

# number of cars in use
cars_driven = drivers

# number of people that can be driven given the number of cars in use and the space in each car
carpool_capacity = cars_driven * space_in_a_car

# number of people that need to fit in an average car
average_passengers_per_car = passengers / cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put", average_passengers_per_car, "in each car.")