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
# package admin.tags

from __future__ import annotations

from tags.CustomTagSupport import CustomTagSupport


class MultipartRequestParamForwardTag(CustomTagSupport):

    def _init_fields(self) -> None:
        self.page: str = None
        self.command: str = None
        self.paramVector: BasicArrayList = None

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setPage(self, page: str) -> None:
        self.page = page
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def setParamVector(self, paramVector: BasicArrayList) -> None:
        self.paramVector = paramVector
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from admin.tags.ParentInventoryTagHelper import ParentInventoryTagHelper
        from admin.tags.AbTagData import AbTagData
        try:
            parentTag: HelperTag = self.getParent()
            ParentInventoryTagHelper.getInstance().isValid(self, parentTag)
            hashMap: dict = StdUtil.getInstance().createHashMap()
            hashMap.put(AbTagData.PARENT, parentTag)
            multipartRequestParamForwardHelper: MultipartRequestParamForwardHelper = MultipartRequestParamForwardHelper(parentTag, self.page, self.command, self.paramVector, self.pageContext)
            multipartRequestParamForwardHelper.forward()
            return Tag.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return Tag.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return Tag.SKIP_BODY
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.tagext.Tag import Tag
from admin.taghelpers.MultipartRequestParamForwardHelper import MultipartRequestParamForwardHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from tags.HelperTag import HelperTag


