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


class ScreenCaptureFactory:
    instance: ScreenCapture = None
    

    @staticmethod
    def getInstance() -> ScreenCapture:
        return ScreenCaptureFactory.instance


def _ScreenCaptureFactory_instance() -> object:
    from org.allbinary.graphics.ScreenCaptureNoneFactory import ScreenCaptureNoneFactory
    return ScreenCaptureNoneFactory.getInstance()

lazy_static(ScreenCaptureFactory, "instance", _ScreenCaptureFactory_instance)

