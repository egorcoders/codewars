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


def are_you_playing_banjo3(s):
    return (
        f'{s} plays banjo'
        if s.lower().startswith('r')
        else f'{s} does not play banjo'
    )
