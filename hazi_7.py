
def multip_table():
    form = "{0:>5}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}"

    print(form.format("", "1", "2", "3","4","5","6", "7", "8", "9", "10", "11", "12"))
    print(form.format(":","-----","-----","-----","-----","-----","-----","-----","-----","-----","-----","-----","-----",))
    for n in range(1, 13):
        print(form.format(str(n) + ":", n*1, n*2, n*3, n*4,n*5,n*6,n*7,n*8,n*9,n*10,n*11,n*12 ))


def palindrom(word):
    merge = word.split()
    normal = ""
    reverse = ""
    
    for w in merge:
        normal += w
    for w in normal[::-1]:
        reverse += w
    print(normal)
    print(reverse)

    

    if(normal == reverse):
        print("It is a palindrome")  
    else:
        print("It is not a palindrome")      

palindrom("redder")
multip_table()