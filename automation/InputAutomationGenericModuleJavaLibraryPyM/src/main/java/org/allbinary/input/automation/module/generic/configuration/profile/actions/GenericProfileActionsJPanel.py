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

# from javax.swing.JPanel import JPanel


class GenericProfileActionsJPanel(JPanel):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.genericProfileActions: GenericProfileActions = None
        self.genericProfileActionJPanel: GenericProfileActionJPanel = None
        self.blankGenericProfileActionJPanel: JPanel = None
        self.deleteActionJButton: JButton = None
        self.genericProfileActionsJList: JList = None
        self.genericProfileActionsJPanel: JPanel = None
        self.genericProfileActionsJScrollPane: JScrollPane = None
        self.newActionJButton: JButton = None
        self.newProfileActionJDialog: JDialog = None
        self.newProfileActionJLabel: JLabel = None
        self.newProfileActionJTextField: JTextField = None
        self.okNewProfileActionJButton: JButton = None
        self.saveJButton: JButton = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
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
        self.okNewProfileActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okNewProfileActionJButtonActionPerformed(evt)
))
        newProfileActionJDialogLayout: GroupLayout = GroupLayout(self.newProfileActionJDialog.getContentPane())
        self.newProfileActionJDialog.getContentPane().setLayout(newProfileActionJDialogLayout)
        newProfileActionJDialogLayout.setHorizontalGroup(newProfileActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGroup(newProfileActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGap(93, 93, 93).addComponent(self.okNewProfileActionJButton)).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGap(75, 75, 75).addComponent(self.newProfileActionJLabel)).addGroup(newProfileActionJDialogLayout.createSequentialGroup().addGap(29, 29, 29).addComponent(self.newProfileActionJTextField, GroupLayout.PREFERRED_SIZE, 178, GroupLayout.PREFERRED_SIZE))).addContainerGap(34, Short.MAX_VALUE)))
        newProfileActionJDialogLayout.setVerticalGroup(newProfileActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(GroupLayout.Alignment.TRAILING, newProfileActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.newProfileActionJLabel).addGap(21, 21, 21).addComponent(self.newProfileActionJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 20, Short.MAX_VALUE).addComponent(self.okNewProfileActionJButton).addContainerGap()))
        self.genericProfileActionsJPanel.setPreferredSize(Dimension(10000, 10000))
        self.genericProfileActionsJList.addListSelectionListener((ListSelectionListener()  # Java anonymous class body:
#             
# 
#             def valueChanged(self, evt: ListSelectionEvent) -> None:
#                 self.genericProfileActionsJListValueChanged(evt)
))
        self.genericProfileActionsJScrollPane.setViewportView(self.genericProfileActionsJList)
        self.newActionJButton.setText("New")
        self.newActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.newActionJButtonActionPerformed(evt)
))
        self.deleteActionJButton.setText("Delete")
        self.deleteActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.deleteActionJButtonActionPerformed(evt)
))
        self.saveJButton.setText("Save")
        self.saveJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.saveJButtonActionPerformed(evt)
))
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


