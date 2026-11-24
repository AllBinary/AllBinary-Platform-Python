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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface


class TagHelperFactory(TagHelperFactoryInterface):

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception, LicensingException
    def getInstance(self, hashMap: HashMap, pageContext: PageContext) -> object:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        raise RuntimeError()
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.string.CommonStrings import CommonStrings


