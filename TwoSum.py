# Get the data input
lst=[]
numbers=int(input("The number of the array: "))
try:
    for i in range(0,numbers):
        key=int(input("The number`s value: "))
        lst.append(key)
    taget=int(input("Input the taget: "))
except:
    print("入力データはエラーがあります。")

# Slove the problem: 
# 値１＋値２= taget
# 値１、値２ in list
out=[]
for index_1,member1 in enumerate(lst):
    # if member1<= taget:
       member2=taget-member1
       if member2 in lst[index_1+1:]:
           out.append(index_1)
           out.append(lst[index_1+1:].index(member2)+index_1+1)
           print(f"The result is: {out}")
           break