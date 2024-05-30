def count_substring(Str, sub):
    return [Str[i:i+len(sub)] for i in range(len(Str))].count(sub)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)