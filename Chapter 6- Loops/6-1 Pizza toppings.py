prompt = ("\nWhat topping would you like on your pizza?")
prompt += "\nEnter 'quit' when you are finished: "
#Use while loop to itterate until the user enters quit
while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break