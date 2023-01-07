glossary = {
'loop' : ' a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied.' ,
'Data_structure':'A data structure allows data to be added, removed, stored and maintained in a structured manner',
'function':'A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.',
'comment': 'A note in a program that the Python interpreter ignores.',
'syntax':'Syntax refers to the rules that define the structure of a language.',
'key': 'The first item in a key-value pair in a dictionary.',
'value': 'An item associated with a key in a dictionary.',
'conditional test': 'A comparison between two values.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, meaning in glossary.items():
    print("\n" + word.title() + ": " + meaning)
 
