def cheese_and_crackers(cheese_count, cracker_box_count):
    print(f"You have {cheese_count} cheeses.")
    print(f"You have {cracker_box_count} boxes of crackers.")
    print(f"Man, that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script.")
number_of_cheese = 10
number_of_crackers = 50

cheese_and_crackers(number_of_cheese, number_of_crackers)

print("We can even do math inside, too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two—variables and math:")
cheese_and_crackers(number_of_cheese + 100, number_of_crackers)