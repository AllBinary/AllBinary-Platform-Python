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
# package org.allbinary.logic.visual.dhtml.html.head.meta

from __future__ import annotations



class HtmlMetaAttributeDataFactory:
    instance: HtmlMetaAttributeDataFactory = None

    def _init_fields(self) -> None:
        self.NAME: HtmlMetaAttributeData = HtmlMetaAttributeData(0, "HTMLMETA_ATTRIBUTE_NAME")
        self.HTTP_EQUIV: HtmlMetaAttributeData = HtmlMetaAttributeData(1, "HTMLMETA_ATTRIBUTE_HTTPEQUIV")
        self.CONTENT: HtmlMetaAttributeData = HtmlMetaAttributeData(2, "HTMLMETA_ATTRIBUTE_CONTENT")
    

    @staticmethod
    def getInstance() -> HtmlMetaAttributeDataFactory:
        return HtmlMetaAttributeDataFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.logic.visual.dhtml.html.head.meta.HtmlMetaAttributeData import HtmlMetaAttributeData


HtmlMetaAttributeDataFactory.instance = HtmlMetaAttributeDataFactory()

