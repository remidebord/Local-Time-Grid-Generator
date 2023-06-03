import pytz
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

filename = "./tz_world/tz_world.shp"

if __name__ == "__main__":

  print("Read shapefile %s..." % filename)
  polys = gpd.read_file(filename)

  print("Print polygons....")
  print(polys)

  print("Create point...")
  p = Point(1.4488911764032935, 43.604560049363485)
  print(p)

  print("Put point in a geodataframe...")
  d = {'col1': ['Toulouse'], 'geometry': [p]}
  gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")

  print("Display shapefile and point...")
  fig, ax = plt.subplots()
  polys.plot(ax=ax, facecolor='gray');
  gdf.plot(ax=ax, facecolor='red');
  plt.show()
