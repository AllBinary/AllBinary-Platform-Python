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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from admin.tags.TableTag import TableTag


@java_inherited_overloads
class InventoryTag(TableTag):
    def _java_defaults(self):
        vars(self).setdefault("storeName", None)

    def _init_fields(self) -> None:
        if "storeName" not in vars(self): self.storeName: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.InventoryHelperFactory import InventoryHelperFactory
        from admin.taghelpers.InventoryRequestHelperFactory import InventoryRequestHelperFactory
        super().__init__()
        __class__._init_fields(self)
        self.setTagHelperFactory(InventoryHelperFactory())
        self.setTagRequestHelperFactory(InventoryRequestHelperFactory())
    

    def setStoreName(self, value: str) -> None:
        self.storeName = value
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from admin.tags.ParentInventoryTagHelper import ParentInventoryTagHelper
        from admin.tags.AbTagData import AbTagData
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        try:
            if java_predicate(self, "isEnabled"):
                if self.getCommand() is not None:
                    if self.getCommand().compareTo(GLOBALS2.BACKUP) != 0 and self.getCommand().compareTo(GLOBALS2.RESTORE) != 0 and self.getCommand().compareTo(self.commonStrings.CREATE) != 0 and self.getCommand().compareTo(self.commonStrings.DROP) != 0:
                        parentTag: Tag = self.getParent()
                        ParentInventoryTagHelper.getInstance().isValid(self, parentTag)
                        self.getPropertiesHashMap().put(AbTagData.PARENT, parentTag)
                        self.getPropertiesHashMap().put(StoreFrontData.getInstance().NAME, self.storeName)
                    return java_super_call(super(), "doStartTag")
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.tagext.Tag import Tag
# from admin.taghelpers.InventoryHelperFactory import InventoryHelperFactory
# from admin.taghelpers.InventoryRequestHelperFactory import InventoryRequestHelperFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.globals.GLOBALS2 import GLOBALS2


