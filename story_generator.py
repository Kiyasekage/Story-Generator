def combine(p_ans):
    question = ["why","what"]
    words = p_ans.lower().split()
    if words[0] in question:
        return f"{ans}?"
    else:
        return f"{ans}."
print("Welcome to combining your input using the story generator!")
com_list = []
status = int(input("How many lines do you want to add? "))
i = 0
while i<status:
    ans = input("input : ")
    com_list.append(combine(ans))
    i+=1
com_list = " ".join(com_list)
print(com_list)
    

