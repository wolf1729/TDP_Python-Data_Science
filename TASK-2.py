def fibonacci(n):
    a = 0
    b = 1
    z = [0, 1]

    if(n<0):
        return 'invalid input'
    
    elif(n==0):
        return a

    elif(n==1):
        return b

    print(a)
    print(b)
    for i in range(0, n):
        c = a+b
        print(c)
        a = b
        b = c
        
        
fibonacci(5)

    
    


    
