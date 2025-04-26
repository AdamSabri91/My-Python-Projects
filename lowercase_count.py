message = str(input("Enter a message : "))
chosen_letter =str(input("Enter a lowercase letter : "))
count = 0
for letter in message :
    if letter == chosen_letter:
        count += 1
print(chosen_letter +" is repeated "+ str(count) +" times")