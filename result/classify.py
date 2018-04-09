#!/usr/bin/env python
import numpy as np

result_q = [0]*10
result_pi = [0]*10
with open("./paras_result.txt","r") as paras:
	for para in paras:
		para = para.strip()
		class_no , para = para.split('\t')
		class_no = int(class_no)
		pi, q = para.split(":")
		q = q.split(",")
		result_pi[class_no] = float(pi)
		result_q[class_no] = [float(x) for x in q]


gamma = np.zeros(10)
class_cnt=[0]*10
with open("../data/image_train.txt","r") as images:
	for image in images:
		image = image.strip()
		image = image.split(",")
		image = [int(x) for x in image]
		for i in range(0,10):
			gamma[i] = result_pi[i]
			for j in range(len(image)):
				if image[j] == 1:
					gamma[i] *= result_q[i][j]
				else:
					gamma[i] *= 1 - result_q[i][j]
		class_no = gamma.argmax()
		class_cnt[class_no]+=1
for i in range(0,10):
	print("Parameter "+str(i)+": "+"{0:0.2f}".format(result_pi[i])+": ["+", ".join("{0:0.2f}".format(x) for x in result_q[i])+"], "+str(class_cnt[i]))
#print(class_cnt)
