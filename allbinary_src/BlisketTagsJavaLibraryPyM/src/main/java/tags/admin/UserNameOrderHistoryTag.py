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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from tags.StoreValidationTransformTag import StoreValidationTransformTag


@java_inherited_overloads
class UserNameOrderHistoryTag(StoreValidationTransformTag):
    def _java_defaults(self):
        vars(self).setdefault("status", None)

    def _init_fields(self) -> None:
        if "status" not in vars(self): self.status: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def setStatus(self, value: str) -> None:
        self.status = value
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        try:
            self.setName("Range Order History View")
            self.setObjectFile("views.admin.orderhistory.UserNameOrderHistoryView")
            if self.getCommand() is not None:
                if self.getCommand().compareTo(GLOBALS2.VIEW) == 0:
                    pass
                else:
                    raise Exception("No Such View Command: " + str(self.getCommand()))
                return java_super_call(super(), "doStartTag")
            raise Exception("Command Null")
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.globals.GLOBALS2 import GLOBALS2


