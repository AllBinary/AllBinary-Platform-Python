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
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ScreenCaptureNoneFactory:
    instance: ScreenCapture = None
    

    @staticmethod
    def getInstance() -> ScreenCapture:
        return ScreenCaptureNoneFactory.instance


def _ScreenCaptureNoneFactory_instance() -> object:
    from org.allbinary.graphics.ScreenCapture import ScreenCapture
    return ScreenCapture()

lazy_static(ScreenCaptureNoneFactory, "instance", _ScreenCaptureNoneFactory_instance)

