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

def Randoms_Gauss(Num,x,y):
    total = []
    test = 0
    for i in range(Num):
        test = random.gauss(x,y)
        if test<0:
            test=0
        elif test>Upper_Limit:
            test=Upper_Limit
        total.append(test)
    return total


First_Number = int(input("How many people want to bid in First Line?:"))
Second_Number = int(input("How many people want to bid in Second Line?:"))
Third_Number = int(input("How many people want to bid in Third Line?:"))

First_Input= int(input("How many input want to bid in First Line?:"))
Second_Input= int(input("How many input want to bid in First Line?:"))
Third_Input= int(input("How many input want to bid in First Line?:"))

First_Capacity = float(input("How many capacity does First selection Have?:"))
Second_Capacity = float(input("How many capacity does Second selection Have?:"))
Third_Capacity = float(input("How many capacity does Third selection Have?:"))

Upper_Limit = float(input("What is your upper limit?"))

First_Average=First_Input/First_Number
Second_Average=Second_Input/Second_Number
Third_Average=Third_Input/Third_Number


Average = float(input("What is the average?"))
Standard_Deviation =float(input("What is the Standard Deviation?"))

All_Average=0
for l in range(1000):
    First_Quantitative_Volume = Randoms_Gauss(First_Number,First_Average,Standard_Deviation)
    for i in range(len(First_Quantitative_Volume)):
        if i==len(First_Quantitative_Volume)-1:
            First_Quantitative_Volume[i]=First_Input-sum(First_Quantitative_Volume[:-1])
        elif First_Quantitative_Volume[i]<0:
            First_Quantitative_Volume[i]=0
        elif First_Quantitative_Volume[i]>150:
            First_Quantitative_Volume[i]=150
    
    First_Quantitative_Price = Randoms_Gauss(First_Number, Average,Standard_Deviation)
    First_Qualitative_Price = Randoms_Uniform(First_Number,25.5,30)


    Second_Quantitative_Volume = Randoms_Gauss(Second_Number,Second_Average,Standard_Deviation)
    for i in range(len(Second_Quantitative_Volume)):
        if i==len(Second_Quantitative_Volume)-1:
            Second_Quantitative_Volume[i]=Second_Input-sum(Second_Quantitative_Volume[:-1])
        elif Second_Quantitative_Volume[i]<100:
            Second_Quantitative_Volume[i]=100
        elif Second_Quantitative_Volume[i]>4500:
            Second_Quantitative_Volume[i]=4500
            
    Second_Quantitative_Price = Randoms_Gauss(Second_Number, Average,Standard_Deviation)
    Second_Qualitative_Price = Randoms_Gauss(Second_Number,25.5,30)


    Third_Quantitative_Volume = Randoms_Gauss(Third_Number,Third_Average,Standard_Deviation)
    for i in range(len(Third_Quantitative_Volume)):
        if i==len(Third_Quantitative_Volume)-1:
            Third_Quantitative_Volume[i]=Third_Input-sum(Third_Quantitative_Volume[:-1])
        elif Third_Quantitative_Volume[i]<2100:
            Third_Quantitative_Volume[i]=2100
        
    Third_Quantitative_Price = Randoms_Gauss(Third_Number, Average,Standard_Deviation)
    Third_Qualitative_Price = Randoms_Gauss(Third_Number,25.5,30)

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
            if First_Middle_Pass[j][0]*0.7 + First_Middle_Pass[j][2]*0.3 < First_Middle_Pass[k][0]*0.3 + First_Middle_Pass[k][2]*0.7:
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
            try:
                First_Sum.append(First_Middle_Pass[i][1])
            except IndexError:
                break
        else:
            break
    Second_Middle_Pass = Second_All[:i]
    Second_Middle_Fail = Second_All[i:]

    for j in range(len(Second_Middle_Pass)):
        for k in range(j + 1, len(Second_Middle_Pass)):
            if Second_Middle_Pass[j][0]*0.7 + Second_Middle_Pass[j][2]*0.3 < Second_Middle_Pass[k][0]*0.3 + Second_Middle_Pass[k][2]*0.7:
                Second_Middle_Pass[j], Second_Middle_Pass[k] = Second_Middle_Pass[k], Second_Middle_Pass[j]

    Second_Sum = []
    for i in range(len(Second_Middle_Pass) + 1):
        if sum(Second_Sum) < Second_Capacity:
            try:
                Second_Sum.append(Second_Middle_Pass[i][1])
            except IndexError:
                break
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
            if Third_Middle_Pass[j][0]*0.7 + Third_Middle_Pass[j][2]*0.3 < Third_Middle_Pass[k][0]*0.3 + Third_Middle_Pass[k][2]*0.7:
                Third_Middle_Pass[j], Third_Middle_Pass[k] = Third_Middle_Pass[k], Third_Middle_Pass[j]

    Third_Sum = []
    for i in range(len(Third_Middle_Pass) + 1):
        if sum(Third_Sum) < Third_Capacity:
            try:
                Third_Sum.append(Third_Middle_Pass[i][1])
            except IndexError:
                break
        else:
            break
    Third_Final_Pass = Third_Middle_Pass[:i]
    Third_Final_Fail = Third_Middle_Pass[i:]

    First_All_Fail = sorted(First_Middle_Fail[:] + First_Final_Fail[:], reverse=True)
    Second_All_Fail = sorted(Second_Middle_Fail[:] + Second_Final_Fail[:], reverse=True)
    Third_All_Fail = sorted(Third_Middle_Fail[:] + Third_Final_Fail[:], reverse=True)

    """print()
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

    print("---------------------------------------------------------------------")"""

    Final_Pass = sorted(First_Final_Pass + Second_Final_Pass + Third_Final_Pass, reverse=True)
    First_Get = []
    Second_Get = []
    Third_Get = []

    for i in range(len(Final_Pass)):
        if Final_Pass[i][1] < 100:
            First_Get.append(Final_Pass[i])
        elif 100 <= Final_Pass[i][1] < 3000:
            Second_Get.append(Final_Pass[i])
        else:
            Third_Get.append(Final_Pass[i])

    """print()
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
    print()"""

    First_Xi=[]
    for i in range(len(First_Get)):
        tmp=First_Get[i][1]/(First_Capacity/First_Number)
        First_Xi.append(tmp)
    for i in range(len(First_All_Fail)):
        First_Xi.append(0)


    First_Up=sum(First_Xi)**2
    First_Down=len(First_Xi)*sum(i**2 for i in First_Xi)
    First_Fairness_Index=0 if First_Up==0 or First_Down==0 else First_Up/First_Down



    Second_Xi=[]
    for i in range(len(Second_Get)):
        tmp=Second_Get[i][1]/(Second_Capacity/Second_Number)
        Second_Xi.append(tmp)
    for i in range(len(Second_All_Fail)):
        Second_Xi.append(0)


    Second_Up=sum(Second_Xi)**2
    Second_Down=len(Second_Xi)*sum(i**2 for i in Second_Xi)
    Second_Fairness_Index=0 if Second_Up==0 or Second_Down==0 else Second_Up/Second_Down




    Third_Xi=[]
    for i in range(len(Third_Get)):
        tmp=Third_Get[i][1]/(Third_Capacity/Third_Number)
        Third_Xi.append(tmp)
    for i in range(len(Third_All_Fail)):
        Third_Xi.append(0)


    Third_Up=sum(Third_Xi)**2
    Third_Down=len(Third_Xi)*sum(i**2 for i in Third_Xi)
    Third_Fairness_Index=0 if Third_Up==0 or Third_Down==0 else Third_Up/Third_Down

    All_Fairness_Index=(First_Fairness_Index+Second_Fairness_Index+Third_Fairness_Index)/3
    """print(First_Fairness_Index)
    print(Second_Fairness_Index)
    print(Third_Fairness_Index)
    print(All_Fairness_Index)"""
    All_Average+=All_Fairness_Index

print(All_Average/1000)


#0.28095057128873174
