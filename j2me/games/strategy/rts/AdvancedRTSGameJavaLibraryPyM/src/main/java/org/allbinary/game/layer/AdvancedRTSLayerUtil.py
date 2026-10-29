# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot  
# Generated Code Do Not Modify
# package org.allbinary.game.layer

from __future__ import annotations



class AdvancedRTSLayerUtil:
    instance: AdvancedRTSLayerUtil = None
    

    @staticmethod
    def getInstance() -> AdvancedRTSLayerUtil:
        return AdvancedRTSLayerUtil.instance
    

    def createFakeRTSLayerHashtable(self, baseRaceTrackGeographicMap: BaseRaceTrackGeographicMap) -> ABHashtable[object, object]:
        from org.allbinary.game.layer.RTSLayerUtil import RTSLayerUtil
        hashtable: ABHashtable[object, object] = RTSLayerUtil.getInstance().createFakeRTSLayerHashtable(baseRaceTrackGeographicMap)
        hashtable.put(WorkWaypoint.ID, SmallIntegerSingletonFactory.getInstance().getAt(50))
        return hashtable
from org.allbinary.game.layer.waypoint.WorkWaypoint import WorkWaypoint
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.graphics.geography.map.racetrack.BaseRaceTrackGeographicMap import BaseRaceTrackGeographicMap
from org.allbinary.util.ABHashtable import ABHashtable


AdvancedRTSLayerUtil.instance = AdvancedRTSLayerUtil()

