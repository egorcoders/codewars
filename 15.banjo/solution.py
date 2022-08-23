# my solution
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return "{} plays banjo".format(name)
    return "{} does not play banjo".format(name)

# best solution
def are_you_playing_banjo2(name):
    return name + (
        ' plays ' if name[0].lower() == 'r'
        else ' does not play '
    ) + 'banjo'
