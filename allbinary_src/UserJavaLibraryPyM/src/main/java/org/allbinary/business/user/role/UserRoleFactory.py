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



class UserRoleFactory:
    instance: UserRoleFactory = None

    def _init_fields(self) -> None:
        self.basicUserRoleFactory: BasicUserRoleFactory = BasicUserRoleFactory.getInstance()
        self.INSTALLER: UserRole = UserRoleB(self.basicUserRoleFactory.INSTALLER, None)
        self.ADMINISTRATOR: UserRole = UserRoleB(self.basicUserRoleFactory.ADMINISTRATOR, AdminUserFactory())
        self.CUSTOMER: UserRole = UserRoleB(self.basicUserRoleFactory.CUSTOMER, UserFactory())
        self.SUBSCRIBERCUSTOMER: UserRole = UserRoleB(self.basicUserRoleFactory.SUBSCRIBERCUSTOMER, SubscriberUserFactory())
        self.WHOLESALECUSTOMER: UserRole = UserRoleB(self.basicUserRoleFactory.WHOLESALECUSTOMER, WholesaleUserFactory())
        self.STOREMANAGER: UserRole = UserRoleB(self.basicUserRoleFactory.STOREMANAGER, StoreAdminUserFactory())
        self.PRODUCTMANAGER: UserRole = UserRoleB(self.basicUserRoleFactory.PRODUCTMANAGER, ProductStoreAdminUserFactory())
        self.CUSTOMERMANAGER: UserRole = UserRoleB(self.basicUserRoleFactory.CUSTOMERMANAGER, CustomerStoreAdminUserFactory())
        self.PAYMENTMANAGER: UserRole = UserRoleB(self.basicUserRoleFactory.PAYMENTMANAGER, PaymentStoreAdminUserFactory())
        self.ORDERMANAGER: UserRole = UserRoleB(self.basicUserRoleFactory.ORDERMANAGER, OrderStoreAdminUserFactory())
        self.WEBMANAGER: UserRole = UserRoleB(self.basicUserRoleFactory.WEBMANAGER, WebStoreAdminUserFactory())
        self.REVIEWER: UserRole = UserRoleB(self.basicUserRoleFactory.REVIEWER, ReviewOrderStoreAdminUserFactory())
        self.SHIPPING: UserRole = UserRoleB(self.basicUserRoleFactory.SHIPPING, ShipOrderStoreAdminUserFactory())
        self.ADJUSTER: UserRole = UserRoleB(self.basicUserRoleFactory.ADJUSTER, AdjustOrderStoreAdminUserFactory())
        self.WORKFLOWEDITOR: UserRole = UserRoleB(self.basicUserRoleFactory.WORKFLOWEDITOR, WorkflowEditorWebStoreAdminUserFactory())
        self.WIZARD: UserRole = UserRoleB(self.basicUserRoleFactory.WIZARD, WizardWebStoreAdminUserFactory())
        self.VIEWEDITOR: UserRole = UserRoleB(self.basicUserRoleFactory.VIEWEDITOR, ViewEditorWebStoreAdminUserFactory())

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> UserRoleFactory:
        return UserRoleFactory.instance
from org.allbinary.business.user.modules.UserFactory import UserFactory
from org.allbinary.business.user.modules.admin.AdminUserFactory import AdminUserFactory
from org.allbinary.business.user.modules.admin.store.StoreAdminUserFactory import StoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.customer.CustomerStoreAdminUserFactory import CustomerStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.order.OrderStoreAdminUserFactory import OrderStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.order.adjust.AdjustOrderStoreAdminUserFactory import AdjustOrderStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.order.review.ReviewOrderStoreAdminUserFactory import ReviewOrderStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.order.ship.ShipOrderStoreAdminUserFactory import ShipOrderStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.payment.PaymentStoreAdminUserFactory import PaymentStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.product.ProductStoreAdminUserFactory import ProductStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.web.WebStoreAdminUserFactory import WebStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.web.view.editor.ViewEditorWebStoreAdminUserFactory import ViewEditorWebStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.web.wizard.WizardWebStoreAdminUserFactory import WizardWebStoreAdminUserFactory
from org.allbinary.business.user.modules.admin.store.web.workflow.editor.WorkflowEditorWebStoreAdminUserFactory import WorkflowEditorWebStoreAdminUserFactory
from org.allbinary.business.user.modules.customer.subscriber.SubscriberUserFactory import SubscriberUserFactory
from org.allbinary.business.user.modules.customer.wholesale.WholesaleUserFactory import WholesaleUserFactory
from org.allbinary.business.user.role.BasicUserRoleFactory import BasicUserRoleFactory
from org.allbinary.business.user.role.UserRoleB import UserRoleB


UserRoleFactory.instance = UserRoleFactory()

