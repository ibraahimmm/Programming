prompt = ("\nEnter your age,")
prompt += "\n Enter quit when you are finished:"
while True:
    age = input(prompt)
    if age =='quit':
        break
    age = int(age)

    if age <= 3 :
        print("You are free to enter")
    elif age < 13:
        print("Your ticket price is 10$")
    else:
        print("Your ticket price is 15$")


