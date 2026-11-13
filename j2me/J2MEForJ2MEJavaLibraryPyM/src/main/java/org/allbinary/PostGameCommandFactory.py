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

from java.lang.JavaRuntimeStatic import lazy_static


class PostGameCommandFactory:
    instance: PostGameCommandFactory = None
    

    @staticmethod
    def getInstance() -> PostGameCommandFactory:
        return PostGameCommandFactory.instance
    

    def addCommands(self, canvas: MyCanvas) -> None:
        from org.allbinary.game.configuration.feature.MultiPlayerGameFeatureFactory import MultiPlayerGameFeatureFactory
        from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
        MultiPlayerGameFeatureFactory.getInstance().addCommands(canvas)
# from org.allbinary.game.configuration.feature.MultiPlayerGameFeatureFactory import MultiPlayerGameFeatureFactory
# from org.allbinary.graphics.displayable.MyCanvas import MyCanvas


def _PostGameCommandFactory_instance() -> object:
    return PostGameCommandFactory()

lazy_static(PostGameCommandFactory, "instance", _PostGameCommandFactory_instance)

