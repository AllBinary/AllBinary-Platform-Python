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
# package tags.admin

from __future__ import annotations

from tags.StoreValidationTransformTag import StoreValidationTransformTag


class UserTag(StoreValidationTransformTag):

    def _init_fields(self) -> None:
        self.role: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setRole(self, value: str) -> None:
        self.role = value
        self.getPropertiesHashMap().put(UserRoleData.NAME, self.role)
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.getCommand() is not None:
                if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.NEW) == 0:
                    self.setName("New User View")
                    self.setObjectFile("views.admin.user.NewUserView")
                elif self.getCommand().compareTo(self.commonStrings.INSERT) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().INSERT_INTO) == 0:
                    self.setName("Add Validation User View")
                    self.setObjectFile("views.admin.user.AddValidationUserView")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.VIEW) == 0:
                    self.setName("Validation User View")
                    self.setObjectFile("views.admin.user.ViewValidationUserView")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.EDIT) == 0:
                    self.setName("Validation User View")
                    self.setObjectFile("views.admin.user.EditValidationUserView")
                elif self.getCommand().compareTo(self.commonStrings.UPDATE) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().UPDATE) == 0:
                    self.setName("Update Validation User View")
                    self.setObjectFile("views.admin.user.UpdateValidationUserView")
                elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                    self.setName("Delete Validation User View")
                    self.setObjectFile("views.admin.user.DeleteValidationUserView")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.BACKUP) == 0:
                    raise Exception("View not implemented")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.RESTORE) == 0:
                    raise Exception("View not implemented")
                elif self.getCommand().compareTo(self.commonStrings.DROP) == 0:
                    raise Exception("View not implemented")
                elif self.getCommand().compareTo(self.commonStrings.CREATE) == 0:
                    raise Exception("View not implemented")
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
from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings


