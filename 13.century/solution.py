
# my solution
def wave(str):
    return [str[:i] + str[i].upper() + str[i + 1:] for i, v in enumerate(str) if str[:i] + str[i].upper() + str[i + 1:] != str]


# best solution
def wave2(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
