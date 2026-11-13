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


class DisposalUtil:
    instance: DisposalUtil = None
    

    @staticmethod
    def getInstance() -> DisposalUtil:
        return DisposalUtil.instance
    

    def disposeImage(self, image: Image) -> None:
        from javax.microedition.lcdui.Image import Image
        pass
    

    def disposeResource(self, resource: Resource) -> None:
        from org.eclipse.swt.graphics.Resource import Resource
        if not resource.isDisposed():
            resource.dispose()
# from javax.microedition.lcdui.Image import Image
# from org.eclipse.swt.graphics.Resource import Resource


def _DisposalUtil_instance() -> object:
    return DisposalUtil()

lazy_static(DisposalUtil, "instance", _DisposalUtil_instance)

