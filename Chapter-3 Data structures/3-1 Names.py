friends = ["JJ", "latif", "aiman","saif","Tim"]#string list containing 5 names
print (friends[0])
print (friends[1])
print (friends[2])
print (friends[3])
print (friends[-1])

friends = ["JJ", "latif", "aiman","saif","Tim"]#string list containing 5 names
print ("Hi",friends[0],"How are you doing today?")
print ("Hi",friends[1],"How are you doing today?")
print ("Hi",friends[2],"How are you doing today?")
print ("Hi",friends[3],"How are you doing today?")
print ("Hi",friends[-1],"How are you doing today?")

mode=["Motorcycle","Car","Jet","Train"] #string list containing differents modes of transport
print("i would love to own a Yamaha",(mode[0]))
print("i would love to own a Mercedes",(mode[1]))
print("i would love to own a Private",(mode[2]))
print("i would love to own a Private",(mode[3]))

guest=["JuiceWRLD","Pop smoke","Joe Rogan"]
print("Hi",guest[0],",you are invited to a dinner tonight at 8 pm")
print("Hi",guest[1],",you are invited to a dinner tonight at 8 pm")
print("Hi",guest[-1],",you are invited to a dinner tonight at 8 pm")
#Adding a print statement to replace a guest
print("Hi",guest[0],",Sorry to hear that you cannot make it")
guest[0]="Adison Tesla"
print("Hi",guest[0],",you are invited to a dinner tonight at 8 pm")
print("Hi",guest[1],",you are invited to a dinner tonight at 8 pm")
print("Hi",guest[-1],",you are invited to a dinner tonight at 8 pm")
#Using pop to exlude guests from the list
print("Hi",guest[0],",Due to unforeseen circumstances it will not be possible to arrange the dinner.")
guest.pop(0)
print("Hi",guest[1],",you are invited to a dinner on friday night at 8 pm. Please arrive prior to the given time")
print("Hi",guest[-1],",you are invited to a dinner on friday night at 8 pm. Please arrive prior to the given time")
print("Guest list before deleting is:"+ str (guest))
#Using del to make the list empty and print it
del guest[0:2]
print("Guest list after deleting is:"+ str (guest))















