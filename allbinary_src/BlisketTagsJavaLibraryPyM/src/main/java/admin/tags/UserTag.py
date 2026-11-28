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
class UserTag(TableTag):
    def _java_defaults(self):
        vars(self).setdefault("role", None)
        vars(self).setdefault("enable", None)

    def _init_fields(self) -> None:
        if "role" not in vars(self): self.role: str = None
        if "enable" not in vars(self): self.enable: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.UserHelperFactory import UserHelperFactory
        super().__init__()
        __class__._init_fields(self)
        self.setTagHelperFactory(UserHelperFactory())
        self.setTagRequestHelperFactory(UserHelperFactory())
    

    def setRole(self, value: str) -> None:
        from org.allbinary.business.user.role.UserRoleData import UserRoleData
        self.role = value
        self.getPropertiesHashMap().put(UserRoleData.NAME, self.role)
    

    def setEnable(self, value: str) -> None:
        from org.allbinary.business.entry.EntryData import EntryData
        self.enable = value
        self.getPropertiesHashMap().put(EntryData.getInstance().ENABLE, self.enable)
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        try:
            if java_predicate(self, "isEnabled"):
                return java_super_call(super(), "doStartTag")
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
# from admin.taghelpers.UserHelperFactory import UserHelperFactory
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.role.UserRoleData import UserRoleData
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler


