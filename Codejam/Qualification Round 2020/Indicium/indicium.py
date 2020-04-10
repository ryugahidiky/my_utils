def print_it(mat):
	for i in range(len(mat)):
		for j in range(len(mat)):
			print(mat[i][j], end="")
			if j!=len(mat):
				print(" ", end="")
		print()
def find_empty(mat):
	for i in range(len(mat)):
		for j in range(len(mat)):
			if mat[i][j]==0:
				return (i,j)
	return None
def valid(mat, num, pos):
	#check row
	for i in range(len(mat[0])):
		if mat[pos[0]][i]==num and pos[1]!=i:
			return False
	#check column
	for i in range(len(mat)):
		if mat[i][pos[1]]==num and pos[0]!=i:
			return False
	return True
def fill_mat(bo):
	find=find_empty(bo)
	if not find:
		return True
	else:
		row, col=find
	for i in range(1,len(bo)+1):
		if valid(bo, i, (row, col)):
			bo[row][col]=i
			if fill_mat(bo):
				return True
			bo[row][col]=0
	return False	
def create_mat(n,k):
	mat=[[0 for i in range(n)] for j in range(n)]
	l=decompose(n,k)
	for i in range(n):
		for j in range(n):
			if i==j:
				mat[i][j]=l[i]
	if not fill_mat(mat):
		return None
	return mat
def decompose(n,k):
	l=[ 1 for i in range(n)]
	i=0
	while (sum(l)<k):
		if(l[i]>=n):
			i+=1
		l[i]+=1
		if sum(l)==k:
			break
	return l
def solve(x,n,k):

	mat=create_mat(n,k)
	if not mat:
		print("Case #{}:IMPOSSIBLE".format(x))
	else:
		print("Case #{}:POSSIBLE".format(x))
		print_it(mat)
if __name__ == '__main__':
	t = int(input())
	for x in range(1, t + 1):
		a=[int(x) for x in input().split()]
		n=a[0]
		k=a[1]
		if n<2 or k<n or k>n*n:
			print("Case #{}:IMPOSSIBLE".format(x))
		else:
			solve(x,n,k)