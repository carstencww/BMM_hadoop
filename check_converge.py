#!/usr/bin/env python
import numpy as np

origin_centroid = [0]*10

with open("./train_centroid.txt","r") as cens:
	for cen in cens:
		cen = cen.strip()
		class_no , centroid = cen.split('\t')
		class_no = int(class_no)
		centroid = centroid.split(",")
		origin_centroid[class_no] = [float(x) for x in centroid]
origin_centroid = np.asarray(origin_centroid)


result_centroid = [0]*10

with open("./centroid_result.txt","r") as cens:
	for cen in cens:
		cen = cen.strip()
		class_no , centroid = cen.split('\t')
		class_no = int(class_no)
		centroid = centroid.split(",")
		result_centroid[class_no] = [float(x) for x in centroid]
result_centroid = np.asarray(result_centroid)
diff = np.linalg.norm(origin_centroid - result_centroid, axis=1)
dist = diff.sum()
if dist<0.0001:
	print("0")
else: 
	print("1")
print(dist)
