import sys
import os
import subprocess

from osgeo import gdal


def isExistDir(dir: str):
    ret = os.path.isdir(dir)

    return ret


def ChkDirExist(indir: str, outdir: str):
    
    if isExistDir(indir) != False:
        ret1 = 0
    else:
        print('not exists input directory.',indir)
        ret1 = 1
        
    if isExistDir(outdir) != False:
        ret2 = 0
    else:
        print('not exists output directory.',outdir)
        ret2 = 2
        
    return ret1+ret2



def main(indir: str, outdir: str):
    #
    if ChkDirExist(indir, outdir) != 0:
        print('processing terminated.')
        exit()
    #
    list_targ_stem  = [ f for f in os.listdir(indir) if os.path.isdir(os.path.join(indir, f)) ]

    for targ_stem in list_targ_stem:
        individual_dem_file = f'{indir}/{targ_stem}'
        target_dem_file     = f'{outdir}/dem_{targ_stem}.tif'

        cmd = f'gdal_merge.py -o {target_dem_file} {individual_dem_file}/*.tif'
        subprocess.run(cmd, shell=True)

        
if __name__ == "__main__":
    input_dir  = sys.argv[1]
    output_dir = sys.argv[2]

    print(f'Input directory  = {input_dir}')
    print(f'Output directory = {output_dir}')

    main(input_dir, output_dir)
