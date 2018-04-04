#!/usr/bin/env python
import sys
import numpy as np
cnt = 0
origin_q = [0]*10
origin_pi = [0]*10


with open("./train_paras.txt","r") as cens:
	for cen in cens:
		cen = cen.strip()
		class_no , paras = cen.split('\t')
		class_no = int(class_no)
		pi, vector  = paras.split(":")
		vector =vector.split(",")
		origin_pi[class_no] = float(pi)
		origin_q[class_no] = [float(x) for x in vector]
origin_q = np.asarray(origin_q)

q_numer_sum = np.zeros((10,origin_q.shape[1]))
pi_numer_sum = [0] * 10
for line in sys.stdin:
	partial_gamma = [0]*10
	cnt+=1
	line = line.strip()
	pixels = line.split(",")
	pixels = [int(x) for x in pixels]
	pixels = np.asarray(pixels)
	for i in range(0,10):
		partial_gamma[i] = origin_pi[i]
		for j in range(len(pixels)):
			if pixels[j] == 1:
				partial_gamma[i] *= origin_q[i][j]
			else:
				partial_gamma[i] *= 1 - origin_q[i][j]

	total = sum(partial_gamma)

	gamma = [x / total for x in partial_gamma]	
#	print(gamma)
	for i in range(0,10):
		pi_numer_sum[i] += gamma[i]
		q_numer_sum[i] += gamma[i] * pixels
	
for i in range(0,10):
	print(str(i)+"\t"+str(pi_numer_sum[i])+":"+",".join(str(x) for x in q_numer_sum[i]))
print("__CNT__"+'\t'+str(cnt))



