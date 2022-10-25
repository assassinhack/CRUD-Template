# init answer var
answer = "hacktoberfest"

# print the question, symbol '\t' is used to tab indent
print("Question : What a month-long celebration of open-source projects, their maintainers, and the entire community of contributors is called ?")
guess = input("Answer\t : ")

# check the guess
if guess == answer:
    print("Correct!")
else:
    print("Incorrect!")