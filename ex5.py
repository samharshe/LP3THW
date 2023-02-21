name = 'Samuel Harshe'
age = 20 # not a lie
height = 70 # in inches
weight = 170 # in lbs
height_centimeters = height * 2.54
weight_kilos = weight / 2.2
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall, which is roughly {round(height_centimeters)} centimeters.")
print(f"He's {weight} pounds heavy, which is roughly {round(weight_kilos)} kilos.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky; try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")