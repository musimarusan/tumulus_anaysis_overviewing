#! /bin/sh

ROUT=/Volumes/dev02/work/20240828_SVM_processig

TRAIN=${ROUT}/data/learning_and_evaluation/Train/TRAIN
TEST=${ROUT}/data/learning_and_evaluation/Test/TEST


TP=${ROUT}/verif/raster/TP
TN=${ROUT}/verif/raster/TN
FP=${ROUT}/verif/raster/FP
FN=${ROUT}/verif/raster/FN


rm -f ${TP}/*.tif
rm -f ${TN}/*.tif
rm -f ${FP}/*.tif
rm -f ${FN}/*.tif


CSV=${ROUT}/verif/verification.csv

while read line
do
    filename=$(echo ${line} | cut -d , -f 2)
    trueth=$(echo ${line} | cut -d , -f 3)
    prediction=$(echo ${line} | cut -d , -f 4)

    if [ ${trueth} -eq 1 ] && [ ${prediction} -eq 1 ]; then
	echo "TP:" ${filename}
	cp ${TEST}/${filename} ${TP}
    elif [ ${trueth} -eq 1 ] && [ ${prediction} -eq 0 ]; then
	echo "TN:" ${filename}
	cp ${TEST}/${filename} ${TN}
    elif [ ${trueth} -eq 0 ] && [ ${prediction} -eq 1 ]; then
	echo "FP:" ${filename}
	cp ${TEST}/${filename} ${FP}
    elif [ ${trueth} -eq 0 ] && [ ${prediction} -eq 0 ]; then
	echo "FN:" ${filename}
	cp ${TEST}/${filename} ${FN}
    fi

done<${CSV}

exit 0
