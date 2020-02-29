import datetime
from datetime import datetime
from datetime import timedelta  
import time
import os
from colorama import init 
from termcolor import colored 



def wordClock(currentDT):
	os.system('clear') 

	print (currentDT)
	print("")

	currentDT = str(currentDT)
	currentTime = currentDT[11:19]
	print("Time: " + currentTime)

	currentHour = currentTime[0:2]
	currentMinute = currentTime[3:5]
	currentSecond = currentTime[6:8]
	print("Hour: " + currentHour)
	print("Minute: "+ currentMinute)
	print("Second: "+ currentSecond)


	print("")
	if len(currentMinute)<2:
		currentMinute = '0'+currentMinute

	# Zeit runden
	plusUhr = 0
	t = int(currentMinute[0:2]) + int(currentSecond) / 60.0

	print("Min.Second - Numeric: "+str(t))
	if t < 2.5000:
		mins = '00'
	if 2.5000 <= t < 7.5000:
		mins = '05'
	if 7.5000 <= t < 12.500:
		mins = '10'
	if 12.5000 <= t < 17.500:
		mins = '15'
		plusUhr = 1
	if 17.5000 <= t < 22.500:
		mins = '20'
	if 22.5000 <= t < 27.500:
		mins = '25'
		plusUhr = 1
	if 27.5000 <= t < 32.500:
		mins = '30'
		plusUhr = 1
	if 32.5000 <= t < 37.500:
		mins = '35'
		plusUhr = 1
	if 37.5000 <= t < 42.500:
		mins = '40'
		plusUhr = 1
	if 42.5000 <= t < 47.500:
		mins = '45'
		plusUhr = 1
	if 47.5000 <= t < 52.500:
		mins = '50'
		plusUhr = 1
	if 52.5000 <= t < 57.500:
		mins = '55'
		plusUhr = 1
	if 57.5000 <= t:
		mins = '00'
		plusUhr = 1


	currentHour = int(currentHour) + plusUhr
	if int(currentHour) > 12:
		currentHour = int(currentHour)-12


	if len(str(currentHour))<2:
		currentHour = '0'+str(currentHour)

	if currentHour == "00":
		currentHour = "12"

	print ("Hour new: " + str(currentHour))
	print("Mins new: " + str(mins))

	timeNew = str(currentHour)+':'+str(mins)

	print("Time New: "+timeNew)

	w = 'white'
	m = 'on_magenta'




	if str(mins) == "25":
		print(colored('E S ', w, m)+'K '+colored('I S T ', w, m)+'L '+colored('F U N F', w, m))
	elif str(mins) == "35":
		print(colored('E S ', w, m)+'K '+colored('I S T ', w, m)+'L '+colored('F U N F', w, m))
	elif str(mins) == "05":
		print(colored('E S ', w, m)+'K '+colored('I S T ', w, m)+'L '+colored('F U N F', w, m))
	elif str(mins) == "55":
		print(colored('E S ', w, m)+'K '+colored('I S T ', w, m)+'L '+colored('F U N F', w, m))
	else:
		print(colored('E S ', w, m)+'K '+colored('I S T ', w, m)+'L F U N F')

	if str(mins) == "40":
		print("Z E H N "+colored('Z W A N Z I G', w, m))
	elif str(mins) == "50":
		print(colored('Z E H N ', w, m)+"Z W A N Z I G")
	elif str(mins) == "10":
		print(colored('Z E H N ', w, m)+"Z W A N Z I G")
	elif str(mins) == "20":
		print("Z E H N "+colored('Z W A N Z I G', w, m))
	else:
		print("Z E H N Z W A N Z I G")

	if str(mins) == "45":
		print(colored('D R E I V I E R T E L', w, m))
		#print("DREI"+colored('VIERTEL', w, m))
	elif str(mins) == "15":
		print("D R E I "+colored('V I E R T E L', w, m))
	else:
		print("D R E I V I E R T E L")

	if str(mins) == "25":
		print("T G N A C H "+colored('V O R ', w, m)+"J M")
	elif str(mins) == "35":
		print("T G "+colored('N A C H ', w, m)+"V O R J M")
	elif str(mins) == "40":
		print("T G N A C H "+colored('V O R ', w, m)+"J M")
	#elif str(mins) == "45":
	#	print("TGNACH"+colored('VOR', w, m)+"JM")
	elif str(mins) == "50":
		print("T G N A C H "+colored('V O R ', w, m)+"J M")
	elif str(mins) == "55":
		print("T G N A C H " +colored('V O R ', w, m)+"J M")
	elif str(mins) == "05":
		print("T G "+colored('N A C H ', w, m)+"V O R J M")
	elif str(mins) == "10":
		print("T G "+colored('N A C H ', w, m)+"V O R J M")
	elif str(mins) == "20":
		print("T G "+colored('N A C H ', w, m)+"V O R J M")
	else:
		print("T G N A C H V O R J M")

	if str(currentHour) == "12":
		if str(mins) == "25":
			print(colored('H A L B ', w, m)+"Q "+colored('Z W O L F ', w, m)+"P")
		elif str(mins) == "30":
			print(colored('H A L B ', w, m)+"Q "+colored('Z W O L F ', w, m)+"P")
		elif str(mins) == "35":
			print(colored('H A L B ', w, m)+"Q "+colored('Z W O L F ', w, m)+"P")
		else: 
			print("H A L B Q "+colored('Z W O L F ', w, m)+"P")
	else:
		if str(mins) == "25":
			print(colored('H A L B ', w, m)+"Q Z W O L F P")
		elif str(mins) == "30":
			print(colored('H A L B ', w, m)+"Q Z W O L F P")
		elif str(mins) == "35":
			print(colored('H A L B ', w, m)+"Q Z W O L F P")
		else: 
			print("H A L B Q Z W O L F P")

	if str(currentHour) == "02":
		print(colored('Z W E I ', w, m)+"N S I E B E N")
	elif str(currentHour) == "07":
		print("Z W E I N "+colored('S I E B E N', w, m))
	elif str(currentHour) == "01":
		if (str(mins) == "00"):
			print("Z W "+colored('E I N ', w, m)+"S I E B E N")
		else:
			print("Z W "+colored('E I N S ', w, m)+"I E B E N")
	else:
		print("Z W E I N S I E B E N")


	# hier fehlt noch was!
	if str(currentHour) == "03":
		print("K "+colored('D R E I ', w, m) +"F H R O N F")
	else:
		print("K D R E I F H R O N F")


	if str(currentHour) == "11":
		print(colored('E L F ', w, m)+"N E U N V I E R")
	elif str(currentHour) == "09":
		print("E L F "+colored('N E U N ', w, m)+"V I E R")
	elif str(currentHour) == "04":
		print("E L F N E U N "+colored('V I E R', w, m))
	else:
		print("E L F N E U N V I E R")

	if str(currentHour) == "08":
		print("W "+colored('A C H T ', w, m)+"Z E H N R S")
	elif str(currentHour) == "10":
		print("W A C H T "+colored('Z E H N ', w, m)+"R S")
	else:
		print("W A C H T Z E H N R S")

	if str(currentHour) == "06":
		if str(mins) == "00":
			print ("B "+colored('S E C H S ', w, m)+"F M "+colored('U H R', w, m))
		else:
			print("B "+colored('S E C H S ', w, m)+"F M U H R")
	elif str(mins) == "00":
		print("B S E C H S F M "+colored('U H R', w, m))
	else: 
		print("B S E C H S F M U H R")
	print("")

### MAIN 


init() 
i = 0
datetime_str = '02/02/02 00:00:00'
currentDT = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')


wordClock(currentDT)

while i < 720:
	currentDT = currentDT + timedelta(seconds=60)
	wordClock(currentDT)
	time.sleep(0.3)
	i = i+1
