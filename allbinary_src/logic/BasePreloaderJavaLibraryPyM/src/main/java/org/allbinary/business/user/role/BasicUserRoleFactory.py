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
# package org.allbinary.business.user.role

from __future__ import annotations



class BasicUserRoleFactory:
    instance: BasicUserRoleFactory = None

    def _init_fields(self) -> None:
        self.INACTIVITYTIMEOUT: int = 360000000
        self.CUSTOMERTIMEOUT: int = 360000000
        self.CUSTOMERMAXSESSIONTIME: int = 360000000
        self.MAXSESSIONTIME: int = 360000000
        self.INSTALLER: BasicUserRole = BasicUserRole("Installer", 16, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.ADMINISTRATOR: BasicUserRole = BasicUserRole("Administrator", 0, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.CUSTOMER: BasicUserRole = BasicUserRole("CustomerUser", "Customer User", 1, self.CUSTOMERTIMEOUT, self.CUSTOMERMAXSESSIONTIME)
        self.SUBSCRIBERCUSTOMER: BasicUserRole = BasicUserRole("SubscriberUser", "Subscriber User", 2, self.CUSTOMERTIMEOUT, self.CUSTOMERMAXSESSIONTIME)
        self.WHOLESALECUSTOMER: BasicUserRole = BasicUserRole("WholesaleUser", "Wholesale User", 3, self.CUSTOMERTIMEOUT, self.CUSTOMERMAXSESSIONTIME)
        self.STOREMANAGER: BasicUserRole = BasicUserRole("StoreManager", "Store Manager", 4, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.PRODUCTMANAGER: BasicUserRole = BasicUserRole("ProductManager", "Product Manager", 5, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.CUSTOMERMANAGER: BasicUserRole = BasicUserRole("UserManager", "User Manager", 6, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.PAYMENTMANAGER: BasicUserRole = BasicUserRole("PaymentManager", "Payment Manager", 7, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.ORDERMANAGER: BasicUserRole = BasicUserRole("OrderManager", "Order Manager", 8, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.WEBMANAGER: BasicUserRole = BasicUserRole("WebManager", "Web Manager", 9, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.REVIEWER: BasicUserRole = BasicUserRole("Reviewer", 10, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.SHIPPING: BasicUserRole = BasicUserRole("Shipping", 11, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.ADJUSTER: BasicUserRole = BasicUserRole("Adjuster", 12, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.WORKFLOWEDITOR: BasicUserRole = BasicUserRole("WorkFlowEditor", "WorkFlow Editor", 13, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.WIZARD: BasicUserRole = BasicUserRole("WizardUser", "Wizard User", 14, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)
        self.VIEWEDITOR: BasicUserRole = BasicUserRole("ViewEditor", "View Editor", 15, self.MAXSESSIONTIME, self.INACTIVITYTIMEOUT)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicUserRoleFactory:
        return BasicUserRoleFactory.instance
from org.allbinary.business.user.role.BasicUserRole import BasicUserRole


BasicUserRoleFactory.instance = BasicUserRoleFactory()

