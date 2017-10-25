# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Compactness.py
# Created on: 2017-09-14 04:50:03.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Compactness <CBD_CDA> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
CBD_CDA = arcpy.GetParameterAsText(0)

# Local variables:
FCDis = ""
FCDisGeo = FCDis
Output_Feature_Class = FCDisGeo
FC_Dis_Area = Output_Feature_Class
FC_Dis_ConvexHull = ""
ConvexHullArea = FC_Dis_ConvexHull
Output_Feature_Class__2_ = ConvexHullArea
ConvexHullArea2 = Output_Feature_Class__2_
ConvexHullArea3 = ConvexHullArea2
Ratio = ConvexHullArea3
Output_Feature_Class__3_ = Ratio
Area2Perimeter = Output_Feature_Class__3_
Ideal2Actual = Area2Perimeter
IdealActualCompute = Ideal2Actual

# Process: Dissolve
arcpy.Dissolve_management(CBD_CDA, FCDis, "", "", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Geometry Attributes
arcpy.AddGeometryAttributes_management(FCDis, "AREA;PERIMETER_LENGTH", "KILOMETERS", "SQUARE_KILOMETERS", "")

# Process: Add Field
arcpy.AddField_management(FCDisGeo, "km1", "FLOAT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Output_Feature_Class, "km1", "[POLY_AREA]", "VB", "")

# Process: Minimum Bounding Geometry
arcpy.MinimumBoundingGeometry_management(FC_Dis_Area, FC_Dis_ConvexHull, "RECTANGLE_BY_AREA", "NONE", "", "NO_MBG_FIELDS")

# Process: Add Geometry Attributes (2)
arcpy.AddGeometryAttributes_management(FC_Dis_ConvexHull, "AREA", "", "SQUARE_KILOMETERS", "")

# Process: Add Field (2)
arcpy.AddField_management(ConvexHullArea, "km2", "FLOAT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(Output_Feature_Class__2_, "km2", "[POLY_AREA]", "VB", "")

# Process: Add Field (3)
arcpy.AddField_management(ConvexHullArea2, "BaChRatio", "FLOAT", "", "", "", "", "NULLABLE", "REQUIRED", "")

# Process: Calculate Field (3)
arcpy.CalculateField_management(ConvexHullArea3, "BaChRatio", "[km1] / [km2]", "VB", "")

# Process: Add Field (4)
arcpy.AddField_management(Ratio, "Peri2Area", "FLOAT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (4)
arcpy.CalculateField_management(Output_Feature_Class__3_, "Peri2Area", "[PERIMETER]/ [km1]", "VB", "")

# Process: Add Field (5)
arcpy.AddField_management(Area2Perimeter, "IdealActual", "FLOAT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (5)
arcpy.CalculateField_management(Ideal2Actual, "IdealActual", "(4*3.14159265359/ [PERIMETER])/[Peri2Area]", "VB", "")

