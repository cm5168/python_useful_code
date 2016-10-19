import urllib.request
from time import sleep
import random

start_num = 13458238
end_num = 15522906
list_n = []

for x in range(start_num,end_num+1):
	sleep(random.uniform(0.5,1))
	try:
		with urllib.request.urlopen('http://www.shuotxts.com/8/30/30360/%d.html'%x) as response:
			html = response.read()
			with open("%d.txt"%(x-13458237),'wb') as wfile:
				wfile.write(html)
				print("Done %d"%(x-13458237))
			sleep(random.uniform(0.5,1))
	except:
		print("Cannot read %d"%(x-13458237))
		list_n.append(x-13458237)

with open("not.txt",'w') as w:
	for item in list_n:
		w.write("%d\n"%item)
