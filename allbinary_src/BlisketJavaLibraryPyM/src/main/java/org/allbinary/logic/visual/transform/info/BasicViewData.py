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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations



class BasicViewData:
    instance: BasicViewData = None

    def _init_fields(self) -> None:
        self.GENERICDIR: str = "generic/"
        self.USERDIR: str = self.GENERICDIR + "user/"
        self.ADDRESSDIR: str = self.USERDIR + "address/"
        self.BILLINGADDRESSDIR: str = self.ADDRESSDIR + "billing/"
        self.SHIPPINGADDRESSDIR: str = self.ADDRESSDIR + "shipping/"
        self.COMMERCEDIR: str = self.USERDIR + "commerce/"
        self.INVENTORYDIR: str = self.COMMERCEDIR + "inventory/"
        self.BASKETDIR: str = self.INVENTORYDIR + "basket/"
        self.ITEMDIR: str = self.INVENTORYDIR + "item/"
        self.MONEYDIR: str = self.COMMERCEDIR + "money/"
        self.SHIPPINGDIR: str = self.COMMERCEDIR + "shipping/"
        self.ORDERDIR: str = self.INVENTORYDIR + "order/"
        self.ORDEREMAILDIR: str = self.ORDERDIR + "email/"
        self.ORDERHISTORYDIR: str = self.ORDERDIR + "history/"
        self.ORDERREVIEWDIR: str = self.ORDERDIR + "review/"
        self.PAYMENTDIR: str = self.MONEYDIR + "payment/"
        self.GENERATIONDIR: str = self.GENERICDIR + "generation/"
        self.PRODUCTSDIR: str = self.GENERICDIR + "products/"
        self.IGNOREXMLXSL: str = self.GENERICDIR + "ignoreXmlView.xsl"
        self.REVIEWORDERVIEWXSL: str = self.ORDERREVIEWDIR + "reviewOrderView.xsl"
        self.ORDERVIEWXSL: str = self.REVIEWORDERVIEWXSL
        self.INVENTORYXSL: str = self.INVENTORYDIR + "inventory.xsl"
        self.BASKETXSL: str = self.BASKETDIR + "basket.xsl"
        self.CHECKOUTBASKETXSL: str = self.BASKETDIR + "staticBasket.xsl"
        self.MINIBASKETXSL: str = self.BASKETDIR + "miniBasket.xsl"
        self.BILLINGADDRESSCHANGEFORMXSL: str = self.BILLINGADDRESSDIR + "billingAddressChangeForm.xsl"
        self.BILLINGADDRESSINPUTFORMXSL: str = self.BILLINGADDRESSDIR + "billingAddressInputForm.xsl"
        self.BILLINGADDRESSVIEWXSL: str = self.BILLINGADDRESSDIR + "billingAddressView.xsl"
        self.SHIPPINGADDRESSCHANGEFORMXSL: str = self.SHIPPINGADDRESSDIR + "shippingAddressChangeForm.xsl"
        self.SHIPPINGADDRESSINPUTFORMXSL: str = self.SHIPPINGADDRESSDIR + "shippingAddressInputForm.xsl"
        self.SHIPPINGADDRESSVIEWXSL: str = self.SHIPPINGADDRESSDIR + "shippingAddressView.xsl"
        self.NEWTAXADDRESSXSL: str = self.SHIPPINGADDRESSDIR + "newTaxAddressView.xsl"
        self.EDITTAXADDRESSXSL: str = self.SHIPPINGADDRESSDIR + "editTaxAddressView.xsl"
        self.SHIPPINGMETHODSXSL: str = self.SHIPPINGDIR + "shippingMethods.xsl"
        self.ORDERCUSTOMEREMAILVIEWXSL: str = self.ORDEREMAILDIR + "orderCustomerEmailView.xsl"
        self.ORDERMANAGEREMAILVIEWXSL: str = self.ORDEREMAILDIR + "orderManagerEmailView.xsl"
        self.EDITCUSTOMERXSL: str = self.USERDIR + "editCustomerInputForm.xsl"
        self.ORDERHISTORYXSL: str = self.ORDERHISTORYDIR + "orderHistory.xsl"
        self.PAYMENTVIEWXSL: str = self.PAYMENTDIR + "paymentView.xsl"
        self.SUMMARYXSL: str = self.ITEMDIR + "summary/summary.xsl"
        self.PAYMENTGATEWAYOPTIONSXSL: str = self.PAYMENTDIR + "paymentGatewayOptions.xsl"
        self.MAKEPAYMENTVIEWXSL: str = self.PAYMENTDIR + "invoice/" + "makePayment.xsl"
    

    @staticmethod
    def getInstance() -> BasicViewData:
        return BasicViewData.instance
    

    def __init__(self) -> None:
        self._init_fields()


BasicViewData.instance = BasicViewData()

