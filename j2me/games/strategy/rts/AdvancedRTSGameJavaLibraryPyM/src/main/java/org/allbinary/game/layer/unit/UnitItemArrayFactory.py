# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.unit

from __future__ import annotations

from org.allbinary.graphics.form.item.CustomItemUtil import CustomItemUtil
from org.allbinary.graphics.form.item.ItemArraySingletonFactoryInterface import ItemArraySingletonFactoryInterface


class UnitItemArrayFactory(ItemArraySingletonFactoryInterface):
    ITEMS: list[ABCustomItem] = CustomItemUtil.getInstance().CUSTOM_ITEM_ARRAY

    def _init_fields(self) -> None:
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
        self.resources: list[BasicGameResources] = None
    

    def __init__(self, resources: list[BasicGameResources]) -> None:
        self._init_fields()
        self.resources = resources
    

    # throws Exception
    def createFlagItem(self, flagResources: FlagGameResources, layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface) -> ABCustomItem:
        name: str = flagResources.NAME
        index: int = name.find(self.commonSeps.SPACE)
        if index >= 0:
            name = name[index:]
        return self.createNamedFlagItem(flagResources, name, layerInterfaceFactoryInterface)
    

    # throws Exception
    def createNamedFlagItem(self, flagResources: FlagGameResources, name: str, layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface) -> ABCustomItem:
        from org.allbinary.game.layer.unit.IMAGE_CACHE import IMAGE_CACHE
        IMAGE_CACHE: ImageCache = GameFeatureImageCacheFactory.getInstance()
        image: Image = IMAGE_CACHE.getWithKey(flagResources.RESOURCE_ICON)
        item: ABCustomItem = LayerInterfaceFactoryImageItem(name, image, ImageItem.LAYOUT_DEFAULT, flagResources.NAME, self.basicColor, [RTSLayerTextAnimation(RTSGameStrings.getInstance().DRAGGABLE, image)], layerInterfaceFactoryInterface)
        return item
    

    # throws Exception
    def getItems(self) -> list[ABCustomItem]:
        return UnitItemArrayFactory.ITEMS
    

    def getResources(self) -> list[BasicGameResources]:
        return self.resources
    

    def indexOf(self, basicGameResources: BasicGameResources) -> int:
        for index in range(len(self.resources) - 1, 0 - 1, -1):
            if self.resources[index] == basicGameResources:
                return index
        return -1
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.ImageItem import ImageItem
from org.allbinary.game.layer.RTSGameStrings import RTSGameStrings
from org.allbinary.game.layer.item.LayerInterfaceFactoryImageItem import LayerInterfaceFactoryImageItem
from org.allbinary.game.layer.item.RTSLayerTextAnimation import RTSLayerTextAnimation
from org.allbinary.game.layer.resources.BasicGameResources import BasicGameResources
from org.allbinary.game.layer.waypoint.FlagGameResources import FlagGameResources
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface


