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



class AdminRoleFactory:
    instance: AdminRoleFactory = None

    def _init_fields(self) -> None:
        self.adminRoles: BasicArrayList = BasicArrayListD()
        self.storeAdminRoles: BasicArrayList = BasicArrayListD()
        self.storeManagementRoles: BasicArrayList = BasicArrayListD()
        self.productManagementRoles: BasicArrayList = BasicArrayListD()
        self.reviewManagementRoles: BasicArrayList = BasicArrayListD()
        self.customerManagementRoles: BasicArrayList = BasicArrayListD()
        self.workflowManagementRoles: BasicArrayList = BasicArrayListD()
        self.orderManagementRoles: BasicArrayList = BasicArrayListD()
        self.adjusterManagementRoles: BasicArrayList = BasicArrayListD()
        self.shippingManagementRoles: BasicArrayList = BasicArrayListD()
        self.webManagementRoles: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> AdminRoleFactory:
        return AdminRoleFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.business.user.role.BasicUserRoleFactory import BasicUserRoleFactory
        self._init_fields()
        basicUserRoleFactory: BasicUserRoleFactory = BasicUserRoleFactory.getInstance()
        self.adminRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.storeAdminRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.storeAdminRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.storeManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.storeManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.storeManagementRoles.add(basicUserRoleFactory.CUSTOMERMANAGER)
        self.storeManagementRoles.add(basicUserRoleFactory.ADJUSTER)
        self.storeManagementRoles.add(basicUserRoleFactory.PRODUCTMANAGER)
        self.storeManagementRoles.add(basicUserRoleFactory.REVIEWER)
        self.storeManagementRoles.add(basicUserRoleFactory.SHIPPING)
        self.productManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.productManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.productManagementRoles.add(basicUserRoleFactory.PRODUCTMANAGER)
        self.reviewManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.reviewManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.reviewManagementRoles.add(basicUserRoleFactory.REVIEWER)
        self.customerManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.customerManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.customerManagementRoles.add(basicUserRoleFactory.CUSTOMERMANAGER)
        self.workflowManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.workflowManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.workflowManagementRoles.add(basicUserRoleFactory.WORKFLOWEDITOR)
        self.orderManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.orderManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.adjusterManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.adjusterManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.adjusterManagementRoles.add(basicUserRoleFactory.ADJUSTER)
        self.shippingManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.shippingManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.shippingManagementRoles.add(basicUserRoleFactory.SHIPPING)
        self.webManagementRoles.add(basicUserRoleFactory.ADMINISTRATOR)
        self.webManagementRoles.add(basicUserRoleFactory.STOREMANAGER)
        self.webManagementRoles.add(basicUserRoleFactory.WEBMANAGER)
        self.webManagementRoles.add(basicUserRoleFactory.WORKFLOWEDITOR)
        self.webManagementRoles.add(basicUserRoleFactory.VIEWEDITOR)
    

    def getProductManagementRoles(self) -> BasicArrayList:
        return self.productManagementRoles
    

    def getAdminRoles(self) -> BasicArrayList:
        return self.adminRoles
    

    def getStoreAdminRoles(self) -> BasicArrayList:
        return self.storeAdminRoles
    

    def getStoreManagementRoles(self) -> BasicArrayList:
        return self.storeManagementRoles
    

    def getReviewManagementRoles(self) -> BasicArrayList:
        return self.reviewManagementRoles
    

    def getCustomerManagementRoles(self) -> BasicArrayList:
        return self.customerManagementRoles
    

    def getWorkflowManagementRoles(self) -> BasicArrayList:
        return self.workflowManagementRoles
    

    def getWebManagementRoles(self) -> BasicArrayList:
        return self.webManagementRoles
    

    def getShippingManagementRoles(self) -> BasicArrayList:
        return self.shippingManagementRoles
    

    def getAdjusterManagementRoles(self) -> BasicArrayList:
        return self.adjusterManagementRoles
    

    def getOrderManagementRoles(self) -> BasicArrayList:
        return self.orderManagementRoles
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


AdminRoleFactory.instance = AdminRoleFactory()

