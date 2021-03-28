Peak Viewer API Reference
===================

This document explain how to build and use the Peak Viewer API.

API goal is to :

- Create/read/update/delete a peak using REST endpoints. HTML forms also available. 
- Retrieve a list of peaks in a given geographical bounding box
- Show stored peaks on a map. On click on a peak, it displays the next 3 days temperature forecast (hourly) on a line chart.



----------


Building Peak Viewer using Docker
-------------

**Prerequisites : ** docker and docker-compose. 
Reference : https://github.com/docker/compose

**Step 1** : Clone this repo :

	git clone https://github.com/libgit2/libgit2
**Step 2** Inside local repo, open a terminal prompt and run :

	docker-compose build 
**Step 3** Once the container is built, you can run it using :

    docker-compose up
**Step 4** Access API root by browsing to http://localhost:8000/

----------

Peak API Endpoints
-------------------

Route    | Description
-------- | ---
GET /peaks/| List all peaks
GET /peaks/{id} | Get peak based on peak ID
DELETE /peaks/{id}|  Delete peak based on peak ID
PUT /peaks/{id}| Update peak based on peak ID 
POST peaks/  | Create peak
GET /getpeakswithinBB/{top_lat},{top_long},{bot_lat},{bot_long} | Retrieve a list of peaks in a given geographical bounding box. 

> **Note:**  Peak attributes have to be inside the body of the request for PUT and POST operations, either as form-data format or json format. 

 **Attributes** for peak are : 
 
- peak_name : Name of the peak (string format)
- coordinates : GPS coordinates of peak. Exemple of valid coordinate : 35.879813, 76.514585
- altitude : Peak altitude in meters.



Records API Endpoints
-------------------
Weather forecast records for a given peak. 

Route    | Description
-------- | ---
GET /records/| List all records
GET /records/{id}| Get record based on record ID
DELETE /records/{id}| Delete record based on record ID
PUT /records/{id} | Update record based on record ID. 
POST records/ | Create record. 


> **Note:**  Records attributes have to be inside the body of the request for PUT and POST operations, either as form-data format or json format. 

**Attributes** for records are : 

- forecasted_at: Forecast Datetime
- peak: Peak reference object
- temperature : Forecast value (in °C)



Peak Viewer
--------------------

An Open Layers map is available to display peaks. 

To access it browse to : http://localhost:8000/map

When clicking on a peak, it will displays the next 3 forecast. 


Documentation
--------------------

This documentation is also available on http://localhost:8000/docs
