#! /bin/sh

ROUT=/Volumes/dev02/work/20240810_Kanto-tumulus/data

MISC=${ROUT}/misc

ZIPD=/Volumes/dev02/Data/GIS/全国5ADEM/関東/5As

XMLD=/Volumes/dev02/work/20240810_Kanto-tumulus/data/raster/XML


TARG=${MISC}/target_grid_ID.csv

cd ${ZIPD}
while read LINE
do
    sec=`echo ${LINE} | cut -c 1-4`
    bra=`echo ${LINE} | cut -c 5-6`

    zipf=FG-GML-${sec}-${bra}-DEM5A.zip

    echo ${zipf}
    cp -p ${zipf} ${XMLD}
    
done <${TARG}

exit 0
