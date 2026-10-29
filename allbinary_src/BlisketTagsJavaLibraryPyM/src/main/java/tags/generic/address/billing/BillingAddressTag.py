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
# package tags.generic.address.billing

from __future__ import annotations

from tags.StoreValidationTransformTag import StoreValidationTransformTag


class BillingAddressTag(StoreValidationTransformTag):
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.getCommand() is not None:
                if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.VIEW) == 0:
                    self.setName("Basic Billing Address View")
                    self.setObjectFile("views.generic.address.billing.ValidationView")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.EDIT) == 0:
                    self.setName("Basic Billing Address View")
                    self.setObjectFile("views.generic.address.billing.EditValidationView")
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.NEW) == 0:
                    self.setName("Basic Billing Address View")
                    self.setObjectFile("views.generic.address.billing.NewValidationView")
                elif self.getCommand().compareTo(self.commonStrings.INSERT) == 0:
                    self.setName("Basic Billing Address View")
                    self.setObjectFile("views.generic.address.billing.AddValidationView")
                elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                    self.setName("Basic Billing Address View")
                    self.setObjectFile("views.generic.address.billing.DeleteValidationView")
                elif self.getCommand().compareTo(BillingAddressData.SELECT) == 0:
                    self.setName("Basic Billing Address View")
                    self.setObjectFile("views.generic.address.billing.SelectValidationView")
                elif self.getCommand().compareTo(BillingAddressData.SETTOSHIPPINGADDRESS) == 0:
                    self.setName("Basic Billing Address View")
                    self.setObjectFile("views.generic.address.billing.SetValidationView")
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
from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


