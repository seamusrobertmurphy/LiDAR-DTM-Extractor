# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LiDAR-DTM-Extractor
                                 A QGIS plugin
 Used to process, clean, classify and clip continuous point-cloud data into DTM raster layer over user site selection
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-01
        copyright            : (C) 2022 by Cabin Resource Management
        email                : seamusrobertmurphy@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LiDAR-DTM-Extractor class from file LiDAR-DTM-Extractor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LiDAR-DTM-Extractor import LiDAR-DTM-Extractor
    return LiDAR-DTM-Extractor(iface)
