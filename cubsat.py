#import urllib3
f= open("test.txt","w")
##import urllib
##
###http = urllib3.PoolManager()
##
###r = http.request('GET', 'https://www.celestrak.com/NORAD/elements/cubesat.txt')#fields={'arg': 'value'})
##r = urllib.urlopen('https://www.celestrak.com/NORAD/elements/cubesat.txt').read()
##n = 0
##for line in r:
##    if n>3:
##        break
##    elif str(r).startswith("b'CUTE-1"):
##        n = n + 1
##        f.write(str(line))
 
import requests
response = requests.get('https://www.celestrak.com/NORAD/elements/cubesat.txt')
#print(response.encoding)
body = response.content   
body2 = response.text

f.write(body2)
f.close()
f= open("test.txt","r")
printed = False
#body = response.text    
n = 0
name = input("Enter Name: ")

for line in f:
    #print (line)
    if line.startswith(name):# and n<4:
        printed = True
        

        
    if printed and n<6:
        n = n + 1
        print(line)
    elif n<6:
        printed = False
        
#datat = r.data
#print(for )
#print (datat)
#print(r.headers)



#json.loads(r.data.decode('utf-8'))['args']

#f.write(str(r.data))
f.close() 


















##for line in datat:
##    print (line)
##    n = n +1
##    if n >50:
##        break
