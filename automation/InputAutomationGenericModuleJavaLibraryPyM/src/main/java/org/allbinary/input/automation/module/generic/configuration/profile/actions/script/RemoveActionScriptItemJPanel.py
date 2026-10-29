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
# package org.allbinary.input.automation.module.generic.configuration.profile.actions.script

from __future__ import annotations

from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.Panel import Panel


class RemoveActionScriptItemJPanel(Panel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.genericProfileActionJPanel: GenericProfileActionJPanel = None
        self.profileActionScriptConditionInterface: ProfileActionScriptConditionInterface = None
        self.removeJButton: JButton = None
    

    def __init__(self, genericProfileActionJPanel: GenericProfileActionJPanel, profileActionScriptConditionInterface: ProfileActionScriptConditionInterface) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.genericProfileActionJPanel = genericProfileActionJPanel
        self.profileActionScriptConditionInterface = profileActionScriptConditionInterface
    

    def initComponents(self) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.JButton import JButton
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GridLayout import GridLayout
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.ActionListener import ActionListener
        self.removeJButton = JButton()
        self.setLayout(GridLayout())
        self.removeJButton.setText("Remove")
        self.removeJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.removeJButtonActionPerformed(evt)
))
        self.add(self.removeJButton)
    

    def removeJButtonActionPerformed(self, evt: ActionEvent) -> None:
        genericProfileAction: GenericProfileAction = self.genericProfileActionJPanel.getGenericProfileAction()
        if genericProfileAction is None:
            self.logUtil.putF("GenericProfileAction was null", self, "removeJButtonActionPerformed")
            return
        genericProfileAction.getGenericProfileActionScript().removeCondition(self.profileActionScriptConditionInterface)
        self.genericProfileActionJPanel.updateProfileActionUI()
from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileAction import GenericProfileAction
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
from org.allbinary.logic.communication.log.LogUtil import LogUtil


