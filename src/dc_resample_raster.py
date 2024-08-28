import sys
import os
from pathlib import Path
import subprocess

from osgeo import gdal



def main(indir: str, outdir: str):

#    list_targ_stem  = [ f for f in os.listdir(indir) if os.path.isdir(os.path.join(indir, f)) ]

    targ_files = os.listdir(indir)
    
    for targ_file in targ_files:
        
        targ_file = f'{indir}/{targ_file}'
        
        p_file = Path(targ_file)
        targ_stem = p_file.stem

        resampled_file = f'{outdir}/{targ_stem}_resampled.tif'
        print(resampled_file)

        
        cmd = f'gdal_translate -outsize 50 50 {targ_file} {resampled_file}'
        subprocess.run(cmd, shell=True)



if __name__ == "__main__":
    input_dir  = sys.argv[1]
    output_dir = sys.argv[2]

    print(f'Input directory  = {input_dir}')
    print(f'Output directory = {output_dir}')

    main(input_dir, output_dir)
