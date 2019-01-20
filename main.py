# -*- coding: utf-8 -*-
#표준편차 5단위
#예정된 곳에서 팔린 REC 비율
import openpyxl
import random
import config
import module
         

for one in range(len(config.Standard_Deviation_List)):
    Standard_Deviation = config.Standard_Deviation_List[one]
    for two in range(len(config.in_advance_List)):
        in_advance=config.in_advance_List[two]
        for three in range(10):
            First_Quantitative_Volume = module.Randoms_Price(config.DATA_OF_2017['First_Number'], config.First_Average, Standard_Deviation) #정량은 정규분포(1)
            for i in range(len(First_Quantitative_Volume)): 
                if First_Quantitative_Volume[i] < 0 or First_Quantitative_Volume[i] > 150:             #표준편차가 커도(50) 거의 범위 안에
                    First_Quantitative_Volume[i] = random.gauss(config.First_Average, Standard_Deviation)
            
            First_Quantitative_Price = module.Randoms_Uniform(config.DATA_OF_2017['First_Number'],config.DATA_OF_2017['Average']-(config.DATA_OF_2017['Upper_Limit']-config.DATA_OF_2017['Average']) ,config.DATA_OF_2017['Upper_Limit']) #가격은 앞뒤 10씩
            First_Qualitative_Price = module.Randoms_Uniform(config.DATA_OF_2017['First_Number'], 25.5, 30) #정성적인거는 랜덤으로
            
            Second_Quantitative_Volume = module.Randoms_Price(config.DATA_OF_2017['Second_Number'], config.Second_Average, Standard_Deviation) 
            for i in range(len(Second_Quantitative_Volume)): 
                if Second_Quantitative_Volume[i] < 100 or Second_Quantitative_Volume[i] > 4500:
                    Second_Quantitative_Volume[i] = random.gauss(config.Second_Average, Standard_Deviation)
            
            Second_Quantitative_Price = module.Randoms_Uniform(config.DATA_OF_2017['Second_Number'], config.DATA_OF_2017['Average']-(config.DATA_OF_2017['Upper_Limit']-config.DATA_OF_2017['Average']) ,config.DATA_OF_2017['Upper_Limit'])
            Second_Qualitative_Price = module.Randoms_Uniform(config.DATA_OF_2017['Second_Number'], 25.5, 30)
            
            Third_Quantitative_Volume = module.Randoms_Price(config.DATA_OF_2017['Third_Number'], config.Third_Average, Standard_Deviation)
            for i in range(len(Third_Quantitative_Volume)):
                if Second_Quantitative_Volume[i] < 2100:
                    Second_Quantitative_Volume[i] = random.gauss(config.Second_Average, Standard_Deviation)
                        
            Third_Quantitative_Price = module.Randoms_Uniform(config.DATA_OF_2017['Third_Number'], config.DATA_OF_2017['Average']-(config.DATA_OF_2017['Upper_Limit']-config.DATA_OF_2017['Average']) ,config.DATA_OF_2017['Upper_Limit'])
            Third_Qualitative_Price = module.Randoms_Uniform(config.DATA_OF_2017['Third_Number'], 25.5, 30)
            
            
            First_All = []
            for i in range(config.DATA_OF_2017['First_Number']):
                First_All.append([First_Quantitative_Price[i], First_Quantitative_Volume[i], First_Qualitative_Price[i]])  #정량적인 가격을 맨 앞에 세워서 sort함 ,First_Quantitative_Price가 높다 = 가격이 낮다
            First_All.sort(reverse=True)
            
            Second_All = []
            for i in range(config.DATA_OF_2017['Second_Number']):
                Second_All.append([Second_Quantitative_Price[i], Second_Quantitative_Volume[i], Second_Qualitative_Price[i]])
            Second_All.sort(reverse=True)
            
            
            Third_All = []
            for i in range(config.DATA_OF_2017['Third_Number']):
                Third_All.append([Third_Quantitative_Price[i], Third_Quantitative_Volume[i], Third_Qualitative_Price[i]])
            Third_All.sort(reverse=True) 
            
            
            Down=0 #효율성의 Down은 우선선발, 일반선발A, 일반선발B를 다 통합해서 그것들 중에 가격이 낮으거(Price가 큰거) 부터 구매해서 효율성 최대화
            Down_tmp=[]
            Down_tmp=First_All+Second_All+Third_All
            Down_tmp.sort(reverse=True,key=lambda x:x[0])
            Downs=0
            for i in range(len(Down_tmp)):
                if Downs< config.DATA_OF_2017['First_Capacity']+config.DATA_OF_2017['Second_Capacity']+config.DATA_OF_2017['Third_Capacity']: #그 용량을 넘으면 안 됨.
                    Down+=Down_tmp[i][0]*Down_tmp[i][1]
                    Downs+=Down_tmp[i][0]
                else:
                    break
            
            
            First_Middle_Sum=in_advance*sum((First_All[i][1]) for i in range(len(First_All)))   # First_Middle_Sum = 몇 %를 먼저 구할것인지.
            Second_Middle_Sum=in_advance*sum((Second_All[i][1]) for i in range(len(Second_All)))  #나중에 이 부분을 바꾸면 됨@@@@@@@@@@
            Third_Middle_Sum=in_advance*sum((Third_All[i][1]) for i in range(len(Third_All)))
                
            
            
            for i in range(len(First_All)):
                First_All[i][1]=First_All[i][1]*(1-in_advance)     #1-알파퍼센트 를 가지고 경쟁하려고 하는 준비,   First_Quantitative_Volume은 1-in_advace만 살아남음 
            
            for i in range(len(Second_All)):
                Second_All[i][1]=Second_All[i][1]*(1-in_advance)
            
            for i in range(len(Third_All)):
                Third_All[i][1]=Third_All[i][1]*(1-in_advance)
            
            
            
            First_Sum = []
            for i in range(config.DATA_OF_2017['First_Number']):
                if sum(First_Sum) <(config.DATA_OF_2017['First_Capacity']-First_Middle_Sum) * 1.3:   #1.3배 한 후 미리 산 용량은 빼기
                    try:
                        First_Sum.append(First_All[i][1])
                    except IndexError:
                        break
                else:
                    break
            First_Middle_Pass = First_All[:i+1]
            First_Middle_Fail = First_All[i+1:]
            
            for j in range(len(First_Middle_Pass)): #비교 후 다시 정렬
                for k in range(j + 1, len(First_Middle_Pass)):
                    if round((config.DATA_OF_2017['Upper_Limit']-First_Middle_Pass[j][0])/config.DATA_OF_2017['Upper_Limit']*70,2)+ First_Middle_Pass[j][2] < round((config.DATA_OF_2017['Upper_Limit']-First_Middle_Pass[k][0])/config.DATA_OF_2017['Upper_Limit']*70,2) + First_Middle_Pass[k][2]: 
                        First_Middle_Pass[j], First_Middle_Pass[k] = First_Middle_Pass[k], First_Middle_Pass[j]
                        
            
            First_Sum = [] 
            for i in range(len(First_Middle_Pass) + 1):                     #1.3배가 아닌 1배로 다시 정렬
                if sum(First_Sum) < config.DATA_OF_2017['First_Capacity']-First_Middle_Sum:
                    try:
                        First_Sum.append(First_Middle_Pass[i][1])
                    except IndexError:
                        break
                else:
                    break
            First_Final_Pass = First_Middle_Pass[:i+1]
            First_Final_Fail = First_Middle_Pass[i+1:]
            
            
            Second_All2 = Second_All + First_Middle_Fail + First_Final_Fail   #우선선발에서 실패한사람들이 모두 내려옴
            Second_All2.sort(reverse=True)  
            
            Second_Sum = []
            for i in range(len(Second_All2)):
                if sum(Second_Sum) < (config.DATA_OF_2017['Second_Capacity']-Second_Middle_Sum) * 1.3:
                    try:
                        Second_Sum.append(Second_All2[i][1])
                    except IndexError:
                        break
                else:
                    break
            Second_Middle_Pass = Second_All2[:i+1]
            Second_Middle_Fail = Second_All2[i+1:]
            
            for j in range(len(Second_Middle_Pass)):
                for k in range(j + 1, len(Second_Middle_Pass)):
                    if round((config.DATA_OF_2017['Upper_Limit']-Second_Middle_Pass[j][0])/config.DATA_OF_2017['Upper_Limit']*70,2)+ Second_Middle_Pass[j][2] < round((config.DATA_OF_2017['Upper_Limit']-Second_Middle_Pass[k][0])/config.DATA_OF_2017['Upper_Limit']*70,2) + Second_Middle_Pass[k][2]:
                        Second_Middle_Pass[j], Second_Middle_Pass[k] = Second_Middle_Pass[k], Second_Middle_Pass[j]
            
            Second_Sum = []
            for i in range(len(Second_Middle_Pass) + 1):
                if sum(Second_Sum) < config.DATA_OF_2017['Second_Capacity']-Second_Middle_Sum:
                    try:
                        Second_Sum.append(Second_Middle_Pass[i][1])
                    except IndexError:
                        break
                else:
                    break
            Second_Final_Pass = Second_Middle_Pass[:i+1]
            Second_Final_Fail = Second_Middle_Pass[i+1:]
            
            Third_All2 = Third_All + Second_Middle_Fail + Second_Final_Fail
            Third_All2.sort(reverse=True)
            
            Third_Sum = []
            for i in range(len(Third_All2)):
                if sum(Third_Sum) < (config.DATA_OF_2017['Third_Capacity']-Third_Middle_Sum) * 1.3:
                    try:
                        Third_Sum.append(Third_All2[i][1])
                    except IndexError:
                        break
                else:
                    break
            Third_Middle_Pass = Third_All2[:i+1]
            Third_Middle_Fail = Third_All2[i+1:]
            
            
            for j in range(len(Third_Middle_Pass)):
                for k in range(j + 1, len(Third_Middle_Pass)):
                    if round((config.DATA_OF_2017['Upper_Limit']-Third_Middle_Pass[j][0])/config.DATA_OF_2017['Upper_Limit']*70,2)+ Third_Middle_Pass[j][2] < round((config.DATA_OF_2017['Upper_Limit']-Third_Middle_Pass[k][0])/config.DATA_OF_2017['Upper_Limit']*70,2) + Third_Middle_Pass[k][2]:
                        Third_Middle_Pass[j], Third_Middle_Pass[k] = Third_Middle_Pass[k], Third_Middle_Pass[j]
            
            Third_Sum = []
            for i in range(len(Third_Middle_Pass) + 1):
                if sum(Third_Sum) < config.DATA_OF_2017['Third_Capacity']-Third_Middle_Sum:
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
            
            
            Final_Pass = sorted(First_Final_Pass + Second_Final_Pass + Third_Final_Pass, reverse=True)   #다 합치기
            First_Get = []
            Second_Get = []
            Third_Get = []
            
            for i in range(len(Final_Pass)):      #다 합친거에서 출신이 어디냐로 다시 나눔
                if Final_Pass[i] in First_All:
                    First_Get.append(Final_Pass[i])
                elif Final_Pass[i] in Second_All:
                    Second_Get.append(Final_Pass[i])
                else:
                    Third_Get.append(Final_Pass[i])
            
                    
            First_Xi=[]                          #뽑힌거는 1 안뽑힌거는 in_advance를 넣음                                                
            for i in range(len(First_Get)):
                First_Xi.append(1)
            for i in range(len(First_All)-len(First_Get)):
                First_Xi.append(in_advance)
                
                
            First_Up=sum(First_Xi)**2
            First_Down=len(First_Xi)*sum(i**2 for i in First_Xi)
            First_Fairness_Index=0 if First_Up==0 or First_Down==0 else First_Up/First_Down
                
            
            Second_Xi=[]
            for i in range(len(Second_Get)):
                Second_Xi.append(1)
            for i in range(len(Second_All)-len(Second_Get)):
                Second_Xi.append(in_advance)
            
            
            Second_Up=sum(Second_Xi)**2
            Second_Down=len(Second_Xi)*sum(i**2 for i in Second_Xi)
            Second_Fairness_Index=0 if Second_Up==0 or Second_Down==0 else Second_Up/Second_Down
            
            
            
            
            Third_Xi=[]
            for i in range(len(Third_Get)):
                Third_Xi.append(1)
            for i in range(len(Third_All)-len(Third_Get)):
                Third_Xi.append(in_advance)
            
            
            Third_Up=sum(Third_Xi)**2
            Third_Down=len(Third_Xi)*sum(i**2 for i in Third_Xi)
            Third_Fairness_Index=0 if Third_Up==0 or Third_Down==0 else Third_Up/Third_Down
            
            
            All_Fairness_Index=(First_Fairness_Index+Second_Fairness_Index+Third_Fairness_Index)/3
            config.All_Fair+=All_Fairness_Index
            Up=0
            for i in range(len(First_Final_Pass)):
                Up+=First_Final_Pass[i][0]*First_Final_Pass[i][1]
            for i in range(len(Second_Final_Pass)):
                Up+=Second_Final_Pass[i][0]*Second_Final_Pass[i][1]
            for i in range(len(Third_Final_Pass)):
                Up+=Third_Final_Pass[i][0]*Third_Final_Pass[i][1]
            Down_tmp.sort()
            SSS=Down_tmp[0][0]   
            #SSS=sum((Down_tmp[i][0]) for i in range(len(Down_tmp)))/len(Down_tmp)
            Up1 = Up +(First_Middle_Sum+Second_Middle_Sum+Third_Middle_Sum)*SSS    #이미 Up에다가 in_advance를 더함
            config.The_end+=Up1/Down
        config.ws.cell(row=2+two+(one*13),column=3).value=config.The_end/10
        config.ws.cell(row=2+two+(one*13),column=4).value=config.All_Fair/10
        config.ws.cell(row=2+two+(one*13),column=5).value=(len(First_Get)+len(Second_Get)+len(Third_Get))/(len(First_All)+len(Second_All)+len(Third_All))
        config.The_end=0
        config.All_Fair=0
config.wb.save("연습1.xlsx")
config.wb.close()