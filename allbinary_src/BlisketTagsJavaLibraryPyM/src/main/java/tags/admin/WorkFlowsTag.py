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


class WorkFlowsTag(StoreValidationTransformTag):
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.getCommand() is not None:
                if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.NEW) == 0:
                    self.setName("New WorkFlow View")
                    self.setObjectFile("views.admin.workflow.NewView")
                elif self.getCommand().compareTo(self.commonStrings.INSERT) == 0:
                    self.setName("Add Validation WorkFlow View")
                    self.setObjectFile("views.admin.workflow.AddValidationView")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.VIEW) == 0:
                    self.setName("Validation WorkFlow View")
                    self.setObjectFile("views.admin.workflow.WorkflowsValidationView")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.EDIT) == 0:
                    self.setName("Validation WorkFlow View")
                    self.setObjectFile("views.admin.workflow.EditValidationView")
                elif self.getCommand().compareTo(self.commonStrings.UPDATE) == 0:
                    self.setName("Update Validation WorkFlow View")
                    self.setObjectFile("views.admin.workflow.UpdateValidationView")
                elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                    self.setName("Delete Validation WorkFlow View")
                    self.setObjectFile("views.admin.workflow.DeleteValidationView")
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
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler


