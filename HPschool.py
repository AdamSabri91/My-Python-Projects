Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0 
#Question1
print("Q1) Do you like dawn or dusk ?")
print("    1)Dawn ")
print("    2)Dusk ")
answer1="Dawn"
answer2="Dusk"
answer=input("Enter your answer(write just like in the options):")
if answer==answer1 :
    Gryffindor += 1
    Ravenclaw += 1
elif answer==answer2 :
    Hufflepuff += 1
    Slytherin += 1
else :
    print("Wrong input")
#Question2
print("Q2) When I’m dead, I want people to remember me as:")
print("    1)The Good ")
print("    2)The Great ")
print("    3)The Wise ")
print("    4)The Bold ")
answer1="The Good"
answer2="The Great"
answer3="The Wise"
answer4="The Bold"
answer=input("Enter your answer(write just like in the options):")
if answer==answer1 :
    Hufflepuff += 2
elif answer==answer2 :
    Slytherin += 2
elif answer==answer3 :
    Ravenclaw += 2
elif answer==answer4 :
    Gryffindor += 2
else :
    print("Wrong input")
#Question3
print("Q3) Which kind of instrument most pleases your ear?")
print("    1)The Violin ")
print("    2)The Trumpet ")
print("    3)The Piano ")
print("    4)The Drum ")
answer1="The Violin"
answer2="The Trumpet"
answer3="The Piano"
answer4="The Drum"
answer=input("Enter your answer(write just like in the options):")
if answer==answer1 :
    Slytherin += 4 
elif answer==answer2 :
    Hufflepuff += 4
elif answer==answer3 :
    Ravenclaw += 4
elif answer==answer4 :
    Gryffindor += 4
else :
    print("Wrong input")

if Gryffindor>Ravenclaw and Gryffindor>Hufflepuff and Gryffindor>Slytherin :
    print("Your house is Gryffindor.")
elif Ravenclaw>Gryffindor and Ravenclaw>Hufflepuff and Ravenclaw>Slytherin :
    print("Your house is Ravenclaw")
elif Hufflepuff>Gryffindor and Hufflepuff>Ravenclaw and Hufflepuff>Slytherin :
    print("Your house is Hufflepuff")
else:
    print("Your house is Slytherin")