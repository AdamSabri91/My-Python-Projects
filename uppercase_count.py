message = str(input("Enter a message : "))
chosen_letter =str(input("Enter an uppercase letter : "))
count = 0
for letter in message :
    if letter == chosen_letter:
        count += 1
print("uppercase " chosen_letter +" is repeated "+ str(count) +" times in your message")
