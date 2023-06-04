import pytz
import geopandas as gpd
from shapely.geometry import Point, Polygon
from datetime import datetime, timedelta

filename = "./tz_world/tz_world.shp"

if __name__ == "__main__":

  print("Read shapefile %s..." % filename)
  polys = gpd.read_file(filename)

  print("Print polygons....")
  print(polys)

  print("Prepare parameters...")
  # Shapefile use the geodetic system WGS 84.
  # Its a coordinates system which specifies:
  # Minimum latitude = -90°
  # Minimum longitude = -180°
  # Maximum latitude = +90°
  # Maximum longitude = +180°
  #
  # see https://desktop.arcgis.com/fr/arcmap/latest/map/projections/pdf/geographic_coordinate_systems.pdf
  #
  # We want to have n tiles (e.g: 1000000) for the grid.
  # Horizontal axis (longitude) is [-180:+180], twice as much as 
  # vertical axis (latitude) [-90:90], so here are the equations:
  # 
  # longitude tiles -> tiles_x
  # latitude tiles -> tiles_y
  #
  # tiles = tiles_x * tiles_y
  # tiles_x = 2 * tiles_y
  #
  # Which leads to:
  #
  # tiles_x = sqrt(2 * tiles)
  # tiles_y = tiles / tiles_x
  # 
