print("===== Smart Shopping Assistant =====")
name=input("Enter your name:")
amount=int(input("Enter the shopping amount:"))
print("===== Bill Summary =====")
print("name:",name)
if (amount>=1000) :
    print("discount=%10")
    discount=amount/10
    print(f"discount amount:{discount}")
    print("final amount = ",amount-discount)
elif amount>=500 & amount<=1000 :
    print("discount=%5")
    discount=amount/5
    print(f"discount amount:{discount}")
    print("final amount = ",amount-discount)
else :
    print("discount=0%")
    print("final amount = ",amount)
print("thank you ")