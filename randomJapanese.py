# For a song I wrote, I decided to use the singing software UTAU.
# I hate the sound of English vocal synthesizers, however, and cannot speak Japanese.
# Because it was in line with the meaning of the song, I chose to
# randomly generate Japanese characters and use those as the lyrics.

import random
def main():
    end = 0
    while not end:
        hiragana = ['\u3042', '\u3044', '\u3046', '\u3048', '\u304a', '\u304b', '\u304c', '\u304d', '\u304e', '\u304f', '\u3050', '\u3051', '\u3052', '\u3053', '\u3054', '\u3055', '\u3056', '\u3057', '\u3058', '\u3059', '\u305a', '\u305b', '\u305c', '\u305d', '\u305e', '\u305f', '\u3060', '\u3061', '\u3062', '\u3064', '\u3065', '\u3066', '\u3067', '\u3068', '\u3069', '\u306a', '\u306b', '\u306c', '\u306d', '\u306e', '\u306f', '\u3070', '\u3071', '\u3072', '\u3073', '\u3074', '\u3075', '\u3076', '\u3077', '\u3078', '\u3079', '\u307a', '\u307b', '\u307c', '\u307d', '\u307e', '\u307f', '\u3080', '\u3081', '\u3082', '\u3084', '\u3086', '\u3088', '\u3089', '\u308a', '\u308b', '\u308c', '\u308d', '\u308f']
        invalid = ['\u3041', '\u3043', '\u3045', '\u3047', '\u3049', '\u3063', '\u3083',  '\u3085', '\u3087', '\u308e']
        invalidFlag = int(input("Want invalid notes? 0/1 "))
        if invalidFlag:
                          hiragana += invalid
        num = int(input("Enter number of notes: "))

        for i in range(num):
            print(hiragana[random.randint(0, len(hiragana) - 1)], end="")
            if random.randint(0,300)%13 == 0:
                print()
        print()
        end = int(input("Wanna go again? 1 if not"))

    

main()
