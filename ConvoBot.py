#This is a small conversation bot in Python that asks some personal questions. 

print('Hello, how are you doing today?')
print() #Used to create some space between questions throughout the code. 

print("May I ask what I can call you?")

myName= input()
print()

print('It is nice to meet you,' + myName + '!')

print()

print('The length of your name is: ') # This introduces the length variable to measure name length.
print(len(myName))

print()

print('What is your favorite color,' +  myName '?') # Asking favorite color
myColor = input()

print()

print(myColor + 'That is a nice color' + myName '.' + 'I prefer Dodger Blue myself')

print()

print('I hope you have a great day as I continue to learn some more python to expand this conversation with you' + myName + '!')


