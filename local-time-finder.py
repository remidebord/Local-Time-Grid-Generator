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

  print("Create point...")
  p = Point(1.4488911764032935, 43.604560049363485)
  print(p)
  
  print("Search which polygon contain the point...")
  result = polys.contains(p)
  print(polys.loc[result])
  
  print("Get the timezone name which contain the point...")
  name = polys.loc[result].TZID.iloc[0]
  print(name)

  print("Get timezone informations...")
  timezone = pytz.timezone(name)
  print(timezone)

  print("Print UTC offset...")
  d = timezone.localize(datetime.now())
  print(d.utcoffset())
