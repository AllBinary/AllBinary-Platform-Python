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
# package org.allbinary.input.automation.module.generic.configuration.profile.actions

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class GenericProfileActionsJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("genericProfileActions", None)
        vars(self).setdefault("genericProfileActionJPanel", None)
        vars(self).setdefault("blankGenericProfileActionJPanel", None)
        vars(self).setdefault("deleteActionJButton", None)
        vars(self).setdefault("genericProfileActionsJList", None)
        vars(self).setdefault("genericProfileActionsJPanel", None)
        vars(self).setdefault("genericProfileActionsJScrollPane", None)
        vars(self).setdefault("newActionJButton", None)
        vars(self).setdefault("newProfileActionJDialog", None)
        vars(self).setdefault("newProfileActionJLabel", None)
        vars(self).setdefault("newProfileActionJTextField", None)
        vars(self).setdefault("okNewProfileActionJButton", None)
        vars(self).setdefault("saveJButton", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "genericProfileActions" not in vars(self): self.genericProfileActions: GenericProfileActions = None
        if "genericProfileActionJPanel" not in vars(self): self.genericProfileActionJPanel: GenericProfileActionJPanel = None
        if "blankGenericProfileActionJPanel" not in vars(self): self.blankGenericProfileActionJPanel: JPanel = None
        if "deleteActionJButton" not in vars(self): self.deleteActionJButton: JButton = None
        if "genericProfileActionsJList" not in vars(self): self.genericProfileActionsJList: JList = None
        if "genericProfileActionsJPanel" not in vars(self): self.genericProfileActionsJPanel: JPanel = None
        if "genericProfileActionsJScrollPane" not in vars(self): self.genericProfileActionsJScrollPane: JScrollPane = None
        if "newActionJButton" not in vars(self): self.newActionJButton: JButton = None
        if "newProfileActionJDialog" not in vars(self): self.newProfileActionJDialog: JDialog = None
        if "newProfileActionJLabel" not in vars(self): self.newProfileActionJLabel: JLabel = None
        if "newProfileActionJTextField" not in vars(self): self.newProfileActionJTextField: JTextField = None
        if "okNewProfileActionJButton" not in vars(self): self.okNewProfileActionJButton: JButton = None
        if "saveJButton" not in vars(self): self.saveJButton: JButton = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
    

    def initComponents(self) -> None:
        self.newProfileActionJDialog = JDialog()
        self.newProfileActionJLabel = JLabel()
        self.okNewProfileActionJButton = JButton()
        self.newProfileActionJTextField = JTextField()
        self.genericProfileActionsJPanel = JPanel()
        self.genericProfileActionsJScrollPane = JScrollPane()
        self.genericProfileActionsJList = JList()
        self.newActionJButton = JButton()
        self.deleteActionJButton = JButton()
        self.saveJButton = JButton()
        self.blankGenericProfileActionJPanel = JPanel()
        self.newProfileActionJDialog.setMinimumSize(Dimension(250, 150))
        self.newProfileActionJDialog.setResizable(False)
        self.newProfileActionJLabel.setText("New Action Name")
        self.okNewProfileActionJButton.setText("Ok")
        _java_listener_owner = self
        class _JavaListenerN66752(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "okNewProfileActionJButtonActionPerformed") else _java_listener_owner).okNewProfileActionJButtonActionPerformed(evt)
        self.okNewProfileActionJButton.addActionListener(_JavaListenerN66752()
            )
        newProfileActionJDialogLayout: GroupLayout = GroupLayout(self.newProfileActionJDialog.getContentPane())
        self.newProfileActionJDialog.getContentPane().setLayout(newProfileActionJDialogLayout)
        newProfileActionJDialogLayout.setHorizontalGroup(newProfileActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGroup(newProfileActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGap(93, 93, 93).addComponent(self.okNewProfileActionJButton)).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGap(75, 75, 75).addComponent(self.newProfileActionJLabel)).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGap(29, 29, 29).addComponent(self.newProfileActionJTextField, GroupLayout.PREFERRED_SIZE, 178, GroupLayout.PREFERRED_SIZE))).addContainerGap(34, Short.MAX_VALUE)))
        newProfileActionJDialogLayout.setVerticalGroup(newProfileActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(GroupLayout.Alignment.TRAILING, newProfileActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.newProfileActionJLabel).addGap(21, 21, 21).addComponent(self.newProfileActionJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 20, Short.MAX_VALUE).addComponent(self.okNewProfileActionJButton).addContainerGap()))
        self.genericProfileActionsJPanel.setPreferredSize(Dimension(10000, 10000))
        _java_listener_owner = self
        class _JavaListenerN67750(ListSelectionListener):
            
            

            def valueChanged(self, evt: ListSelectionEvent) -> None:
                (self if hasattr(self, "genericProfileActionsJListValueChanged") else _java_listener_owner).genericProfileActionsJListValueChanged(evt)
        self.genericProfileActionsJList.addListSelectionListener(_JavaListenerN67750()
            )
        self.genericProfileActionsJScrollPane.setViewportView(self.genericProfileActionsJList)
        self.newActionJButton.setText("New")
        _java_listener_owner = self
        class _JavaListenerN67926(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "newActionJButtonActionPerformed") else _java_listener_owner).newActionJButtonActionPerformed(evt)
        self.newActionJButton.addActionListener(_JavaListenerN67926()
            )
        self.deleteActionJButton.setText("Delete")
        _java_listener_owner = self
        class _JavaListenerN68065(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "deleteActionJButtonActionPerformed") else _java_listener_owner).deleteActionJButtonActionPerformed(evt)
        self.deleteActionJButton.addActionListener(_JavaListenerN68065()
            )
        self.saveJButton.setText("Save")
        _java_listener_owner = self
        class _JavaListenerN68204(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "saveJButtonActionPerformed") else _java_listener_owner).saveJButtonActionPerformed(evt)
        self.saveJButton.addActionListener(_JavaListenerN68204()
            )
        self.blankGenericProfileActionJPanel.setMinimumSize(Dimension(500, 300))
        blankGenericProfileActionJPanelLayout: GroupLayout = GroupLayout(self.blankGenericProfileActionJPanel)
        self.blankGenericProfileActionJPanel.setLayout(blankGenericProfileActionJPanelLayout)
        blankGenericProfileActionJPanelLayout.setHorizontalGroup(blankGenericProfileActionJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 500, Short.MAX_VALUE))
        blankGenericProfileActionJPanelLayout.setVerticalGroup(blankGenericProfileActionJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 296, Short.MAX_VALUE))
        genericProfileActionsJPanelLayout: GroupLayout = GroupLayout(self.genericProfileActionsJPanel)
        self.genericProfileActionsJPanel.setLayout(genericProfileActionsJPanelLayout)
        genericProfileActionsJPanelLayout.setHorizontalGroup(genericProfileActionsJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(genericProfileActionsJPanelLayout.createSequentialGroup().addComponent(self.genericProfileActionsJScrollPane, GroupLayout.PREFERRED_SIZE, 95, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.blankGenericProfileActionJPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)).addGroup(genericProfileActionsJPanelLayout.createSequentialGroup().addComponent(self.newActionJButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.deleteActionJButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.saveJButton).addContainerGap()))
        genericProfileActionsJPanelLayout.setVerticalGroup(genericProfileActionsJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(genericProfileActionsJPanelLayout.createSequentialGroup().addGroup(genericProfileActionsJPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.newActionJButton).addComponent(self.deleteActionJButton).addComponent(self.saveJButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(genericProfileActionsJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False).addComponent(self.blankGenericProfileActionJPanel, 0, 296, Short.MAX_VALUE).addComponent(self.genericProfileActionsJScrollPane, GroupLayout.DEFAULT_SIZE, 296, Short.MAX_VALUE)).addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.genericProfileActionsJPanel, GroupLayout.PREFERRED_SIZE, 596, GroupLayout.PREFERRED_SIZE).addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.genericProfileActionsJPanel, GroupLayout.PREFERRED_SIZE, 336, GroupLayout.PREFERRED_SIZE))
    

    def setModel(self) -> None:
        from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
        defaultListModelHelper: DefaultListModelHelper = self.getGenericProfileActions().getDefaultListModelHelper()
        if defaultListModelHelper.getListModel().getSize() > 0:
            self.genericProfileActionsJList.setModel(defaultListModelHelper.getListModel())
    

    def saveJButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.getGenericProfileActions().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "saveJButtonActionPerformed", e)
    

    def updateProfileActionUI(self, profileActionNameString: str) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
        self.blankGenericProfileActionJPanel.removeAll()
        if profileActionNameString is not None:
            genericProfileAction: GenericProfileAction = self.getGenericProfileActions().getAction(profileActionNameString)
            self.setGenericProfileActionJPanel(GenericProfileActionJPanel())
            self.getGenericProfileActionJPanel().setGenericProfileAction(genericProfileAction)
            self.getGenericProfileActionJPanel().updateProfileActionUI()
            layout: GroupLayout = self.blankGenericProfileActionJPanel.getLayout()
            layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE).addComponent(self.getGenericProfileActionJPanel(), GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
            layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 256, Short.MAX_VALUE).addComponent(self.getGenericProfileActionJPanel(), GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
            self.logUtil.putF("Setting Configuration Profile Actions JPanel", self, "genericProfileActionsJListValueChanged")
    

    def genericProfileActionsJListValueChanged(self, evt: ListSelectionEvent) -> None:
        try:
            profileActionNameString: str = self.genericProfileActionsJList.getSelectedValue()
            self.updateProfileActionUI(profileActionNameString)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "genericProfileActionsJListValueChanged", e)
    

    def okNewProfileActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            newActionName: str = self.newProfileActionJTextField.getText()
            self.getGenericProfileActions().add(newActionName)
            self.setModel()
            self.genericProfileActionsJList.setSelectedValue(newActionName, True)
            self.newProfileActionJDialog.setVisible(False)
            self.updateProfileActionUI(newActionName)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "okNewProfileActionJButtonActionPerformed", e)
    

    def deleteActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            anyType: list[object] = self.genericProfileActionsJList.getSelectedValues()
            for index in range(0, len(anyType)):
                nextSelectedValueString: str = anyType[index]
                self.getGenericProfileActions().remove(nextSelectedValueString)
            self.selectFirstElement()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "deleteActionJButtonActionPerformed", e)
    

    # throws Exception
    def selectFirstElement(self) -> None:
        self.setModel()
        if self.genericProfileActionsJList.getModel().getSize() > 0:
            self.genericProfileActionsJList.setSelectedValue(self.genericProfileActionsJList.getModel().getElementAt(0), True)
            self.updateProfileActionUI(self.genericProfileActionsJList.getModel().getElementAt(0))
        else:
            self.blankGenericProfileActionJPanel.removeAll()
            self.blankGenericProfileActionJPanel.repaint()
    

    def getGenericProfileActionJPanel(self) -> GenericProfileActionJPanel:
        return self.genericProfileActionJPanel
    

    def setGenericProfileActionJPanel(self, genericProfileActionJPanel: GenericProfileActionJPanel) -> None:
        self.genericProfileActionJPanel = genericProfileActionJPanel
    

    def getGenericProfileActions(self) -> GenericProfileActions:
        return self.genericProfileActions
    

    def setGenericProfileActions(self, genericProfileActions: GenericProfileActions) -> None:
        self.genericProfileActions = genericProfileActions
    

    def newActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.newProfileActionJDialog.setVisible(True)
# from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.JList import JList
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle
# from javax.swing.event.ListSelectionEvent import ListSelectionEvent
# from javax.swing.event.ListSelectionListener import ListSelectionListener


