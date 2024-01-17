#Slang accronyms: LMK(Let me know), TMP(Tell me please), AMA(Ask me anything), ABT(About) 

#Homoglyphs: A-/-\, B-(3, C-<, D-|}, E-[-, F-/=, G-gee, H-|~|, I-!, J-_], K-|<, L-7, M-/V\, N-/V, O-0, P-9, Q-0_, R-/2, S-5, T-~|~, U-L|, V-\/, W-dubya, X-><, Y-j, Z-7_

def caps(no_puncs):
    #list of lower case alphabets
    lower_c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #new list to transfer upper case alphabets
    upper_c = []
    #iterating old list to turn lower case to upper case
    for c in no_puncs:
        #if alphabet is already upper case
        if c not in lower_c:
            upper_c.append(c)
        else:
            #if alphabet is lower case; using ord() and chr() to convert to upper
            if c in lower_c:
                c = ord(c) - 32
                new_c = chr(c)
                upper_c.append(new_c)

    return (upper_c)

def acro(upper_c):
    #list of acronym phrases 
    word = ['L', 'E', 'T', ' ', 'M', 'E', ' ', 'K', 'N', 'O', 'W', ' ', 'T', 'E', 'L', 'L', ' ', 'M', 'E', ' ', 'P', 'L', 'E', 'A', 'S', 'E', ' ', 'A', 'S', 'K', ' ', 'M', 'E', ' ', 'A', 'N', 'Y', 'T', 'H', 'I', 'N', 'G', ' ', 'A', 'B', 'O', 'U', 'T']
    #new list to store string with acronyms 
    nym_nated = []
    n = -1
    #iterating old list to covert phrases into acronyms
    for a in upper_c:
        n += 1
        #if old list = first phrase in word[]
        if upper_c[n:n+11] == word[:11]:
            nym_nated.append('L')
            nym_nated.append('M')
            nym_nated.append('K')
            #space after the acronym
            if n < (len(upper_c) - 1):
                nym_nated.append(' ')
            #iterating to remove phrase that's equal to the acronym above^^ from old list
            for i in range(11):
                upper_c.pop(n)
        else:
            #if old list = second phrase in word[]
            if upper_c[n:n+14] == word[12:26]:
                nym_nated.append('T')
                nym_nated.append('M')
                nym_nated.append('P')
                #space after the acronym
                if n < (len(upper_c) - 1):
                    nym_nated.append(' ')
                #iterating to remove phrase that's equal to the acronym above^^ from old list
                for i in range(14):
                    upper_c.pop(n)
            else:
                #if old list = third phrase in word[]       
                if upper_c[n:n+15] == word[27:42]:
                    nym_nated.append('A')
                    nym_nated.append('M')
                    nym_nated.append('A')
                    #space after the acronym
                    if n < (len(upper_c) - 1):
                        nym_nated.append(' ')
                    #iterating to remove phrase that's equal to the acronym above^^ from old list
                    for i in range(15):
                        upper_c.pop(n)
                else:
                    #if old list = fourth phrase is word[]
                    if upper_c[n:n+5] == word[43:48]:
                        nym_nated.append('A')
                        nym_nated.append('B')
                        nym_nated.append('T')
                        #space after the acronym
                        if n < (len(upper_c) - 1):
                            nym_nated.append(' ')
                        #iterating to remove phrase that's equal to the acronym above^^ from old list
                        for i in range(5):
                            upper_c.pop(n)
                    else:
                        nym_nated.append(a)
                                               
    return (nym_nated)
    
    
def homos(nym_nated):
    #list of homoglyphs of all the alphbets
             #A  B   C    D    E    F   G   H   I    J     K     L    M     N   O  P   Q     R    S    T     U     V     W     X     Y   Z
    glyph = [ 4, 8, '<', 'I>', 3, '/=', 6, '#', 1, '._|', '|<', '|_', 11, '/V', 0, 9, '0_', '/2', 5, '~|~', 'L|', '\/', 'VV', '><', 'j', 7]
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 , 21, 22, 23, 24, 25]
    n = -1
    equil = 65
    
    #iterating old list to convert alphabets into homoglyphs
    for h in nym_nated:
        n += 1
        #equation to make char = the index of glyph[] according to the alphabets
        char = ord(h) - equil
        #condition for not going out of index
        if char >= 0 and char < 26:
            #if char = the index of num[], then convert the alphabet into the homoglyph in glyph[]
            if char == num[char]:
                nym_nated.pop(n)
                nym_nated.insert(n, glyph[char])
    #iterating new list to convert into a string since ''.join(list[]) is not working due to the special characters != string  
    for i in nym_nated:
        if i == (' '):
            print('', i, end='')
        print(i, end='')

                    
def main():
    print("")
    #user input converted into str and then a list
    ask = list(str(input("Type any sentence you like: ")))
    #list of special characters or punctuations
    puncs = ["." , "," , "?" , "(" , ")" , "[" , "]" , "{" , "}" , "<" , ">" , "!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "-" , "_" , "~" , "`" , ":" , ";" , "+" , "="]
    #making this list global because it is needed to print the acro() function outside of main() since it can't be returned as a string
    global no_puncs
    no_puncs = []
    #iterating user input list[] to only put characters into new list
    for p in ask:
        #if "p" is not a punctuation, then add it to the new list[]
        if not p in puncs:
            no_puncs.append(p)
    
    print("")
    return ''.join(no_puncs), ''.join(caps(no_puncs)), ''.join(acro(caps(no_puncs))) 
    
print("")
print(main())
print("")
print("")
homos(acro(caps(no_puncs))) 
print("")
print("")
