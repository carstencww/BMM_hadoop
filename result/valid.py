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
class_cnt=[[] for x in range(10)]
with open("../data/image_test.txt","r") as images:
	idx = 0 
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
		class_cnt[class_no].append(idx)
		idx += 1

true_label = []
with open("../data/label_test.txt", "r") as f:
	for label in f:
		label = label.strip()
		label = int(label)
		true_label.append(label)

major_labels = [0]*10
correct_images = [0]*10
Num_images = [0]*10

for i in range(10):
	Num_images[i] = len(class_cnt[i])
	count = np.zeros(10)
	for j in range(len(class_cnt[i])):
		count[true_label[class_cnt[i][j]]]+=1
	major_labels[i] = count.argmax()
	correct_images[i] = count[major_labels[i]]
Accuracy = [float(correct_images[i])/Num_images[i] for i in range(10)]
for i in range(0,10):
	print(str(i)+'\t'+str(Num_images[i])+'\t'+str(major_labels[i])+'\t'+str(correct_images[i])+'\t'+"{0:0.2f}".format(Accuracy[i]*100)) 
print("Total"+'\t'+str(sum(Num_images))+'\t'+'\t'+str(sum(correct_images))+'\t'+"{0:0.2f}".format(float(sum(correct_images))*100/sum(Num_images)))
print("\n")

