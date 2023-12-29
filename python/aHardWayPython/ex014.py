from sys import argv

script, userName = argv
prompt = '>'
print(f"hi {userName},I am the {script} script.")
print(f"Please input sth {prompt}")
userInput = input(prompt)
print(f"That you input is \" {userInput}\" ")
