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
# package admin.taghelpers

from __future__ import annotations



class InventoryItemViewParentTagHelper:
    instance: InventoryItemViewParentTagHelper = None
    

    @staticmethod
    def getInstance() -> InventoryItemViewParentTagHelper:
        return InventoryItemViewParentTagHelper.instance
    

    # throws Exception
    def getInventoryItemView(self, inventoryTag: HelperTag) -> InventoryItemView:
        if inventoryTag is not None:
            self.checkForValidationViewHelper(inventoryTag.getHelper())
            validationViewHelper: ValidationViewHelper = inventoryTag.getHelper()
            viewObject: TransformInterface = validationViewHelper.getViewObject()
            if viewObject.getTypeId() != InventoryItemView.TYPE_ID:
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Must have ")
                stringBuffer.append("InventoryItemView and not: ")
                stringBuffer.append(type(inventoryTag.getHelper()).__module__ + "." + type(inventoryTag.getHelper()).__qualname__)
                raise Exception(str(stringBuffer))
            return viewObject
        else:
            raise Exception("Must have parent tag.")
    

    # throws Exception
    def getDownloadableInventoryItemView(self, inventoryTag: HelperTag) -> DownloadableInventoryItemView:
        if inventoryTag is not None:
            self.checkForValidationViewHelper(inventoryTag.getHelper())
            validationViewHelper: ValidationViewHelper = inventoryTag.getHelper()
            viewObject: TransformInterface = validationViewHelper.getViewObject()
            if viewObject.getTypeId() != DownloadableInventoryItemView.TYPE_ID:
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Must have ")
                stringBuffer.append("DownloadableInventoryItemView and not: ")
                stringBuffer.append(type(inventoryTag.getHelper()).__module__ + "." + type(inventoryTag.getHelper()).__qualname__)
                raise Exception(str(stringBuffer))
            return viewObject
        else:
            raise Exception("Must have parent tag.")
    

    # throws Exception
    def getRequestMapInterface(self, inventoryTag: HelperTag) -> RequestMapInterface:
        if inventoryTag is not None:
            self.checkForValidationViewHelper(inventoryTag.getHelper())
            validationViewHelper: ValidationViewHelper = inventoryTag.getHelper()
            viewObject: TransformInterface = validationViewHelper.getViewObject()
            if viewObject.getTypeId() != InventoryItemView.TYPE_ID and viewObject.getTypeId() != DownloadableInventoryItemView.TYPE_ID:
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Must have ")
                stringBuffer.append("specific TYPE_ID and not: ")
                stringBuffer.append(type(inventoryTag.getHelper()).__module__ + "." + type(inventoryTag.getHelper()).__qualname__)
                raise Exception(str(stringBuffer))
            return viewObject
        else:
            raise Exception("Must have parent tag.")
    

    # throws Exception
    def checkForValidationViewHelper(self, helperObject: object) -> None:
        if not (isinstance(helperObject, ValidationViewHelper)):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Must have ")
            stringBuffer.append("ValidationViewHelper")
            stringBuffer.append("and not: ")
            stringBuffer.append(type(helperObject).__module__ + "." + type(helperObject).__qualname__)
            raise Exception(str(stringBuffer))
from org.allbinary.logic.communication.http.request.RequestMapInterface import RequestMapInterface
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from taghelpers.ValidationViewHelper import ValidationViewHelper
from tags.HelperTag import HelperTag
from views.admin.inventory.InventoryItemView import InventoryItemView
from views.admin.inventory.download.DownloadableInventoryItemView import DownloadableInventoryItemView


InventoryItemViewParentTagHelper.instance = InventoryItemViewParentTagHelper()

