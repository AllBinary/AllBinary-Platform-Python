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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from tags.CustomTagSupport import CustomTagSupport


@java_inherited_overloads
class MultipartRequestParamForwardTag(CustomTagSupport):
    def _java_defaults(self):
        vars(self).setdefault("page", None)
        vars(self).setdefault("command", None)
        vars(self).setdefault("paramVector", None)

    def _init_fields(self) -> None:
        if "page" not in vars(self): self.page: str = None
        if "command" not in vars(self): self.command: str = None
        if "paramVector" not in vars(self): self.paramVector: BasicArrayList = None

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def setPage(self, page: str) -> None:
        self.page = page
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def setParamVector(self, paramVector: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.paramVector = paramVector
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from admin.tags.ParentInventoryTagHelper import ParentInventoryTagHelper
        from admin.tags.AbTagData import AbTagData
        from java.util.HashMap import HashMap
        from admin.taghelpers.MultipartRequestParamForwardHelper import MultipartRequestParamForwardHelper
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from tags.HelperTag import HelperTag
        try:
            parentTag: HelperTag = self.getParent()
            ParentInventoryTagHelper.getInstance().isValid(self, parentTag)
            hashMap: HashMap = StdUtil.getInstance().createHashMap()
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
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.tagext.Tag import Tag
# from admin.taghelpers.MultipartRequestParamForwardHelper import MultipartRequestParamForwardHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from tags.HelperTag import HelperTag


