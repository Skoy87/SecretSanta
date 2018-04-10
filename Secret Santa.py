import random
from random import randrange
from random import shuffle


def startq():
    total=input('Quante persone partecipano al Secret Santa?\n')
    while total is not int:
        try:
            total=int(total)
            break
        except ValueError:
            total=input('oh, come ooon! Devi inserire un numero intero: ')
    return total

total=int(startq())

list1=[]

presents=list(range(total))
#print (presents)

def propershuffle():
    done=False
    while not done:
        shuffle(presents)
        intcount=0
        for i, item in enumerate(presents):
            #print (i, item)
            if i != item:
                intcount=intcount+1
                #print (intcount)
                if intcount == total:
                    done=True
            else:
                shuffle(presents)
    return done
        
done=propershuffle()
#print (done)



def poplist1():
    count=0
    while count < (total):
        newuser= input('Inserisci il tuo nome: ')
        list1.append(newuser)
        count=count+1
        #print (list1)
        print ('\nSono stati inseriti '+ str(count)+' nomi su un totale di ' + str(total))
    else:
        print (list1)
#poplist1()

def extract():
    for i in list1:
        print ('\n'+str(list1.pop(0)) + ' riceve il regalo numero ' + str(presents.pop(0)+1))
        list1.append('token')
        presents.append('tokenP')
        enter=input('Premi invio per continuare')
       #print (presents)
       #print (list1)
#extract()

if done == True:
    poplist1()
    extract()





