'''
Code to map fire territories and fire incidents using leaflet
'''

library('geojsonio')
library('leaflet')
library(rgdal)
library(sf)

#Load datasets

grid <- geojsonio::geojson_read("grids_w_zoneNum.json", what = "sp")
points <- read.csv("Jun_Dec18FireIncients1.csv")
big <- read.csv("big_stations.csv")
stations <- read.csv("station_coords.csv")
new <- read.csv("new_stations.csv")

#Great a leaflet object and add various shapes and markings

p <- leaflet(grid)
p <- addTiles(p)
p <- addCircleMarkers(p, lat = points$lat, lng = points$lng, radius = 1, color = 'red')
p <- addCircles(p, lat = big$lat, lng = big$lng, radius = 4023.36, color = 'green')
p <- addCircles(p, lat = stations$lat, lng = stations$lng, radius = 2414.02)
p <- addPolygons(p, stroke = TRUE, fillOpacity = 0.0, color = 'black')
p <- addPopups(p, lat = stations$lat, lng = stations$lng, stations$Label, options = popupOptions(closeButton = FALSE))
p <- addMarkers(p, lat = stations$lat, lng = stations$lng, label = stations$Label, labelOptions = labelOptions(noHide = T, direction = 'auto', textOnly = F))
p <- addMarkers(p, lat = stations$lat, lng = stations$lng, label = stations$Label)
icons <- awesomeIcons(
  icon = 'ios-close',
  iconColor = 'black',
  library = 'ion',
  markerColor = "red"
)
p <- addAwesomeMarkers(p, lat = new$lat, lng = new$lng, icon = icons)
p <- addCircles(p, lat = new$lat, lng = new$lng, radius = 2414.02, color = "red")
p <- addCircles(p, lat = 33.619720, lng = -84.670624, radius = 4023.36, color = "red")
p <-addLegend(p, colors = c("blue", "green"), labels = c("Fire Engine Coverage", "Ladder Truck Coverage"))
p





