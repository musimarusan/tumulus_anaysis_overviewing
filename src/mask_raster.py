import sys

import folium
import pyproj
import json
import rasterio
import geopandas as gpd

from osgeo import gdal  # For read and manipulate rasters
from affine import Affine  # For easly manipulation of affine matrix

import matplotlib.pyplot as plt 

from pprint import pprint
from pathlib import Path
from rasterio.plot import show
from rasterio.mask import mask
from shapely.geometry import box
from skimage import io


def create_masked_raster(input_image: str, poly, output_image: str ):
    data = rasterio.open(str(input_image))
    masked, mask_transform = mask(dataset=data, shapes=poly.geometry.to_crs(crs={'init': 'epsg:6677'}), crop=True)

    # print('tyep(masked)=',type(masked))
    # print('mask_transform = ',mask_transform)
    out_meta = data.meta


    # print(out_meta)
    out_meta.update({"driver": "GTiff",
                 "height": masked.shape[1],
                 "width": masked.shape[2],
                #  "height": 200,
                #  "width": 150,                    
                #  "count":4,
                 "transform": mask_transform})
    # print(out_meta)

    with rasterio.open(output_image, "w", **out_meta) as dest:
        dest.write(masked)


def main(inpoly: str, inimg: str, outdir: str):

    polygons = gpd.read_file(inpoly)

    for ii in range(len(polygons)):
        poly = polygons[ii:ii+1]

        output_raster_file = f'{outdir}/masked_{int(poly['id'])}.tif'
#        print(output_raster_file)
        create_masked_raster(inimg, poly, output_raster_file )

        
if __name__ == "__main__":

    input_polygon_file = sys.argv[1]
    input_raster_file  = sys.argv[2]
    output_dir         = sys.argv[3]

    print(f'input polygon file = {input_polygon_file}')
    print(f'input raster file  = {input_raster_file}')
    print(f'output directory   = {output_dir}')


    main(input_polygon_file, input_raster_file, output_dir)
