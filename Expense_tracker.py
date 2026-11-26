print("===== Expense Tracker =====")
name=input("enter your name :")
print("1.Add expense")
print("2.Edit expense")
print("3.View expense")
print("4.exit")
choice=int(input("enter choice:"))
discreption=[]
amount=[0]
count=0
edit=0
while (choice != 4):
    if (choice==1) :
        count+=1
        discreption.append(input("enter the discription:"))
        amount.append(int(input("enter the expense amount:")))
        print("expense successfully added")
    elif (choice==2) :
        discreptionnum=input("enter the discreption of expense:")
        index1=discreption.index(discreptionnum)
        edit=int(input("enter the amount to edit:"))
        amount[index1]=edit
        print(f"the amount {edit} is added successfully")
        edit1=+1
    elif (choice==3) :
        total=sum(amount)
        print("total expense till now is: ",total)
        print("number of entries :",count)
        print("number of edits :",edit1)
    elif (choice==4) :
        break
    else :
        break
    choice=int(input("enter choice:"))
print("thank you")