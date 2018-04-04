import numpy as np
from random import sample
#np.random.seed(0)
imagefile = "./data/image_train.txt"
centroid_f = "train_paras.txt"
images= []
pi_k=0.1 #1/10
with open(imagefile, "r") as f:
	for line in f:
		line = line.strip()
		line = line.split(",")
		line = [int(x) for x in line]
		images.append(line)


cans = sample(xrange(0,len(images)),10)
candidates = [images[can] for can in cans]

print(cans)
with open(centroid_f, "w") as cenf:
	i=0
	for candidate in candidates:
		for j in range(len(candidate)):
			if candidate[j] == 1:
				candidate[j] = 0.95
			else:
				candidate[j] = 0.05
		cenf.write(str(i)+'\t'+str(pi_k)+":"+",".join(str(x) for x in candidate)+'\n')
		i+=1
