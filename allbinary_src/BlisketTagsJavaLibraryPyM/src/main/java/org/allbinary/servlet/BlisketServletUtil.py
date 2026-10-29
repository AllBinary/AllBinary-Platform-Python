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



class BlisketServletUtil:
    instance: BlisketServletUtil = None
    

    @staticmethod
    def getInstance() -> BlisketServletUtil:
        return BlisketServletUtil.instance
    

    def init(self, request: HttpServletRequest) -> None:
        urlGlobals: AppUrlGlobals = AppUrlGlobals()
        urlGlobals.setWebappPath(request.getServletContext().getRealPath(AbPathData.getInstance().SEPARATOR))
        self.URLGLOBALS.init(urlGlobals)
        WebappClassLoaderInfo.setLoader(type(self).getClassLoader())
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo


BlisketServletUtil.instance = BlisketServletUtil()

