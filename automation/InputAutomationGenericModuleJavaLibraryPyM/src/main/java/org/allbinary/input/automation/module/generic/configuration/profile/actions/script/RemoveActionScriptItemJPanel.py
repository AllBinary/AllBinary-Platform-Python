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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from java.awt.Panel import Panel


@java_inherited_overloads
class RemoveActionScriptItemJPanel(Panel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("genericProfileActionJPanel", None)
        vars(self).setdefault("profileActionScriptConditionInterface", None)
        vars(self).setdefault("removeJButton", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "genericProfileActionJPanel" not in vars(self): self.genericProfileActionJPanel: GenericProfileActionJPanel = None
        if "profileActionScriptConditionInterface" not in vars(self): self.profileActionScriptConditionInterface: ProfileActionScriptConditionInterface = None
        if "removeJButton" not in vars(self): self.removeJButton: JButton = None
    

    def __init__(self, genericProfileActionJPanel: GenericProfileActionJPanel, profileActionScriptConditionInterface: ProfileActionScriptConditionInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        self.genericProfileActionJPanel = genericProfileActionJPanel
        self.profileActionScriptConditionInterface = profileActionScriptConditionInterface
    

    def initComponents(self) -> None:
        self.removeJButton = JButton()
        self.setLayout(GridLayout())
        self.removeJButton.setText("Remove")
        _java_listener_owner = self
        class _JavaListenerN66292(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "removeJButtonActionPerformed") else _java_listener_owner).removeJButtonActionPerformed(evt)
        self.removeJButton.addActionListener(_JavaListenerN66292()
            )
        self.add(self.removeJButton)
    

    def removeJButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileAction import GenericProfileAction
        genericProfileAction: GenericProfileAction = self.genericProfileActionJPanel.getGenericProfileAction()
        if genericProfileAction is None:
            self.logUtil.putF("GenericProfileAction was null", self, "removeJButtonActionPerformed")
            return
        genericProfileAction.getGenericProfileActionScript().removeCondition(self.profileActionScriptConditionInterface)
        self.genericProfileActionJPanel.updateProfileActionUI()
# from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
# from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileAction import GenericProfileAction
# from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from java.awt.GridLayout import GridLayout
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.JButton import JButton


