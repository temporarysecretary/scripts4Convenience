# This script generates the Unicode formatted characters 
# from 3040 to 310F. However, some of these characters
# are invalid and have to be removed by hand later. 
# The output from this script can be used in other programs
# which may require a list of Hiragana characters.

import random
def main():
    for i in range(304,310):
        for j in range(0, 16):
            string = '\\u' + str(i) + str('{:x}'.format(j))
            print('\'' + string + '\'', end = ", ")
            
        
main()

