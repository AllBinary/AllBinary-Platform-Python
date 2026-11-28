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
# package org.allbinary.globals

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import threading
from org.allbinary.globals.UrlGlobalsInterface import UrlGlobalsInterface


@java_inherited_overloads
class WebAppUrlGlobals(UrlGlobalsInterface):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("path", None)
        vars(self).setdefault("isWebappPathSet", False)

    def _init_fields(self) -> None:
        if "path" not in vars(self): self.path: str = None
        self.isWebappPathSet: bool = False

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def isTestingMode(self) -> bool:
        from org.allbinary.business.init.InitInfo import InitInfo
        return java_predicate(InitInfo.getInstance(), "isTesting")
    

    def getWebappPath(self) -> str:
        return self.path
    

    def setWebappPath(self, path: str) -> None:
        with self._lock:
            return __class__.__dict__["_setWebappPath_unlocked"].__get__(self, __class__)(path)

    def _setWebappPath_unlocked(self, path: str) -> None:
        path = path
        self.isWebappPathSet = True
    

    def getTestHtmlPath(self) -> str:
        from org.allbinary.business.init.InitInfo import InitInfo
        return InitInfo.getInstance().getTestHtmlPath()
    

    # throws Exception
    def getMainPath(self) -> str:
        from org.allbinary.business.init.InitInfo import InitInfo
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        mainPath: str = InitInfo.getInstance().getMainPath()
        if not (StringValidationUtil.getInstance().isEmpty(mainPath)):
            return mainPath
        elif self.isWebappPathSet:
            return self.getWebappPath()
        else:
            raise Exception("Webapp Path is not set")
# from org.allbinary.business.init.InitInfo import InitInfo
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


