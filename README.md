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
