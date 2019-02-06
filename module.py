# -*- coding: utf-8 -*-
import config
import random

"""def Randoms(x):
    total = []
    test = 0
    for i in range(x):
        test = random.random()
        total.append(test)
    return total"""


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
        elif test>config.DATA_OF_2017['Upper_Limit']:
            test=config.DATA_OF_2017['Upper_Limit']
        total.append(test)
    return total

def Randoms_Price(Num,x,y):
    total=[]
    test=0
    for i in range(Num):
        test=random.gauss(x,y)
        total.append(test)
    return total
             
def Quantitative_Volume(quantitative_volume,high_limit,low_limit,average,Standard_Deviation):
    for i in range(len(quantitative_volume)): 
        if quantitative_volume[i] < low_limit or quantitative_volume[i] > high_limit:             #표준편차가 커도(50) 거의 범위 안에
            quantitative_volume[i] = random.gauss(average, Standard_Deviation) 
    return quantitative_volume

def All(number,quantitative_price,quantitative_volume,qualitative_price):
    All_list = []
    for i in range(number):
        All_list.append([quantitative_price[i], quantitative_volume[i], qualitative_price[i]])  #정량적인 가격을 맨 앞에 세워서 sort함 ,First_Quantitative_Price가 높다 = 가격이 낮다
    All_list.sort(reverse=True)
    return All_list

def a_persent(All,in_advance):
    for i in range(len(All)):
        All[i][1]=All[i][1]*(1-in_advance)     #1-알파퍼센트 를 가지고 경쟁하려고 하는 준비,   First_Quantitative_Volume은 1-in_advace만 살아남음 
    return All
            
def Sum(data,middle_sum,All):
    Sum_list = [] 
    for i in range(data):
        if sum(Sum_list) <(data-middle_sum) * 1.3:   #미리 산 용량은 뺀 후 1.3배
            try:
                Sum_list.append(All[i][1]) #1.3배를 다 채울때까지 계속 추가
            except IndexError:  #실제 용량을 가지고 코드를 실행하면 에러가 안 생김
                break
        else:
            break  #1.3배를 다 채우면 for문 종료
    return Sum_list

def Change(middle_pass,upper_limit):
    for j in range(len(middle_pass)):#1.3배안에 속한 판매자 가운데서 정량적인거 70% 정성적인거 30%를 배분해서 다시 정렬
        for k in range(j + 1, len(middle_pass)):
            if round((upper_limit-middle_pass[j][0])/upper_limit*70,2)+ middle_pass[j][2] < round((upper_limit-middle_pass[k][0])/upper_limit*70,2) + middle_pass[k][2]: 
                middle_pass[j], middle_pass[k] = middle_pass[k], middle_pass[j]
    return middle_pass

def Selected(middle_pass,capacity,middle_sum):
    sum_list = [] 
    for i in range(len(middle_pass) + 1):                     #1.3배가 아닌 1배로 다시 정렬
        if sum(sum_list) < capacity-middle_sum: #정렬한 것들을 1배안에 드는 최종선정자들을 결정하는 for문
            try:
                sum_list.append(middle_pass[i][1])
            except IndexError:
                break
        else:
            break
    return sum_list

def Jain(get,all_of,in_advance):
    jain_xi=[] # 실제 측정된(y)/이상적인(z)의 비율 즉, 뽑힌거는 1 안뽑힌거는 in_advance를 넣음   in_advance만큼은 무조건 팔림                                              
    for i in range(len(get)):
        jain_xi.append(1)
    for i in range(len(all_of)-len(get)):
        jain_xi.append(in_advance)
    return jain_xi



