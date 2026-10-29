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

from org.allbinary.game.input.SelectRTSLayerVisitorFactoryInterface import SelectRTSLayerVisitorFactoryInterface


class SelectRTSLayerVisitorFactory(SelectRTSLayerVisitorFactoryInterface):
    instance: SelectRTSLayerVisitorFactory = None
    

    @staticmethod
    def getInstance() -> SelectRTSLayerVisitorFactory:
        return SelectRTSLayerVisitorFactory.instance
    

    def __init__(self) -> None:
        pass
    

    def create(self, selectedRTSLayersPlayerGameInput: SelectedRTSLayersPlayerGameInput) -> Visitor:
        from org.allbinary.game.input.SelectRTSLayerVisitor import SelectRTSLayerVisitor
        return SelectRTSLayerVisitor()
from org.allbinary.logic.util.visitor.Visitor import Visitor


SelectRTSLayerVisitorFactory.instance = SelectRTSLayerVisitorFactory()

