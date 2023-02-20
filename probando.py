def merge_the_tools(string, k):
    
    long_s = len(string)
    sub_len = long_s // k
    
    sub_string = [string[i:i+sub_len] for i in range(0, long_s, sub_len)]
    print(sub_string)

merge_the_tools("AABCAAADA", 3)