import random


def Randoms(x):
    total = []
    test = 0
    for i in range(x):
        test = random.random()
        total.append(test)
    return total


def Randoms_Uniform(x, Start, Finish):
    total = []
    test = 0
    for i in range(x):
        test = random.uniform(Start, Finish)
        total.append(test)
    return total


First_Number = int(input("How many people want to bid in First Line?:"))
Second_Number = int(input("How many people want to bid in Second Line?:"))
Third_Number = int(input("How many people want to bid in Third Line?:"))

First_Capacity = float(input("How many capacity does First selection Have?:"))
Second_Capacity = float(input("How many capacity does Second selection Have?:"))
Third_Capacity = float(input("How many capacity does Third selection Have?:"))

Upper_Limit = float(input("What is your upper limit?"))
sum1 = 0

First_Quantitative_Volume = Randoms_Uniform(First_Number, 0, 100)
First_Quantitative_Price = Randoms_Uniform(First_Number, 0, Upper_Limit)
First_Qualitative_Price = Randoms(First_Number)

Second_Quantitative_Volume = Randoms_Uniform(Second_Number, 100, 3000)
Second_Quantitative_Price = Randoms_Uniform(First_Number, 0, Upper_Limit)
Second_Qualitative_Price = Randoms(Second_Number)

Third_Quantitative_Volume = Randoms_Uniform(Third_Number, 3000, 10000)
Third_Quantitative_Price = Randoms_Uniform(First_Number, 0, Upper_Limit)
Third_Qualitative_Price = Randoms(Third_Number)

First_All = []
for i in range(First_Number):
    First_All.append([First_Quantitative_Price[i], First_Quantitative_Volume[i], First_Qualitative_Price[i]])
First_All.sort(reverse=True)

Second_All = []
for i in range(Second_Number):
    Second_All.append([Second_Quantitative_Price[i], Second_Quantitative_Volume[i], Second_Qualitative_Price[i]])
Second_All.sort(reverse=True)

Third_All = []
for i in range(Third_Number):
    Third_All.append([Third_Quantitative_Price[i], Third_Quantitative_Volume[i], Third_Qualitative_Price[i]])
Third_All.sort(reverse=True)

First_Sum = []
for i in range(First_Number):
    if sum(First_Sum) < First_Capacity * 1.3:
        First_Sum.append(First_All[i][1])
    else:
        break
First_Middle_Pass = First_All[:i]
First_Middle_Fail = First_All[i:]

for j in range(len(First_Middle_Pass)):
    for k in range(j + 1, len(First_Middle_Pass)):
        if First_Middle_Pass[j][0] + First_Middle_Pass[j][2] < First_Middle_Pass[k][0] + First_Middle_Pass[k][2]:
            First_Middle_Pass[j], First_Middle_Pass[k] = First_Middle_Pass[k], First_Middle_Pass[j]

First_Sum = []
for i in range(len(First_Middle_Pass) + 1):
    if sum(First_Sum) < First_Capacity:
        First_Sum.append(First_Middle_Pass[i][1])
    else:
        break
First_Final_Pass = First_Middle_Pass[:i]
First_Final_Fail = First_Middle_Pass[i:]

Second_All = Second_All + First_Middle_Fail + First_Final_Fail
Second_All.sort(reverse=True)

Second_Sum = []
for i in range(Second_Number):
    if sum(Second_Sum) < Second_Capacity * 1.3:
        Second_Sum.append(Second_All[i][1])
    else:
        break
Second_Middle_Pass = Second_All[:i]
Second_Middle_Fail = Second_All[i:]

for j in range(len(Second_Middle_Pass)):
    for k in range(j + 1, len(Second_Middle_Pass)):
        if Second_Middle_Pass[j][0] + Second_Middle_Pass[j][2] < Second_Middle_Pass[k][0] + Second_Middle_Pass[k][2]:
            Second_Middle_Pass[j], Second_Middle_Pass[k] = Second_Middle_Pass[k], Second_Middle_Pass[j]

Second_Sum = []
for i in range(len(Second_Middle_Pass) + 1):
    if sum(Second_Sum) < Second_Capacity:
        Second_Sum.append(Second_Middle_Pass[i][1])
    else:
        break
Second_Final_Pass = Second_Middle_Pass[:i]
Second_Final_Fail = Second_Middle_Pass[i:]

Third_All = Third_All + Second_Middle_Fail + Second_Final_Fail
Third_All.sort(reverse=True)

Third_Sum = []
for i in range(Third_Number):
    if sum(Third_Sum) < Third_Capacity * 1.3:
        Third_Sum.append(Third_All[i][1])
    else:
        break
Third_Middle_Pass = Third_All[:i]
Third_Middle_Fail = Third_All[i:]

for j in range(len(Third_Middle_Pass)):
    for k in range(j + 1, len(Third_Middle_Pass)):
        if Third_Middle_Pass[j][0] + Third_Middle_Pass[j][2] < Third_Middle_Pass[k][0] + Third_Middle_Pass[k][2]:
            Third_Middle_Pass[j], Third_Middle_Pass[k] = Third_Middle_Pass[k], Third_Middle_Pass[j]

Third_Sum = []
for i in range(len(Third_Middle_Pass) + 1):
    if sum(Third_Sum) < Third_Capacity:
        Third_Sum.append(Third_Middle_Pass[i][1])
    else:
        break
Third_Final_Pass = Third_Middle_Pass[:i]
Third_Final_Fail = Third_Middle_Pass[i:]

First_All_Fail = sorted(First_Middle_Fail[:] + First_Final_Fail[:], reverse=True)
Second_All_Fail = sorted(Second_Middle_Fail[:] + Second_Final_Fail[:], reverse=True)
Third_All_Fail = sorted(Third_Middle_Fail[:] + Third_Final_Fail[:], reverse=True)

print()
print("First Final passes : ")
print("정량적 가격           용량                정성적 가격")
for i in range(len(First_Final_Pass)):
    print(First_Final_Pass[i])
    print()
print()

print("Second Final passes : ")
print("정량적 가격           용량                정성적 가격")
for i in range(len(Second_Final_Pass)):
    print(Second_Final_Pass[i])
    print()
print()

print("Third Final passes : ")
print("정량적 가격           용량                정성적 가격")
for i in range(len(Third_Final_Pass)):
    print(Third_Final_Pass[i])
    print()
print()

print("---------------------------------------------------------------------")

Final_Pass = sorted(First_Final_Pass + Second_Final_Pass + Third_Final_Pass, reverse=True)
First_Get = []
Second_Get = []
Third_Get = []

for i in range(len(Final_Pass)):
    if Final_Pass[i][1] < 100:
        First_Get.append(Final_Pass[i])
    elif 100 < Final_Pass[i][1] < 3000:
        Second_Get.append(Final_Pass[i])
    else:
        Third_Get.append(Final_Pass[i])

print()
print("First Get : ")
print("정량적 가격           용량                정성적 가격")
for i in range(len(First_Get)):
    print(First_Get[i])
    print()
print()

print("Second Get : ")
print("정량적 가격           용량                정성적 가격")
for i in range(len(Second_Get)):
    print(Second_Get[i])
    print()
print()

print("Third Get : ")
print("정량적 가격           용량                정성적 가격")
for i in range(len(Third_Get)):
    print(Third_Get[i])
    print()
print()
