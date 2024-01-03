a=int(input())
b=int(input())
if a<=b:
    dem=0
    
    for i in range(b-1,a,-1):
        if i%3==0: 
            dem+=i
            print(i,end=' ')
    if dem==0:
        print('NOT FOUND')
        
        
        

            
        
    
        