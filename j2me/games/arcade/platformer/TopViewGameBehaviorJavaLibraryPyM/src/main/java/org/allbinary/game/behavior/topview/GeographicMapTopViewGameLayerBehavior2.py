# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.behavior.topview

from __future__ import annotations

from org.allbinary.game.behavior.topview.GeographicMapTopViewLayerBehavior import GeographicMapTopViewLayerBehavior


class GeographicMapTopViewGameLayerBehavior2(GeographicMapTopViewLayerBehavior):

    def _init_fields(self) -> None:
        self.gravityUtil: GravityUtil = GravityUtil.getInstance()
        self.geographicMapBehavior: MultiGeographicMapBehavior = MultiGeographicMapBehavior()
        self.autoStepBlocks: bool = None
        self.offsetY: int = None
        self.previousGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    def __init__(self, maxGravityActionIndex: int, autoStepBlocks: bool, offsetY: int) -> None:
        super().__init__(maxGravityActionIndex)
        self._init_fields()
        self.autoStepBlocks = autoStepBlocks
        self.offsetY = offsetY
    

    # throws Exception
    def gravity(self, velocityProperties: VelocityProperties, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition) -> None:
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            self.geographicMapBehavior.getCellTypeAt(geographicMapInterfaceArray, geographicMapCellTypeArray, geographicMapCellPosition)
            hasSolidBlock: bool = self.hasSolidBlock(geographicMapInterfaceArray, geographicMapCellTypeArray)
            if not hasSolidBlock:
                self.gravityUtil.process(velocityProperties, self.gravityUtil.GAME_GRAVITY_VELOCITY)
                velocityProperties.limitXYToForwardAndReverseMaxVelocity()
                self.gravity()
            else:
                pass
    

    # throws Exception
    def getPositionTopLeft(self, geographicMapInterfaceArray: list[BasicGeographicMap], layer: AllBinaryLayer, x: int, y: int) -> GeographicMapCellPosition:
        xCellPosition: int = layer.getXP() + -x
        yCellPosition: int = layer.getYP() + -y
        return geographicMapInterfaceArray[0].getCellPositionAtXYNoThrow(xCellPosition, yCellPosition)
    

    # throws Exception
    def getPositionTopRight(self, geographicMapInterfaceArray: list[BasicGeographicMap], layer: AllBinaryLayer, x: int, y: int) -> GeographicMapCellPosition:
        xCellPosition: int = layer.getXP() + -x + layer.getWidth()
        yCellPosition: int = layer.getYP() + -y
        return geographicMapInterfaceArray[0].getCellPositionAtXYNoThrow(xCellPosition, yCellPosition)
    

    # throws Exception
    def getPositionBottomLeft(self, geographicMapInterfaceArray: list[BasicGeographicMap], layer: AllBinaryLayer, x: int, y: int) -> GeographicMapCellPosition:
        xCellPosition: int = layer.getXP() + -x
        yCellPosition: int = layer.getYP() + -y + layer.getHeight()
        return geographicMapInterfaceArray[0].getCellPositionAtXYNoThrow(xCellPosition, yCellPosition)
    

    # throws Exception
    def getPositionBottomRight(self, geographicMapInterfaceArray: list[BasicGeographicMap], layer: AllBinaryLayer, x: int, y: int) -> GeographicMapCellPosition:
        xCellPosition: int = layer.getXP() + -x + layer.getWidth()
        yCellPosition: int = layer.getYP() + -y + layer.getHeight()
        return geographicMapInterfaceArray[0].getCellPositionAtXYNoThrow(xCellPosition, yCellPosition)
    

    # throws Exception
    def getLeftPosition(self, geographicMapInterfaceArray: list[BasicGeographicMap], layer: AllBinaryLayer) -> GeographicMapCellPosition:
        xCellPosition: int = layer.getXP()
        yCellPosition: int = layer.getYP() + layer.getHeight()
        return geographicMapInterfaceArray[0].getCellPositionAtXYNoThrow(xCellPosition, yCellPosition)
    

    # throws Exception
    def getRightPosition(self, geographicMapInterfaceArray: list[BasicGeographicMap], layer: AllBinaryLayer) -> GeographicMapCellPosition:
        xCellPosition: int = layer.getXP() + layer.getWidth()
        yCellPosition: int = layer.getYP() + layer.getHeight()
        return geographicMapInterfaceArray[0].getCellPositionAtXYNoThrow(xCellPosition, yCellPosition)
    

    # throws Exception
    def getGeographicMapCellPositionIfNotSolidBlockOrOffMapLocation(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer, x: int, y: int) -> GeographicMapCellPosition:
        geographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        topLeftGeographicMapCellPosition: GeographicMapCellPosition = self.getPositionTopLeft(geographicMapInterfaceArray, layer, x, y)
        geographicMapCellPosition = self.getGeographicMapCellPositionIfNotSolidBlockOrOffMap(geographicMapInterfaceArray, geographicMapCellTypeArray, topLeftGeographicMapCellPosition, velocityProperties, layer)
        if geographicMapCellPosition == SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        topRightGeographicMapCellPosition: GeographicMapCellPosition = self.getPositionTopRight(geographicMapInterfaceArray, layer, x, y)
        geographicMapCellPosition = self.getGeographicMapCellPositionIfNotSolidBlockOrOffMap(geographicMapInterfaceArray, geographicMapCellTypeArray, topRightGeographicMapCellPosition, velocityProperties, layer)
        if geographicMapCellPosition == SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        bottomLeftGeographicMapCellPosition: GeographicMapCellPosition = self.getPositionBottomLeft(geographicMapInterfaceArray, layer, x, y)
        geographicMapCellPosition = self.getGeographicMapCellPositionIfNotSolidBlockOrOffMap(geographicMapInterfaceArray, geographicMapCellTypeArray, bottomLeftGeographicMapCellPosition, velocityProperties, layer)
        if geographicMapCellPosition == SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        bottomRightGeographicMapCellPosition: GeographicMapCellPosition = self.getPositionBottomRight(geographicMapInterfaceArray, layer, x, y)
        geographicMapCellPosition = self.getGeographicMapCellPositionIfNotSolidBlockOrOffMap(geographicMapInterfaceArray, geographicMapCellTypeArray, bottomRightGeographicMapCellPosition, velocityProperties, layer)
        if geographicMapCellPosition == SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            pass
        else:
            pass
        return geographicMapCellPosition
    

    # throws Exception
    def getGeographicMapCellPositionIfNotSolidBlockOrOffMap(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition, velocityProperties: VelocityProperties, layer: AllBinaryLayer) -> GeographicMapCellPosition:
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            possibleStepGeographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPosition
            tiledLayer: AllBinaryTiledLayer = geographicMapInterfaceArray[0].getAllBinaryTiledLayer()
            if possibleStepGeographicMapCellPosition.getColumn() > 0 and possibleStepGeographicMapCellPosition.getRow() > 0 and possibleStepGeographicMapCellPosition.getColumn() < tiledLayer.getColumns() and possibleStepGeographicMapCellPosition.getRow() < tiledLayer.getRows():
                self.geographicMapBehavior.getCellTypeAt(geographicMapInterfaceArray, geographicMapCellTypeArray, possibleStepGeographicMapCellPosition)
                hasSolidBlock: bool = self.hasSolidBlock(geographicMapInterfaceArray, geographicMapCellTypeArray)
                hasOffMap: bool = self.isOffMap(geographicMapInterfaceArray, geographicMapCellTypeArray)
                if hasSolidBlock or hasOffMap:
                    self.previousGeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
                    return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
                else:
                    self.previousGeographicMapCellPosition = possibleStepGeographicMapCellPosition
                    return possibleStepGeographicMapCellPosition
        else:
            pass
        self.previousGeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    # throws Exception
    def moveAndLand(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition, velocityProperties: VelocityProperties, layer: AllBinaryLayer, x: int, y: int) -> None:
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            topViewCharacterInterface: TopViewCharacterInterface = (layer)
            topViewCharacterInterface.terrainMove(geographicMapInterfaceArray, geographicMapCellTypeArray, x, y)
        else:
            pass
    

    # throws Exception
    def move(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer, x: int, y: int) -> bool:
        geographicMapCellPosition: GeographicMapCellPosition = self.getGeographicMapCellPositionIfNotSolidBlockOrOffMapLocation(geographicMapInterfaceArray, geographicMapCellTypeArray, velocityProperties, layer, x, y)
        self.moveAndLand(geographicMapInterfaceArray, geographicMapCellTypeArray, geographicMapCellPosition, velocityProperties, layer, x, y)
        if geographicMapCellPosition == SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            return False
        else:
            return True
    

    # throws Exception
    def left(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer) -> None:
        geographicMapCellPosition: GeographicMapCellPosition = self.getLeftPosition(geographicMapInterfaceArray, layer)
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            possibleStepGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterfaceArray[0].getGeographicMapCellPositionFactory().getAt(geographicMapCellPosition.getColumn(), geographicMapCellPosition.getRow() - 1)
            self.geographicMapBehavior.getCellTypeAt(geographicMapInterfaceArray, geographicMapCellTypeArray, possibleStepGeographicMapCellPosition)
            hasSolidBlock: bool = self.hasSolidBlock(geographicMapInterfaceArray, geographicMapCellTypeArray)
            if hasSolidBlock:
                if self.autoStepBlocks:
                    topViewCharacterInterface: TopViewCharacterInterface = (layer)
                    topViewCharacterInterface.leftp()
                else:
                    velocityProperties.getVelocityXBasicDecimalP().setint(0)
            else:
                topViewCharacterInterface: TopViewCharacterInterface = (layer)
                topViewCharacterInterface.leftp()
    

    # throws Exception
    def right(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer) -> None:
        geographicMapCellPosition: GeographicMapCellPosition = self.getRightPosition(geographicMapInterfaceArray, layer)
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            possibleStepGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterfaceArray[0].getGeographicMapCellPositionFactory().getAt(geographicMapCellPosition.getColumn(), geographicMapCellPosition.getRow() - 1)
            self.geographicMapBehavior.getCellTypeAt(geographicMapInterfaceArray, geographicMapCellTypeArray, possibleStepGeographicMapCellPosition)
            hasSolidBlock: bool = self.hasSolidBlock(geographicMapInterfaceArray, geographicMapCellTypeArray)
            if hasSolidBlock:
                if self.autoStepBlocks:
                    topViewCharacterInterface: TopViewCharacterInterface = (layer)
                    topViewCharacterInterface.rightp()
                else:
                    velocityProperties.getVelocityXBasicDecimalP().setint(0)
            else:
                topViewCharacterInterface: TopViewCharacterInterface = (layer)
                topViewCharacterInterface.rightp()
from org.allbinary.media.graphics.geography.map.MultiGeographicMapBehavior import MultiGeographicMapBehavior
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.physics.acceleration.GravityUtil import GravityUtil
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory


