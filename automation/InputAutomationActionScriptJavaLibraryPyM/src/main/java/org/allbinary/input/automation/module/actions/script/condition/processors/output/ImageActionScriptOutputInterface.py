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
# package org.allbinary.input.automation.module.actions.script.condition.processors.output

from __future__ import annotations

from org.allbinary.input.automation.module.actions.script.condition.processors.output.ProfileActionScriptOutputInterface import ProfileActionScriptOutputInterface


# Java interface
class ImageActionScriptOutputInterface(ProfileActionScriptOutputInterface):
    

    def getImageTypes(self) -> ImageTypes:
        raise NotImplementedError()
    

    def setImageTypes(self, imageTypes: ImageTypes) -> None:
        raise NotImplementedError()
    

    def isSaved(self) -> bool:
        raise NotImplementedError()
    

    def setSaved(self, saved: bool) -> None:
        raise NotImplementedError()
    

    def isDisplay(self) -> bool:
        raise NotImplementedError()
    

    def setDisplay(self, display: bool) -> None:
        raise NotImplementedError()
    

    def log(self) -> None:
        raise NotImplementedError()


