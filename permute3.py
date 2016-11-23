
#permute3.py

def permute(seq):
	l = len(seq)
	if l<=2:
		if 2==l:
			return [seq,[seq[1],seq[0]]]
		else:
			return [seq]
	else:
		res = []
		for i in range(l):
			rest = seq[:i]+seq[i+1:]
			for x in permute(rest):
				res.append(seq[i:i+1]+x)
		return res


seq = list("12345")
thelist = permute(seq)
thelist = [''.join(x) for x in thelist]
print(thelist)


