from __future__ import print_function
import time

width = input("Please enter the width:")
height = input("Please enter the height:")
width = int(width)
height =int(height)
horizontal=[]
hor_list=[]
vertical=[]
input_file=open("a.txt")
start_time=time.time()

def check_line(line):
	result = []
	counter = 0;
	for item in line:
		if item == 0:
			if counter != 0:
				result.append(counter)
				counter = 0
		else:
			counter += 1;
	if counter != 0:
		result.append(counter)
	return result

def match(list1, list2):
	return list1==list2

def draw_line_r(list):
	line = []
	sign = 0
	for item in list:
		for i in range(item):
			line.append(sign)
		sign = (sign+1)%2
	return line
'''
def split_bean(num,part):
	slist = []
	slist.append()
'''
def draw_line(list,length):
	pos_draw = []

	for i in range(pow(2,length)):
		temp = format(i,"#0%db"%(length+2))[2:]
		temp = [int(x) for x in temp]
		temp_list = check_line(temp)
		if match(temp_list,list):
			pos_draw.append(temp)
	'''
	draw_list = [0]
	for item in list:
		draw_list.append(item)
		draw_list.append(1)
	draw_list[-1]=0

	diff = length-sum(list)-len(list)
	if diff==0:
		pos_draw.append(draw_line_r(draw_list))
	else:
		

	'''
	return pos_draw

def check_pline(line):
	result = []
	counter = 0;
	for item in line:
		if item == 0:
			if counter != 0:
				result.append(counter)
				counter = 0
		else:
			counter += 1;
	result.append(counter)
	return result

def if_in(list_partial,list2):
	for idx,item in enumerate(list_partial[:-1]):
		if item != list2[idx]:
			return False
	if len(list_partial)>len(list2):
		if list_partial[-1]==0:
			return True
		else:
			return False
	elif list_partial[-1]>list2[(len(list_partial)-1)]:
		return False
	return True

def get_true(lista,diff):
	temp_true = [1]*(width+1)
	for i in range(diff+1):
		temp_list=[0]*i
		for item in lista:
			temp_list.extend([1]*item)
			temp_list.append(0)
		temp_list.extend([0]*(temp_diff-i))
		temp_true = [x&y for (x,y) in zip(temp_true,temp_list)]
	result = [idx for idx,item in enumerate(temp_true) if item==1]
	return result

# Enter the vertical line hortizontally
print("Loading Horizontal")
for i in range(width):
	#temp_input = input("Enter Column %d:"%i)
	temp_input = input_file.readline()
	temp_input = temp_input.strip("\n").split(" ")
	horizontal.append([int(x) for x in temp_input])
	hor_list.append(draw_line(horizontal[i],height))
	print("%d"%(i+1),"/","%d"%width)

# Enter the horizontal lines vertically
print("Enter Vertical")
for i in range(height):
	#temp_input = input("Enter Line %d:"%i)
	temp_input = input_file.readline()
	temp_input = temp_input.strip("\n").split(" ")
	vertical.append([int(x) for x in temp_input])
	temp_diff = width-sum(vertical[i])-len(vertical[i])+1
	if temp_diff<max(vertical[i]):
		print("found %d"%(i+1),end="")
		temp_list = get_true(vertical[i],temp_diff)
		print(temp_list,end="")
		for idx in temp_list:
			hor_list[idx]=[x for x in hor_list[idx] if x[i]==1]
		print(" ")
	print("%d"%(i+1),"/","%d"%height)

total = 0
for line in horizontal:
	for item in line:
		total = total+item

print("Total %d Dots."%total)
final_array=[]
test_count = 0

def find_s(array):
	if len(array)>2:
			for i in range(len(array[0])):
				sum_temp=[x[i] for x in array]
				if sum(sum_temp)>sum(vertical[i]):
					#print("false")
					return False
				elif not if_in(check_pline(sum_temp),vertical[i]):
					return False
	if len(array)==width:
		is_match=1
		print("test")
		for i in range(height):
			temp = [x[i] for x in array]
			temp_list = check_line(temp)
			if not match(temp_list,vertical[i]):
				is_match=0
				break
		if is_match:
			global final_array
			final_array=array
			return True
		else:
			return False
	else:
		for j in range(len(hor_list[len(array)])):
			array.append(hor_list[len(array)][j])
			if find_s(array):
				return True
			del array[-1]

if find_s([]):
	#print(final_array)
	print("Found Solution")
	for y in range(len(final_array[0])):
		for x in range(len(final_array)):
			if final_array[x][y]==1:
				print("*",end="")
			else:
				print(" ",end="")
		print("\n",end="")

input_file.close()
print("Spend %.2f s"%(time.time()-start_time))
