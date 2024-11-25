import time
currenttime=time.strftime('%H:%M:%S')
print(currenttime)
currenthour=int(time.strftime('%H'))
print(currenthour)
currentmin=time.strftime('%M')
print(currentmin)
currentsec=time.strftime('%S')
print(currentsec)
if( 4 <= currenthour <12):
    print("goodmorning")
else:
    print("goodafternoon")