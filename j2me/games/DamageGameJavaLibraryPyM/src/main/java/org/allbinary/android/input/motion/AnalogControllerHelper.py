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
# package org.allbinary.android.input.motion

from __future__ import annotations



class AnalogControllerHelper:

    def _init_fields(self) -> None:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.reduceTimeFactor: int = None
        self.SCALE_VALUE: int = AnalogControllerConfigurationFactory.getInstance().SCALE_VALUE
        self.rightTimeElapsedHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.leftTimeElapsedHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.downTimeElapsedHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.upTimeElapsedHelper: TimeDelayHelper = TimeDelayHelper(0)
    

    def __init__(self, reduceTimeFactor: int) -> None:
        self._init_fields()
        self.reduceTimeFactor = reduceTimeFactor
    

    # throws Exception
    def right(self, collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer, xAnalogValue: int) -> None:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        self.rightTimeElapsedHelper.delay = ((self.SCALE_VALUE - xAnalogValue) >> self.reduceTimeFactor)
        if self.rightTimeElapsedHelper.isTimeTNT():
            collidableDestroyableDamageableLayer.right()
    

    # throws Exception
    def left(self, collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer, xAnalogValue: int) -> None:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        self.leftTimeElapsedHelper.delay = ((self.SCALE_VALUE + xAnalogValue) >> self.reduceTimeFactor)
        if self.leftTimeElapsedHelper.isTimeTNT():
            collidableDestroyableDamageableLayer.left()
    

    # throws Exception
    def up(self, collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer, xAnalogValue: int) -> None:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        self.upTimeElapsedHelper.delay = ((self.SCALE_VALUE - xAnalogValue) >> self.reduceTimeFactor)
        if self.upTimeElapsedHelper.isTimeTNT():
            collidableDestroyableDamageableLayer.up()
    

    # throws Exception
    def down(self, collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer, xAnalogValue: int) -> None:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        self.downTimeElapsedHelper.delay = ((self.SCALE_VALUE + xAnalogValue) >> self.reduceTimeFactor)
        if self.downTimeElapsedHelper.isTimeTNT():
            collidableDestroyableDamageableLayer.down()
# from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.android.input.motion.AnalogControllerConfigurationFactory import AnalogControllerConfigurationFactory


