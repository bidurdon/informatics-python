
a = raw_input('Enter Hours: ')
b = raw_input('Enter Rate: ')
try:
    a=float(a)
    b=float(b)
    Pay = a*b
    Pay1 = (15*(a-40))+(40*10)
    if a <= 40:
        print('Pay: ' + str(Pay))
    
    if a>40:
        print('Pay: ' + str(Pay1))
    
except:
    print('Error, please enter numeric input!!!')

    

    

    



    
    
    
    




