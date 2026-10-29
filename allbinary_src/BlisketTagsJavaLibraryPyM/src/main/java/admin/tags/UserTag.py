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

from admin.tags.TableTag import TableTag


class UserTag(TableTag):

    def _init_fields(self) -> None:
        self.role: str = None
        self.enable: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.setTagHelperFactory(UserHelperFactory())
        self.setTagRequestHelperFactory(UserHelperFactory())
    

    def setRole(self, value: str) -> None:
        self.role = value
        self.getPropertiesHashMap().put(UserRoleData.NAME, self.role)
    

    def setEnable(self, value: str) -> None:
        self.enable = value
        self.getPropertiesHashMap().put(EntryData.getInstance().ENABLE, self.enable)
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.isEnabled():
                return super().doStartTag()
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.UserHelperFactory import UserHelperFactory
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.role.UserRoleData import UserRoleData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler


