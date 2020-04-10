def solve(unsorted_list):
	sorted_list = sorted(unsorted_list, key=lambda tup: tup[0])
	res="C"
	c=sorted_list[0]
	j=[0,0]
	for i in sorted_list[1:]:
		current_task=i
		if current_task[0]>=c[1]:
			res+="C"
			c=current_task
		else:
			if current_task[0]>=j[1]:
				res+="J"
				j=current_task
			else:
				return "IMPOSSIBLE"
	result=""
	for i in unsorted_list:
		result+=res[sorted_list.index(i)]
		sorted_list[sorted_list.index(i)]=[0,0]
	return result

if __name__ == '__main__':
	t = int(input())
	for x in range(1, t + 1):
		matrix=[]
		n=int(input())

		#reading the matrix:
		for i in range(n):
			a=[int(x) for x in input().split()]
			matrix.append(a)
		#solving
		print("Case #{}: {}".format(x, solve(matrix)))