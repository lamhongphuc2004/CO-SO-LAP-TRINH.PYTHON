n=int(input())

kq=0
if n>=0 and n<=10000:

    while n>0:
        dem=n%10
        n//=10
        kq+=dem
    if kq%10==9:
        print('YES')
    else:
        print('NO')
        
        
        
        
    
    