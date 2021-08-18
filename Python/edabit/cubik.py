# https://edabit.com/challenge/PLdJr4S9LoKHHjDJC


def identify( *cube):
    return "Missing {}".format(cube.count(min(cube))) if min(cube) != max(cube) else "Non-Full"if cube.count(min(cube)) != len(min(cube)) else "Full"