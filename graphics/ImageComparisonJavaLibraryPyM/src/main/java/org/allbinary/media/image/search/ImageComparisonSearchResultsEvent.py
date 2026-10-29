#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.media.image.search

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class ImageComparisonSearchResultsEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.imageComparisonSearch: ImageComparisonSearch = None
    

    def __init__(self, anyType: object, imageComparisonSearch: ImageComparisonSearch) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.setImageComparisonSearch(imageComparisonSearch)
    

    def getImageComparisonSearch(self) -> ImageComparisonSearch:
        return self.imageComparisonSearch
    

    def setImageComparisonSearch(self, imageComparisonSearch: ImageComparisonSearch) -> None:
        self.imageComparisonSearch = imageComparisonSearch


