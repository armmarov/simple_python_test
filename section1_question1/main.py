

def calc(n):
	r_fac = 1
	r_sum = 0

	for x in reversed(range(n+1)):
		if x>0:
			r_fac *= x
	
	for x in str(r_fac):
		r_sum += int(x)

	return r_fac, r_sum

res1, res2 = calc(100)
print(res2)
