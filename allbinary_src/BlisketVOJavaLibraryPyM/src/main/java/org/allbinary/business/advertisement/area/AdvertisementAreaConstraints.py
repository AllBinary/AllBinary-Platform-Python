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
# package org.allbinary.business.advertisement.area

from __future__ import annotations

from org.allbinary.business.advertisement.area.AdvertisementAreaConstraintsInterface import AdvertisementAreaConstraintsInterface


class AdvertisementAreaConstraints(AdvertisementAreaConstraintsInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
        self.displayInBrowserContraintsInterface: DisplayInBrowserContraintsInterface = None
        self.twoDimensionConstraintsInterface: TwoDimensionalConstraintInterface = None
    

    def __init__(self, document: Document) -> None:
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraints import DisplayInBrowserContraints
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraint import TwoDimensionalConstraint
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        self._init_fields()
        node: Node = DomSearchHelper.getNode(AdvertisementAreaData.getInstance().NAME, document.getChildNodes())
        self.displayInBrowserContraintsInterface = DisplayInBrowserContraints(node)
        self.twoDimensionConstraintsInterface = TwoDimensionalConstraint(node)
    

    def setDisplayInBrowserContraints(self, displayInBrowserContraintsInterface: DisplayInBrowserContraintsInterface) -> None:
        from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface
        self.displayInBrowserContraintsInterface = displayInBrowserContraintsInterface
    

    def getTwoDimensionContraints_j1(self, twoDimensionConstraintsInterface: TwoDimensionalConstraintInterface) -> None:
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
        self.twoDimensionConstraintsInterface = twoDimensionConstraintsInterface
    

    def getDisplayInBrowserContraints(self) -> DisplayInBrowserContraintsInterface:
        from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface
        return self.displayInBrowserContraintsInterface
    

    def getTwoDimensionContraints_j0(self) -> TwoDimensionalConstraintInterface:
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
        return self.twoDimensionConstraintsInterface

    def getTwoDimensionContraints(self, *args):
        return getattr(self, "getTwoDimensionContraints_j" + str(len(args)))(*args)
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraints import DisplayInBrowserContraints
# from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface
# from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraint import TwoDimensionalConstraint
# from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


