
def solve(s):
	s+="0"
	sol=""
	sol+="("*int(s[0])+s[0]
	i_1=s[0]
	for i in s[1:]:
		par_num=int(i)-int(i_1)
		if(par_num>0):
			sol+="("*par_num
		else:
			sol+=")"*-par_num
		sol+=i
		i_1=i
	return sol[:-1]
	

if __name__ == '__main__':
	t = int(input())
	for x in range(1, t + 1):
		s=input()
		print("Case #{}: {}".format(x,solve(s)))
