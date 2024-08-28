import sys
from pathlib import Path
import numpy as np
import pandas as pd
import geopandas as gpd

from matplotlib import pyplot as plt

import shapely
from shapely.plotting import plot_line
from shapely.plotting import plot_points
from shapely.plotting import plot_polygon
from shapely import affinity
from shapely.geometry import Point


def read_geojson(infile: str):
    targ_epsg = 6677
    
    gdf = gpd.read_file(infile,)
    gdf = gdf.to_crs(epsg = targ_epsg)

#    max_tumulus_length = int( max(gdf['墳丘形状情報テーブル::墳長（m）']) )
    
    return gdf

    

def calculate_offset(maxlen: int):
    deno = 3
    
    xoff1 = int(-maxlen / deno)
    yoff1 = int(maxlen / deno)

    xoff2 = 0
    yoff2 = int(maxlen / deno)

    xoff3 = int(maxlen / deno)
    yoff3 = int(maxlen / deno)

    xoff4 = int(-maxlen / deno)
    yoff4 = 0
        
    xoff5 = 0
    yoff5 = 0

    xoff6 = int(maxlen / deno)
    yoff6 = 0

    xoff7 = int(-maxlen / deno)
    yoff7 = int(-maxlen / deno)

    xoff8 = 0
    yoff8 = int(-maxlen / deno)

    xoff9 = int(maxlen / deno)
    yoff9 = int(-maxlen / deno)

    offset_list = [ [xoff1, yoff1], [xoff2, yoff2], [xoff3, yoff3],
                    [xoff4, yoff4], [xoff5, yoff5], [xoff6, yoff6],
                    [xoff7, yoff7], [xoff8, yoff8], [xoff9, yoff9]]
                    
    return offset_list


def move_point(gdf, xoffset: int, yoffset: int):

    gdf['geometry'] = gdf['geometry'].apply(affinity.translate, xoff=xoffset, yoff=yoffset)
                         
    return gdf



def create_polygon(gdf, scale: float):

    gdf.set_index('IDテーブル::ID',inplace=True)

    buf = max(gdf['墳丘形状情報テーブル::墳長（m）']) * scale
    
    gdf = gdf.buffer(buf).envelope
        
    return gdf


def write_geojson(gdf, outfile):
    targ_epsg = 4326

    gdf.to_file(outfile, driver='GeoJSON', )
    

def main(infile: str, outpath: str, length: int, scale: int):

#    dummy, mxlen = read_geojson(infile)
    offset_list = calculate_offset(length)

    for offset in offset_list:

        gdf1 = gpd.GeoDataFrame()
        gdf2 = gpd.GeoDataFrame()

        gdf = read_geojson(infile)
                
        xoff = int(offset[0])
        yoff = int(offset[1])
#        print(xoff,yoff)

        gdf1 = move_point(gdf,xoff,yoff)
        gdf2 = create_polygon(gdf1, scale)

        p_file = Path(infile)
        targ_stem   = p_file.stem
#        parent_path = p_file.parent
#        print(parent_path, targ_stem)

        outfile = f'{outpath}/{targ_stem}_TRUE_{xoff}{yoff}.geojson'
        
        write_geojson(gdf2, outfile)
   
    return


if __name__ == "__main__":
    inp_gjson = sys.argv[1]
    out_path  = sys.argv[2]
    length    = int( sys.argv[3] )
    scale     = float( sys.argv[4] )

    print(f'input geoJson = {inp_gjson}')
    print(f'output path   = {out_path}')
    print(f'length        = {length}')    
    print(f'scaale        = {scale}')    

    main(inp_gjson, out_path, length, scale)
