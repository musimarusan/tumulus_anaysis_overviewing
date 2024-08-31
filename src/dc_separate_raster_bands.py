import os
import sys
from pathlib import Path
import subprocess
from osgeo import gdal


def main(inraster: str):

        indir = os.path.dirname(inraster)
        band1 = f'{indir}/band1.tif'
        band2 = f'{indir}/band2.tif'
        band3 = f'{indir}/band3.tif'
        band4 = f'{indir}/band4.tif'

        outvrt  = f'{indir}/outvrt.vrt'

        stem = Path(inraster).stem
        outfile = f'{indir}/{stem}_3bands.tif'
        
        cmd1 = f'gdal_translate -of GTiff -b 1 {inraster} {band1}'
        cmd2 = f'gdal_translate -of GTiff -b 2 {inraster} {band2}'
        cmd3 = f'gdal_translate -of GTiff -b 3 {inraster} {band3}'
        cmd4 = f'gdal_translate -of GTiff -b 4 {inraster} {band4}'
        
        subprocess.run(cmd1, shell=True)
        subprocess.run(cmd2, shell=True)
        subprocess.run(cmd3, shell=True)
        subprocess.run(cmd4, shell=True)
        
#        cmd5 = f'gdalbuildvrt -separate {outvrt} {band1} {band2} {band3}'
#        cmd6 = f'gdal_translate {outvrt} {outfile}'
#        subprocess.run(cmd5, shell=True)
#        subprocess.run(cmd6, shell=True)

        cmd5 = f'gdal_merge.py -o {outfile} -co COMPRESS=LZW -co BIGTIFF=YES -separate {band1} {band2} {band3}'
        subprocess.run(cmd5, shell=True)
        
if __name__ == "__main__":

    input_raster_file = sys.argv[1]

    print(f'input rasterfile = {input_raster_file}')

    main(input_raster_file)
