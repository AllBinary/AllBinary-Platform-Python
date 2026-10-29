# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.game.input.RTSLayerFormFactoryInterface import RTSLayerFormFactoryInterface


class RTSLayerFormFactory(RTSLayerFormFactoryInterface):
    

    def getInstance(self, rtsLayer: RTSLayer) -> ScrollSelectionForm:
        raise RuntimeError()
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm


