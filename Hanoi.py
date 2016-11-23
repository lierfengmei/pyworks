# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n,a,b,c):
	if(1==n):
		print(a,'->',c)
	else:
		move(n-1,a,c,b)
		print(a,'->',c)
		move(n-1,b,a,c)

move(6,'A','B','C')