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
# package org.allbinary

from __future__ import annotations



class PostGameCommandFactory:
    instance: PostGameCommandFactory = None
    

    @staticmethod
    def getInstance() -> PostGameCommandFactory:
        return PostGameCommandFactory.instance
    

    def addCommands(self, canvas: MyCanvas) -> None:
        MultiPlayerGameFeatureFactory.getInstance().addCommands(canvas)
from org.allbinary.game.configuration.feature.MultiPlayerGameFeatureFactory import MultiPlayerGameFeatureFactory
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas


PostGameCommandFactory.instance = PostGameCommandFactory()

