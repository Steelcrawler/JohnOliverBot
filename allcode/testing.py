text = "hi my name is john"
first_space = text.find(" ")
second_space = text.find(" ", first_space+1)
completion_start = second_space+1
print(text[completion_start:])