print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
perc = int(input("How much tip in Percentage would you like to give? 10, 15 or 20? "))
split = int(input("How many people to split the bill? "))
percentage = (perc) / 100 + 1
end = round(((total) / (split)) * percentage)



print(f"Each person should pay: {end} ")