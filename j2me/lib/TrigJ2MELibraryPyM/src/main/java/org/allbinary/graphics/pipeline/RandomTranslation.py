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
# package org.allbinary.graphics.pipeline

from __future__ import annotations



class RandomTranslation:
    

    # throws Exception
    @staticmethod
    def getInstance(vector: BasicArrayList, howMuch: int) -> BasicArrayList:
        from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
        myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()
        x: int = -myRandomFactory.getNextInt(howMuch)
        y: int = myRandomFactory.getNextInt(howMuch)
        graphicsPipe: BasicGraphicsPipeline = BasicGraphicsPipeline(vector)
        graphicsPipe.createMatrix()
        graphicsPipe.translate(x, y)
        return graphicsPipe.getMatrix()
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.util.BasicArrayList import BasicArrayList


