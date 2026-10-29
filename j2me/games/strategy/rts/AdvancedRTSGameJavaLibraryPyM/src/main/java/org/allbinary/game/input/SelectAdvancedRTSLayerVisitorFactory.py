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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.game.input.SelectRTSLayerVisitorFactoryInterface import SelectRTSLayerVisitorFactoryInterface


class SelectAdvancedRTSLayerVisitorFactory(SelectRTSLayerVisitorFactoryInterface):
    instance: SelectAdvancedRTSLayerVisitorFactory = None
    

    @staticmethod
    def getInstance() -> SelectAdvancedRTSLayerVisitorFactory:
        return SelectAdvancedRTSLayerVisitorFactory.instance
    

    def __init__(self) -> None:
        pass
    

    def create(self, selectedRTSLayersPlayerGameInput: SelectedRTSLayersPlayerGameInput) -> Visitor:
        from org.allbinary.game.input.SelectAdvancedRTSLayerVisitor import SelectAdvancedRTSLayerVisitor
        return SelectAdvancedRTSLayerVisitor(selectedRTSLayersPlayerGameInput)
from org.allbinary.logic.util.visitor.Visitor import Visitor


SelectAdvancedRTSLayerVisitorFactory.instance = SelectAdvancedRTSLayerVisitorFactory()

