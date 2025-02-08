def rever_sent(sentence):
    return " ".join(sentence.split()[::-1])

usr_input = input()
print(rever_sent(usr_input))