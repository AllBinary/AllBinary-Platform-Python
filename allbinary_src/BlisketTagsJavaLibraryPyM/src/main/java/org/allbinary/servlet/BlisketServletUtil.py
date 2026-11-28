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
# package org.allbinary.servlet

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class BlisketServletUtil:
    instance: BlisketServletUtil = None
    

    @staticmethod
    def getInstance() -> BlisketServletUtil:
        return BlisketServletUtil.instance
    

    def init(self, request: HttpServletRequest) -> None:
        from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo
        urlGlobals: AppUrlGlobals = AppUrlGlobals()
        urlGlobals.setWebappPath(request.getServletContext().getRealPath(AbPathData.getInstance().SEPARATOR))
        URLGLOBALS.init(urlGlobals)
        WebappClassLoaderInfo.setLoader(__import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.getSystemClassLoader())
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo


def _BlisketServletUtil_instance() -> object:
    return BlisketServletUtil()

lazy_static(BlisketServletUtil, "instance", _BlisketServletUtil_instance)

