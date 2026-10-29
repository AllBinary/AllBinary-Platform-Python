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
# package org.allbinary.logic.visual.dhtml.style.css

from __future__ import annotations



class CssElementValidationFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(node: Node) -> ValidationInterface:
        from org.allbinary.logic.visual.dhtml.style.css.CssElementValidation import CssElementValidation
        return CssElementValidation(node)
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.w3c.dom.Node import Node


