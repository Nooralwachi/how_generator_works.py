from sys import getsizeof
def calc_avg(filename):
	total=0
	total_nums=0
	nums =[int(line.strip()) for line in open(filename, 'r')]
	#gives size for list comprehension
	x = getsizeof(nums) 
	print("x = ", x)
	for num in nums:
		total +=int(num)
		total_nums +=1
	print(f'total = {total}, totanl_nums = {total_nums}')
	print(f'Avg = {float(total/total_nums)}')
calc_avg('random.txt')
calc_avg('random2.txt')
print('--------')
def generate_avg(filename):
	total=0
	total_nums=0
	num_gen = (int(line.strip()) for line in open(filename, 'r'))
	#gives size for generator expression
	y = getsizeof(num_gen) 
	print("y = ", y) #will stay same size for both files
	for num in num_gen:
		# print(num)
		total +=int(num)
		total_nums +=1
	print(f'total = {total}, totanl_nums = {total_nums}')
	print(f'Avg = {float(total/total_nums)}')
generate_avg('random.txt')
generate_avg('random2.txt')
