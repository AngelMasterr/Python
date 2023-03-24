s = "abcadeaj"

list_let=[]
for i in range(len(s)-1):
    if s[i] in s[i+1:]:
        new = s[::-1] 
        print(new)   
        ind = new.find(s[i])
        list_let.append(len(new)-2-ind-i)
print(max(list_let))
    