# 🌐 Magicbox Routing API
Utilities to retrieve road networks and compute distances between geospatial coordinates for UNICEF's Magicbox.

![Screenshot](https://raw.githubusercontent.com/msradam/magicbox-routing-api/master/misc/screenshot.png)

## Setup
Note: `sudo` is needed if you are not in the `docker` user group on your system.
```
sudo docker-compose build
sudo docker-compose up
```
The app will run on `http://0.0.0.0:8000`, which will display the API documentation with the appropriate endpoints. 

## Distances

Endpoint: `/distances/upload/`

### Straight-line
Computes straight-line (i.e. haversine) distances between two sets of geographical points (origin sites & destination sites), and will output an 
updated .csv of the origin sites. You must specify the type of destination site. 

Example POST request:
```
curl --request POST \
  --url http://0.0.0.0:8000/distances/upload/ \
  --header 'content-type: multipart/form-data' \
  --form origin_pts=@/home/msradam/Projects/magicbox-geo-api/belize_pop.csv \
  --form dest_pts=@/home/msradam/Projects/magicbox-geo-api/belize_hs.csv \
  --form dest_type=healthsite
```
### Routed
Computes routed distances via a specified country road network. The request schema includes an additional argument - the country's name - 
which queries local storage to determine if the road network for that country has been downloaded. Similarly returns an updated .csv of the origin sites
.csv. with an additional column for routed distance.

Example POST request:
```
curl --request POST \
  --url http://0.0.0.0:8000/distances/upload/ \
  --header 'content-type: multipart/form-data' \
  --form origin_pts=@/<path_to_csv>/belize_pop.csv \
  --form dest_pts=@/<path_to_csv>/belize_hs.csv \
  --form dest_type=healthsite
  --form country_name=Belize
```

### Road Retrieval

Endpoint: `/roads/retrieve/`

Obtains a NetworkX graph from OpenStreetMap via OSMNX and converts it to an iGraph object to perform computations on later:

Example POST Request:
```
curl --request POST \
  --url http://0.0.0.0:8000/distances/upload/ \
  --header 'Content-Type: application/json' \
  --data '{"country_name": "string",
          "network_type": "string",
          "filepath": "string"}'
```
Network type and filepath are optional - network type allows you specify the kind of roads that are download (default: all), 
filepath allows you to specify an absolute path in local storage for the graph to be stored.

## In-Progress
* Travis CI integration
* MongoDB storage for graphs
* Kepler.gl interface as a frontend
* Additional API endpoints to extend functionality
