def likes(names):
    ln = len(names)
    if ln == 0:
        return "no one likes this"
    elif ln == 1:
        return f"{names[0]} likes this"
    elif ln == 2:
        return f"{names[0]} and {names[1]} like this"
    elif ln == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {ln - 2} others like this"
