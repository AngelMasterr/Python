from collections import Counter

def commonChild(s1, s2):
    list_s1=[]; list_s2=[]
    for i, j in zip(s1, s2):
        if i in s2:# and count_s2[i]>0:
            list_s1.append(i)            
        if j in s1:# and count_s1[j]>0:
            list_s2.append(j)
    list_s1="".join(list_s1)
    list_s2="".join(list_s2)
    print(list_s1," ",list_s2)
      
    def compare(list1, list2):
        lists_s = []
        if list1 in list2: lists_s.append(list1)
        elif list2 in list1: lists_s.append(list1)
        else:
            for n in range(len(list1)):
                for i in range(1, len(list1)-n):
                    if list1[n:-i] in list2:
                        lists_s.append(list1[n:-i])
                        break
                for i in range(1, len(list2)-n):
                    if list2[n:-i] in list1:
                        lists_s.append(list2[n:-i])
                        break
        
        return(lists_s)
    
    print(compare(list_s1,list_s2))
    # HNHAN   NHAAAA
                