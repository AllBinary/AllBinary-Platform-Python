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
# package tags.generic.user

from __future__ import annotations

from tags.StoreValidationTransformTag import StoreValidationTransformTag


class UsersTag(StoreValidationTransformTag):

    def _init_fields(self) -> None:
        self.role: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setRole(self, value: str) -> None:
        self.role = value
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            self.setName("Generic Users View")
            self.setObjectFile("views.generic.user.UsersValidationView")
            if self.getCommand() is not None:
                self.getPropertiesHashMap().put(UserRoleData.NAME, self.role)
                if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.VIEW) == 0:
                    pass
                else:
                    raise Exception("No Such View Command: " + str(self.getCommand()))
                return super().doStartTag()
            raise Exception("Command Null")
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
from org.allbinary.business.user.role.UserRoleData import UserRoleData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler


