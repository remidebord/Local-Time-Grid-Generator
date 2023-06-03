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
  
  print("Display shapefile...")
  fig, ax = plt.subplots()
  polys.plot(ax=ax, facecolor='gray');
  plt.show()
