sandwich_orders=['tuna sandwich','chicken sandwich','beef sandwich','salmon sandwich']
finished_sandwiches=[]


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")