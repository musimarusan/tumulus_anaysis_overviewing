import sys
import pandas as pd
import geopandas as gpd

from matplotlib import pyplot as plt
import numpy as np
import shapely
from shapely.plotting import plot_line
from shapely.plotting import plot_points
from shapely.plotting import plot_polygon
from shapely.geometry import Point


def read_geojson(infile: str):
    targ_epsg = 6677
    
    gdf = gpd.read_file(infile,)
    gdf = gdf.to_crs(epsg = targ_epsg)
    
    return gdf


def create_polygon(gdf):

    gdf.set_index('IDテーブル::ID',inplace=True)

    buf = gdf['墳丘形状情報テーブル::墳長（m）'] * 0.8
    
    gdf = gdf.buffer(buf).envelope

        
    return gdf


def write_geojson(gdf, outfile):
    targ_epsg = 4326

    gdf.to_file(outfile, driver='GeoJSON', )
    

def main(infile, outfile):

    gdf = read_geojson(infile)
    gdf = create_polygon(gdf)
    write_geojson(gdf, outfile)
   
    return


if __name__ == "__main__":
    inp_gjson = sys.argv[1]
    out_gjson = sys.argv[2]

    print(f'input geoJson     = {inp_gjson}')
    print(f'output geojson    = {out_gjson}')

    main(inp_gjson, out_gjson)
