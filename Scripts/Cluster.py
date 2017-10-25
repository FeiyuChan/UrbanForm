# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Cluster.py
# Created on: 2017-09-14 04:49:18.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Cluster <Input_Feature_Class> <Output_Standard_Distance_Feature_Class> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Input_Feature_Class = arcpy.GetParameterAsText(0)

Output_Standard_Distance_Feature_Class = arcpy.GetParameterAsText(1)

# Local variables:
NNRatio = "0"
NNZScore = "0"
PValue = "0"
NNExpected = "0"
NNObserved = "0"
Report_File = ""

# Process: Average Nearest Neighbor
arcpy.AverageNearestNeighbor_stats(Input_Feature_Class, "EUCLIDEAN_DISTANCE", "GENERATE_REPORT", "")

# Process: Standard Distance
arcpy.StandardDistance_stats(Input_Feature_Class, Output_Standard_Distance_Feature_Class, "1_STANDARD_DEVIATION", "", "")

