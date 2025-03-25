# This was a script I wrote to get a binary expansion of Euler's number,
# which was a homework assignment or something. I think I may have gotten it
# wrong... so I'll have to fix it again someday.

def main():
    e = 2.7182818284590452353602874713527/2 - 1
    out = ""
    outNum = 1
    
    for i in range(23):
        if e > 1:
            e = e - 1
            print(str(i) + ": 1")
            out += "1"
            outNum += (1/(2**(i)))
        else:
            print(str(i) + ": 0")
            out += "0"
            
        e = e * 2

    print(str(out))
    print(outNum * 2)
    
main()
