#! /bin/sh


ROUT=/Volumes/dev02/work/20240828_SVM_processig/data


ORG_TRUE=${ROUT}/Original_Raster/TRUE
ORG_FALSE=${ROUT}/Original_Raster/FALSE


TRAIN_TRUE=${ROUT}/learning_and_evaluation/Train/TRUE
TRAIN_FALSE=${ROUT}/learning_and_evaluation/Train/FALSE

TEST_TRUE=${ROUT}/learning_and_evaluation/Test/TRUE
TEST_FALSE=${ROUT}/learning_and_evaluation/Test/FALSE

THRES=8


#TRUE
for file in `ls ${ORG_TRUE}`
do
    RND=$((RANDOM %10 +1))
    if [ ${RND} -lt ${THRES} ] ; then 
	cp ${ORG_TRUE}/${file} ${TRAIN_TRUE}/
    else
	cp ${ORG_TRUE}/${file} ${TEST_TRUE}/
    fi    
done


#FALSE
for file in `ls ${ORG_FALSE}`
do
    RND=$((RANDOM %10 +1))
    if [ ${RND} -lt ${THRES} ] ; then 
	cp ${ORG_FALSE}/${file} ${TRAIN_FALSE}/
    else
	cp ${ORG_FALSE}/${file} ${TEST_FALSE}/
    fi    
done
