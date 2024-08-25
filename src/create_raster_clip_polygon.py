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

def create_combined_dataframe(infile: str, reffile: str):

    gdf_inp = gpd.read_file(infile)
    gdf_ref = gpd.read_file(reffile)

    df_inp = pd.DataFrame(gdf_inp)
    df_inp = df_inp.set_index('ID')

    gdf_ext = gdf_ref[['IDテーブル::ID','墳丘情報テーブル::方位（度）', '墳丘形状情報テーブル::墳長（m）']]
    gdf_ext = gdf_ext.rename(columns={'IDテーブル::ID': 'ID'})
    df_ext  = pd.DataFrame(gdf_ext)
    df_ext  = df_ext.set_index('ID')


    df_cnb = pd.concat([df_inp, df_ext], join='inner', axis=1)
    df_cnb = df_cnb.reset_index()

    gdf_cnb = gpd.GeoDataFrame(df_cnb, geometry='geometry', crs='EPSG:6677')
#    print(gdf_cnb)

    return gdf_cnb

def create_polygons(gdf):

    gdf_out = gpd.GeoDataFrame()

    shapely_polygons = []
    id_list         = []
    dir_list         = []
    length_list      = []

    # print('length = ',len(gdf_c['geometry']))

    for ii in range(len(gdf['geometry'])):
        # print(ii)

        id    = gdf['ID'][ii]
        dir    = gdf['墳丘情報テーブル::方位（度）'][ii]
        length = gdf['墳丘形状情報テーブル::墳長（m）'][ii]
        vertex_list = list(gdf['geometry'][ii].exterior.coords)
    
#        buf = int(length / 10) * 3
#        poly = shapely.Polygon(vertex_list).buffer(buf)
#        rect = poly.minimum_rotated_rectangle

#        buf = int(length / 2)
#        poly = shapely.Polygon(vertex_list).buffer(buf)
#        bounds = poly.bounds
#        rect = shapely.box(*poly.bounds)

        buf = int(length/10)*8
        poly = shapely.Polygon(vertex_list)
        center = poly.centroid
        circle = center.buffer(buf)
        rect = circle.envelope
        
        shapely_polygons.append(rect)
        id_list.append(id)
        dir_list.append(dir)
        length_list.append(length)

    return shapely_polygons, id_list, dir_list, length_list

def create_output_polygons(shapely_polygons, id_list, dir_list, length_list, outfile):

    data = {'id':id_list, 'dir':dir_list, 'length':length_list}

    gdf_out = gpd.GeoDataFrame(data, geometry=shapely_polygons, crs='EPSG:6677')

    gdf_out.to_file(outfile, driver='GeoJSON', )



def main(infile, reffile, outfile):
    gdf_combined = create_combined_dataframe(infile, reffile)
#    print(gdf_combined)
    shapely_polygons, id_list, dir_list, length_list = create_polygons(gdf_combined)
#    print(shapely_polygons)
#    print(id_list)
#    print(dir_list)
#    print(length_list)
    create_output_polygons(shapely_polygons, id_list, dir_list, length_list, outfile)
   
    return


if __name__ == "__main__":
    inp_gjson = sys.argv[1]
    ref_gjson = sys.argv[2]
    out_gjson = sys.argv[3]

    print(f'input geoJson     = {inp_gjson}')
    print(f'reference geojson = {ref_gjson}')
    print(f'output geojson    = {out_gjson}')

    main(inp_gjson, ref_gjson, out_gjson)
