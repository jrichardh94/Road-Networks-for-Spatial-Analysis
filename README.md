# Creating primary/secondary/tertiary road shapefiles for each US State and Territory

## Overview
This project retrieves county-level road shapefiles for all 3,200+ counties and counties-equivalent in the United States for spatial transportation analyses

## Objective
The Census Bureau allows for primary roads to be downloaded via a nationalwide shapefile. Secondary roads can be downloaded for each state. Beyond these two levels, “All Roads” are available on the Census FTP website as countywide shapefiles. The objective is to retrieve all roads for all 3,200+ counties, and then merge them into statewide/territory-wide shapefiles.

## Methodology
- Download each county and county-equivalent roads shapefile from the Census Tiger/Line FTP. (allRoads_allStates.py)
- Extract all shapefiles from downloaded zip folders (allStates_to_geopackage.py)
- Merge shapefiles by US State or Territory (allStates_to_geopackage.py)

## Tools Used
- Python
- ArcGIS Pro (arcPython)

## Example Output
(TBC)

## Key Insight
A nationwide “All Roads” shapefile is inadvisable due to file size limitations which cause limitations on geoprocessing speeds. Statewide/territory-wide shapefiles are large enough to avoid dozens (or hundreds) of shapefiles per state, while being robust enough for input into geoprocessing tools.
 
# Creating Primary, Secondary, and Tertiary Road Shapefiles for Each U.S. State and Territory

## Overview
This project builds a scalable spatial dataset of roadway infrastructure across the United States by aggregating county-level road shapefiles into statewide and territory-wide datasets for efficient analysis.

## Objective
While the Census Bureau provides national and state-level datasets for primary and secondary roads, more granular “All Roads” data is only available at the county level. This project automates the retrieval and aggregation of these 3,200+ county shapefiles into usable statewide datasets, enabling large-scale transportation and spatial analysis without performance limitations.

## Methodology
- Programmatically download county and county-equivalent road shapefiles from the Census TIGER/Line FTP (allRoads_allStates.py)
- Extract and standardize shapefile data from compressed archives (allStates_to_geopackage.py)
- Merge county-level shapefiles into unified state and territory datasets for downstream analysis

## Tools Used
- Python (data retrieval and processing)
- ArcGIS Pro / ArcPy (spatial processing and geoprocessing workflows)

## Example Output
(Insert 1–2 images of maps or charts)

## Key Insight
Processing road data at a statewide scale provides an optimal balance between data granularity and performance. National datasets are too large for efficient geoprocessing, while county-level datasets create fragmentation. State-level aggregation enables scalable spatial analysis while maintaining sufficient detail for modeling and decision-making.

## Application
These datasets can support:
- transportation accessibility analysis  
- infrastructure planning and prioritization  
- spatial modeling of connectivity and travel patterns  

## Reusability
The data retrieval process is modular and can be adapted to download other datasets from the Census FTP by modifying the BASE_URL parameter in the allRoads_allStates.py script.
