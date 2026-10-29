# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.game.midlet

from __future__ import annotations



class LicenseCheckRunnableFactory:
    

    def getInstance(self, specialDemoGameMidlet: SpecialDemoGameMidlet) -> ABRunnable:
        return NullABRunnable.getInstance()
from org.allbinary.thread.ABRunnable import ABRunnable
from org.allbinary.thread.NullABRunnable import NullABRunnable


