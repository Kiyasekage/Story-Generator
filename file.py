def combine(p_ans):
    lists = []
    question = ["why","what"]
    words = p_ans.lower().split()
    if words[0] and words in question:
        lists.append(f"{ans}?")
    else:
        lists.append(f"{ans}.")
    return lists
print("Welcome to combining your input using the story generator!")
com_list = []
status = int(input("How many lines do you want to add? "))
i = 0
while i<status:
    ans = input("input : ")
    com_list.append(combine(ans))
    i+=1

    

