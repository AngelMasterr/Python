def substrCount(n, s):
    cont = 0
    a = 0
    for i in s[:-1]:
        string1 = i
        a += 1
        for j in s[a:]:
            string1 += j            
            leng = len(string1)
            string2 = s[a-1: a+2*leng-2]
            char = string1[leng//2]
            if len(set(string1)) == 1:
                cont += 1                
            elif len(set(string2)) == 2 and string1.count(char) == 1 and string1 != string2:
                cont += 1
                break
            elif len(set(string2))>2: break
    return(cont+n)
                
s = "abcbaba"
n = len(s)              
print(substrCount(n, s))