
import requests
html = 'https://www.celestrak.com/NORAD/elements/cubesat.txt'
name = input("Enter Name: ")
DATA = ["","","","","","","","","","","","","","","","","","",""]
#TLESIZE = [[""]*23,[""]*1,[""]*4,[""]*1,[""]*2,[""]*3,[""]*3,[""]*2,[""]*12,[""]*10,[""]*8,[""]*8,[""]*1,[""]*4,[""]*1,[""]*1,[""]*5,[""]*8,[""]*8,[""]*7,[""]*8,[""]*10,[""]*5,[""]*1]
TLESIZE = [[0,23],[26,30],31,[33,34],[35,37],[38,40],[42,43],[44,55],[57,66],[68,75],[78,84],[88,91],[101,108],[110,117],[119,125],[127,134],[136,143],[145,155],[156,160]]
def fetch(html,name):
    textTemp = ""
    temp = ""
    f= open("test.txt","w")
    response = requests.get(html)
    body2 = response.text
    f.write(body2)
    f.close() 
    f= open("test.txt","r")
    printed = False
    n = 0

    for line in f:
        if line.startswith(name):
            printed = True
        if printed and n<6:
            n = n + 1
            temp = line[:-1]
            textTemp = textTemp + temp
            print(line)
        elif n<6:
            printed = False
    f.close()
    a = 0
    
    for i in range(0,19):
        print(len(textTemp))
        print(textTemp[2:4])
        #print(i)
        if (type(TLESIZE[i]) != int) :
            #if (len(TLESIZE[i]) == 1):
            #    DATA[i] = textTemp[TLESIZE[i][0]]+textTemp[TLESIZE[i][0]+1]
            #else:
            #if (TLESIZE[i][1]+1 == 1 :
            #print(i)
            #print(TLESIZE[i][1])
            #print(TLESIZE[i][1]+1)
            DATA[i] = textTemp[TLESIZE[i][0] : TLESIZE[i][1]+1]
        else:
            DATA[i] = textTemp[TLESIZE[i]]
        #print(DATA)
    
    
    
##    f= open("test.txt","w")
##    for line in f:
        #textTemp = textTemp + line
    #print (textTemp)
    #print (DATA)
       
fetch(html,name)



