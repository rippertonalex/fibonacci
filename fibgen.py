def fibonaciGenerator(fibnum):
    start = [0,1]
    for i in range(2,fibnum+1):
        nextnum = start[-1] + start[-2]
        start.append(nextnum)
    return(start[fibnum])

def isfibonaci(num):
    i = 0
    while i <= num:
        new_num = fibonaciGenerator(i)
        i+=1
        if new_num == num:
            return True
        elif num == 3:
            return True 
    return False 

val = input("Enter which element in the fibonaci sequence you want to see:")
if val!= None:
    print("The "+ val+ "th" " element of the fibonaci sequence is " +
    str(fibonaciGenerator(int(val))))

isfib_val = input("Check wether your number is a fibonaci number:")
print(isfibonaci(int(isfib_val)))

