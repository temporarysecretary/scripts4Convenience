# This script takes a list of characters and a casting list and randomly
# assigns characters until there aren't any left to evenly distribute.
# As of right now, these characters are hard coded, but I will likely return
# to this in the future to make these more dynamic.

import random

def main():
    characters = []
    cast = []

    i = 0
    while i < 3:
        j = 0
        while j < 3:
            selectedNum = random.randrange(0,len(characters))
            name = cast[j]
            outputString = cast[j] + ": " + characters[selectedNum]
            print(outputString)
            characters.remove(characters[selectedNum])
            j += 1
        i += 1
    print("Left overs: ")
    print(characters)

main()
