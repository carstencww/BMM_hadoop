#!/bin/bash

OUT_FILE=/user/ChanCarsten/hw1a
IN_FILE=/user/ChanCarsten/input/image_train.txt
kmean () {
hadoop dfs -rm -R $OUT_FILE
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.map.tasks=10 \
-D mapred.reduce.tasks=10 \
-file $PWD/train_centroid.txt \
-file $PWD/map_kmean.py -mapper map_kmean.py \
-file $PWD/red_kmean.py -reducer red_kmean.py \
-input $IN_FILE \
-output $OUT_FILE
hadoop fs -getmerge $OUT_FILE ./centroid_result.txt
}
echo $PWD
kmean
converging=( $(./check_converge.py) )
while [ ${converging[0]} = 1 ]; do
mv centroid_result.txt train_centroid.txt
echo ${converging[1]} >> log.txt
kmean
converging=( $(./check_converge.py) )
done











