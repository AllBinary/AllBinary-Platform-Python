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
# package tags.generic.payment

from __future__ import annotations

from tags.StoreValidationTransformTag import StoreValidationTransformTag


class PaymentTag(StoreValidationTransformTag):
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            self.setName("Basic Payment View")
            self.setObjectFile("views.generic.payment.ValidationView")
            if self.getCommand() is not None:
                if self.getCommand().compareTo(PaymentData.VIEW) == 0 or self.getCommand().compareTo(PaymentData.CHANGE) == 0 or self.getCommand().compareTo(PaymentData.ADDNEW) == 0:
                    pass
                elif self.getCommand().compareTo(self.commonStrings.INSERT) == 0:
                    pass
                elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                    return self.EVAL_BODY_INCLUDE
                elif self.getCommand().compareTo(PaymentData.SELECT) == 0:
                    return self.EVAL_BODY_INCLUDE
                else:
                    raise Exception("No Such View Command: " + str(self.getCommand()))
                return super().doStartTag()
            raise Exception("Command Null")
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


