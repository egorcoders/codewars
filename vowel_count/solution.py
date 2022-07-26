# my solution
def get_count(sentence):
    lst = ['a', 'e', 'i', 'o', 'u']
    return len(list(i for i in sentence if i in lst))


# best solution
def get_count2(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")


def get_count3(sentence):
    return sum(c in 'aeiou' for c in sentence)
