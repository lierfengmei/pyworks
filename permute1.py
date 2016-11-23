# permute1.py

def permute(seq):
	result = []
	for a in seq:
		for b in seq:
			for c in seq:
				for d in seq:
					for e in seq:
						if  a!=b and a!=c and a!=d and a!=e and \
							b!=c and b!=d and b!=e and \
							c!=d and c!=e and d!=e:
							result.append(''.join([a,b,c,d,e]))
	return result


seq = list("56789")
where = 3
thelist = permute(seq)
print(thelist)
import calc
calc.calc(thelist,where)
