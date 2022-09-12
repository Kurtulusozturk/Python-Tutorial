i=0

while(i<10):
    if i==5:
        break
    print("i:",i)
    i+=1
print("---------------------")
i=0
while(i<10):
    if i==3 or i==5:
      i+=1  
      continue
    print("i:",i)
    i+=1  
print("---------------------")
i=0
while(i<10):
    if i%2==0:  
      pass #bu sırayı geçer
    else:
        print("tek sayı:",i)
    i=1+i
    # else:
    #     print(i)
    # i+=1 
