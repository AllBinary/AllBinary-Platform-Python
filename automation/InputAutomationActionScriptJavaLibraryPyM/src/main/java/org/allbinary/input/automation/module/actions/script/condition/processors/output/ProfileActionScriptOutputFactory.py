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
# package org.allbinary.input.automation.module.actions.script.condition.processors.output

from __future__ import annotations



class ProfileActionScriptOutputFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(node: Node) -> ProfileActionScriptOutputInterface:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutput import ImageActionScriptOutput
        profileActionScriptOutputInterface: ProfileActionScriptOutputInterface = None
        if DomSearchHelper.getNodeNoThrow(ImageActionScriptOutputData.NAME, node.getChildNodes()) is not None:
            profileActionScriptOutputInterface = ImageActionScriptOutput(node)
        else:
            raise Exception("No Such ActionScript Output")
        return profileActionScriptOutputInterface
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.w3c.dom.Node import Node


