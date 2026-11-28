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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.input.RTSLayerFormFactory import RTSLayerFormFactory


@java_inherited_overloads
class AdvancedRTSLayerFormFactory(RTSLayerFormFactory):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("scrollSelectionForm", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "scrollSelectionForm" not in vars(self): self.scrollSelectionForm: ScrollSelectionForm = None
    

    def __init__(self, label: str, itemArrayFactoryInterface: ItemArraySingletonFactoryInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.layer.RTSScrollSelectionFormFactory import RTSScrollSelectionFormFactory
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
        from org.allbinary.graphics.form.item.ItemArraySingletonFactoryInterface import ItemArraySingletonFactoryInterface
        super().__init__()
        __class__._init_fields(self)
        scrollSelectionForm: ScrollSelectionForm = ScrollSelectionForm.getNullScrollSelectionForm()
        try:
            items: list[ABCustomItem] = itemArrayFactoryInterface.getItems()
            scrollSelectionForm = RTSScrollSelectionFormFactory.getInstance(label, items)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
        self.scrollSelectionForm = scrollSelectionForm
    

    def getInstance(self, rtsLayer: RTSLayer) -> ScrollSelectionForm:
        from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
        return self.scrollSelectionForm
# from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
# from org.allbinary.graphics.form.item.ItemArraySingletonFactoryInterface import ItemArraySingletonFactoryInterface


