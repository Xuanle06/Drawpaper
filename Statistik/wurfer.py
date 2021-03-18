import numpy as np
import random as rd

def wuerfen1():
    return rd.choice([1,2,3,4,5,6])

def wuerfen2():
    return rd.randint(1,6)

def wuerfen3():
    return rd.sample([1,2,3,4,5,6],k=1)

#python method
#python for-schiefen
#python list,dict,variable

#histogramm
import matplotlib.pyplot as plt
plt.hist([1,2,2,2,1],bins=3)#统计数据的个数，汇图
plt.grid()
plt.title('title name')
plt.xlabel('X-label name')
plt.ylabel('Y-Label name')
#plt.show()

#Münzwurfen
def muenze() -> str:
    seiten = ['K', 'Z']

    return rd.choice(seiten)

def muenze1() -> str:
    seiten = ['K', 'Z']
    return seiten[np.random.randint(0, 2)]
    
#string if 'Spieler' in 'Hallo Spieler' if 在string里面的用法，string可以理解为数组

if 'Spielers' in 'Hallo Spieler' :
    print(muenze1())


#wahrscheinlichkeit


