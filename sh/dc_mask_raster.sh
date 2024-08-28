#! /bin/sh


ROUT=/Users/hiroakit/dev02/work/20240827_create_training-data

SRC=${ROUT}/src
DATA=${ROUT}/data

echo ${SRC}

cd ${SRC}


TRUE_RANGE=/Volumes/dev02/work/20240827_create_training-data/data/Polygons/Tumulus_Range/TRUE
FALSE_RANGE=/Volumes/dev02/work/20240827_create_training-data/data/Polygons/Tumulus_Range/FALSE
PFALSE_RANGE=/Volumes/dev02/work/20240827_create_training-data/data/Polygons/Tumulus_Range/PseudoFALSE

RASTER=/Volumes/dev02/work/20240827_create_training-data/data/Raster/CSMap/merged_csmap.tif

TRUE_OUT=/Volumes/dev02/work/20240827_create_training-data/data/Raster/True/Masked
FALSE_OUT=/Volumes/dev02/work/20240827_create_training-data/data/Raster/False/Masked


#TRUE
for file in `ls ${TRUE_RANGE}`
do
    python3 mask_raster.py ${TRUE_RANGE}/${file} ${RASTER} ${TRUE_OUT}
done


#FALSE
for file in `ls ${FALSE_RANGE}`
do
    python3 mask_raster.py ${FALSE_RANGE}/${file} ${RASTER} ${FALSE_OUT}
done


#pseudoFALSE
for file in `ls ${PFALSE_RANGE}`
do
    python3 mask_raster.py ${PFALSE_RANGE}/${file} ${RASTER} ${FALSE_OUT}
done





