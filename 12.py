# expreesion execution
#01
a,b=2,3
TxT="@"
print(2*TxT*3)
print("end of first program")

#92
a,b="2",3
TxT="@"
print((a+TxT)*3)
print("end of second program")

# pracice
for i in range(1,5):
    print(i*"*")
    
print("a","b","c", sep="-")




# just to work 
def calc_even_or_odd(a):
    if(a%2==0):
        print("EVEN")
    else:
        print("ODD")
    return a

x=int(input("enter a value: "))
res=calc_even_or_odd(x)
#print(res)
    