# UrbanForm
urban form metrics for small to medium sized cities

These toolsets were made to accompany Quantifying the sustainability of urban growth and form through time: An algorithmic analysis of a city's development

##Inputs ArcGIS Python Toolbox:
Here are four toolsets in the form of ArcGIS  toolboxes and accompanying python scripts.

###Connectivity
######Requirements: 
Roads layer, City or Area of Interest Layer
######Use: 
Judges the mean intersection density
######Description: 
This tool measures the intersection density across a city or pre-defined area using a 440 meter default. Outputs a point density raster.
#######Key Statistics: 
Raster of city connectivity and connectivity statistics.

Clustering
Requirements: Building footprint, city center/CBD
Use: clustering of houses toward one another is calculated using nearest neighbor algorithm. While standard distance calculation is used to measure distance from the CBD.
Description: This tool measures the average nearest neighbor (observed is the important for further comparative analysis) and standard distance.
Key Statistics: observed mean nearest neighbor and standard distance.

Density
Requirements: Enumeration Boundaries, Population Statistics
Use: calculates various household and population densities.
Description: This tool takes a file of enumeration boundaries and user input for household and population (which can be derived from the census) and calculates densities therefrom.
Key Statistics: Population Density, Persons per household

Compactness
Requirements: City Limits
Uses: calculates actual versus optimal perimeter to area ratio for the city and calculates the convex hull ratio to actual city.
Description: The ideal to actual ratio shows how close the geometry of the city is to that of a circle, the most efficient form. The convex hull to built extent ratio also is a measure of compactness.
Key Statistics: IdealActual field gives the ratio of the ideal perimeter to area versus actual for the area of study, whereas, the field BaChRatio is the built area to convex hull ratio needed for further study

