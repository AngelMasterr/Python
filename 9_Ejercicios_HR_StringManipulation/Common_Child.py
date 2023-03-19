# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters 
# from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest 
# string that can be constructed such that it is a child of both?

"""Example:
s1 = "ABQRTOCE"
s2 = "ABTCROEX"  
These strings have two children with maximum length 5, ABROE and ABTCE. They can be formed by eliminating the characters 
("Q","T","C" in s1 and "T","C","X" in s2) or ("Q","R","O" in s1 and "R","O","X" in s2)"""

from collections import Counter
def commonChild(s1, s2):
    m = len(s1)
    n = len(s2)
    # 2D Array m*n
    counter = [[0] * (n + 1) for x in range(m + 1)]
    longest = 0

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                c = counter[i][j] + 1
                counter[i + 1][j + 1] = c
                if c > longest:
                    longest = c
            else:
                counter[i + 1][j + 1] = max(counter[i + 1][j], counter[i][j + 1])
    return longest 
      
s1 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
s2 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"
print(commonChild(s1,s2))
                