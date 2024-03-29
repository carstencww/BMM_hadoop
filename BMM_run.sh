#!/bin/bash

OUT_FILE=/user/ChanCarsten/out_BMM
IN_FILE=/user/ChanCarsten/input_BMM/image_train.txt
BMM () {
hadoop dfs -rm -R $OUT_FILE
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.map.tasks=20 \
-D mapred.reduce.tasks=10 \
-file $PWD/train_paras.txt \
-file $PWD/map_BMM.py -mapper map_BMM.py \
-file $PWD/red_BMM.py -reducer red_BMM.py \
-input $IN_FILE \
-output $OUT_FILE
hadoop fs -getmerge $OUT_FILE ./paras_result.txt
}
echo $PWD
BMM
converging=( $(./check_converge.py) )
while [ ${converging[0]} = 1 ]; do
mv paras_result.txt train_paras.txt
echo ${converging[1]} >> log.txt
BMM
converging=( $(./check_converge.py) )
done











