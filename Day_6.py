# Enter your code here. Read input from STDIN. Print output to STDOUT

num_t  = int(input())
if num_t >= 1 and num_t <= 10:
    for t in range(num_t):
        s = str(input())
        if len(s) >=2 and len(s) <= 10000:
            e_s = []
            o_s = []
            for i in range(len(s)):
                    if i %2 == 0:
                        e_s.append(s[i])
                    else:
                        o_s.append(s[i])
            even_string = ''.join(e_s)
            odd_string = ''.join(o_s)
            print(even_string, odd_string)
        else:
            s = str(input())

else:
    num_t = int(input())        


