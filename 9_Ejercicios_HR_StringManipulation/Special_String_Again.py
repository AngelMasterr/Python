def substrCount(n, s):
    cont = 0
    a = 0
    for i in s[:-1]:
        string1 = i
        a += 1
        for j in s[a:]:
            string1 += j
            leng = len(string1)
            char = string1[leng//2]
            if len(set(string1)) == 1:
                cont += 1                
            elif leng%2 == 1 and len(set(string1)) == 2 and string1.count(char) == 1:
                    cont += 1
                    break
            else:
                if len(set(string1))>2: break
    return(cont+n)
                
s = "abcbaba"
n = len(s)              
print(substrCount(n, s))