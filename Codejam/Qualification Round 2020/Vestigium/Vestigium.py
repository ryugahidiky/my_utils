def solve(matrix,n):
	k=0
	r=0
	c=0
	first=True
	for i in range(n):
		row=matrix[i]
		if len(row) != len(set(row)):
			r+=1
		for j in range(n):
			if(i==j):
				k+=matrix[i][j]

			if(first):
				column=[row[j] for row in matrix]
				if len(column) != len(set(column)):
					c+=1
			
		first=False
	return k,r,c
	

	#print("Case #{}: {} {} {} ".format(x, k, r, c))


if __name__ == '__main__':
	t = int(input())
	for x in range(1, t + 1):
		matrix=[]
		n=int(input())

		#reading the matrix:
		for i in range(n):
			a=[]
			a=[int(x) for x in input().split()]
			matrix.append(a)
		#solving
		k,c,r=solve(matrix,n)
		print("Case #{}: {} {} {}".format(x, k, c, r))