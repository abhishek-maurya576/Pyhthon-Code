def count_substring(string, sub_string):
    i,c = 0,1
    n = len(string)
    while i<n:
        sub_string in string
        c +=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)