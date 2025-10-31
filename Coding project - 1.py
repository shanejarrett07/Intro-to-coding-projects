print("Hello! Today you will be taking a quiz on what football position you would most likely play.")
print("The available positions are quaterback, running back, wide receiver, linebacker, conerback, and safety.")
print("Points will be given based off of your answers.")
print("Whichever psosition recieves the most points is the position that will be recommended to you.")
print("Good Luck!\n")

quaterback_points = 0
runningback_points = 0
widereceiver_points = 0
linebacker_points = 0
cornerback_points = 0
safety_points = 0

 
height = int(input("How tall are you inches? "))

if height >= 74:
    quaterback_points += 3
    widereceiver_points +=3
    safety_points += 1

elif height < 74 and height > 68:
    runningback_points += 3
    linebacker_points += 3
    cornerback_points += 1

else:
    cornerback_points += 3
    runningback_points += 1

weight = int(input("How much do you weigh? "))

if weight >= 225:
    linebacker_points += 3
    runningback_points += 2

elif weight < 220 and weight > 195:
    quaterback_points += 2
    safety_points += 2
    widereceiver_points += 2

else:
    cornerback_points += 2
    widereceiver_points += 2

offDef = input("Do you like offense or defense? ")

if offDef == "offense":
    quaterback_points += 2
    widereceiver_points += 2
    runningback_points += 2

elif offDef == "defense":
    linebacker_points += 2
    cornerback_points += 2
    safety_points += 2

physicality = input("Are you physical? yes or no. ")

if physicality == "yes":
    runningback_points += 3
    linebacker_points += 3
    safety_points += 2
    cornerback_points += 1
else:
    widereceiver_points += 2
    quaterback_points += 2

leadership = input("Do you like being in control? yes or no. ")

if leadership == "yes":
    quaterback_points += 3
    linebacker_points += 2
    safety_points += 2

else:
    runningback_points += 2
    widereceiver_points += 2
    cornerback_points += 1

best_position = "Quaterback"
highest_score = quaterback_points

if runningback_points > highest_score:
    best_position = "Running Back"
    highest_score = runningback_points

if widereceiver_points > highest_score:
    best_position = "Wide Receiver"
    highest_score = widereceiver_points

if linebacker_points > highest_score:
    best_position = "Linebacker"
    highest_score = linebacker_points

if cornerback_points > highest_score:
    best_position = "Cornerback"
    highest_score = cornerback_points

if safety_points > highest_score:
    best_position = "Safety"
    highest_score = safety_points

print("\nThat is the end! Thank you so much for taking my quiz")
print("Feel free to come back and take it again!")
print("\nYour recommended position is:", best_position)