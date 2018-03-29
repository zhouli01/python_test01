def fun(num):
    s = 0.0
    if int(num) % 2 == 0:
        for i in range(2,int(num)+1,2):
            s+=1.0/i
    else:
        for i in range(1,int(num)+1,2):
            s+=1.0 / i
    return s
num = int(input("please input a num:\n"))
print (fun(num))