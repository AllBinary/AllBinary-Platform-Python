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
# package org.allbinary.input.automation.module.generic.configuration

from __future__ import annotations

from org.allbinary.input.automation.module.generic.configuration.JPanel import JPanel
from org.allbinary.input.automation.module.generic.configuration.GenericModuleConfigurationInterface import GenericModuleConfigurationInterface


class GenericModuleConfigurationJPanel(JPanel, GenericModuleConfigurationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.genericProfiles: GenericProfiles = None
        self.selectedGenericProfile: GenericProfile = None
        self.blankGenericProfileActionsJPanel: JPanel = None
        self.buttonGroup2: ButtonGroup = None
        self.captureComparisonJCheckBox: JCheckBox = None
        self.captureMotionAnalysisJCheckBox: JCheckBox = None
        self.deleteProfileJButton: JButton = None
        self.genericJTabbedPane: JTabbedPane = None
        self.genericProfilesJList: JList = None
        self.genericProfilesJPanel: JPanel = None
        self.genericProfilesJScrollPane: JScrollPane = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.jLabel3: JLabel = None
        self.jPanel1: JPanel = None
        self.newProfileJButton: JButton = None
        self.newProfileJDialog: JDialog = None
        self.newProfileNameJLabel: JLabel = None
        self.newProfileNameJTextField: JTextField = None
        self.okNewProfileJButton: JButton = None
        self.savedCaptureJRadioButton: JRadioButton = None
        self.screenCaptureJRadioButton: JRadioButton = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.setGenericProfiles(GenericProfiles(GenericProfiles.DEFAULT_FILE))
        self.selectFirstElement()
    

    def initComponents(self) -> None:
        from org.allbinary.input.automation.module.generic.configuration.JDialog import JDialog
        from org.allbinary.input.automation.module.generic.configuration.JButton import JButton
        from org.allbinary.input.automation.module.generic.configuration.JLabel import JLabel
        from org.allbinary.input.automation.module.generic.configuration.JTextField import JTextField
        from org.allbinary.input.automation.module.generic.configuration.ButtonGroup import ButtonGroup
        from org.allbinary.input.automation.module.generic.configuration.JTabbedPane import JTabbedPane
        from org.allbinary.input.automation.module.generic.configuration.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.JScrollPane import JScrollPane
        from org.allbinary.input.automation.module.generic.configuration.JList import JList
        from org.allbinary.input.automation.module.generic.configuration.JButton import JButton
        from org.allbinary.input.automation.module.generic.configuration.JButton import JButton
        from org.allbinary.input.automation.module.generic.configuration.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.JRadioButton import JRadioButton
        from org.allbinary.input.automation.module.generic.configuration.JLabel import JLabel
        from org.allbinary.input.automation.module.generic.configuration.JLabel import JLabel
        from org.allbinary.input.automation.module.generic.configuration.JRadioButton import JRadioButton
        from org.allbinary.input.automation.module.generic.configuration.JCheckBox import JCheckBox
        from org.allbinary.input.automation.module.generic.configuration.JCheckBox import JCheckBox
        from org.allbinary.input.automation.module.generic.configuration.JLabel import JLabel
        from org.allbinary.input.automation.module.generic.configuration.JPanel import JPanel
        from org.allbinary.input.automation.module.generic.configuration.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.GroupLayout import GroupLayout
        from org.allbinary.input.automation.module.generic.configuration.GridLayout import GridLayout
        from org.allbinary.input.automation.module.generic.configuration.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.ListSelectionListener import ListSelectionListener
        from org.allbinary.input.automation.module.generic.configuration.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.configuration.Insets import Insets
        from org.allbinary.input.automation.module.generic.configuration.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.Insets import Insets
        from org.allbinary.input.automation.module.generic.configuration.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.Insets import Insets
        from org.allbinary.input.automation.module.generic.configuration.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.Insets import Insets
        from org.allbinary.input.automation.module.generic.configuration.ActionListener import ActionListener
        from org.allbinary.input.automation.module.generic.configuration.GroupLayout import GroupLayout
        from org.allbinary.input.automation.module.generic.configuration.GroupLayout import GroupLayout
        from org.allbinary.input.automation.module.generic.configuration.GroupLayout import GroupLayout
        self.newProfileJDialog = JDialog()
        self.okNewProfileJButton = JButton()
        self.newProfileNameJLabel = JLabel()
        self.newProfileNameJTextField = JTextField()
        self.buttonGroup2 = ButtonGroup()
        self.genericJTabbedPane = JTabbedPane()
        self.genericProfilesJPanel = JPanel()
        self.genericProfilesJScrollPane = JScrollPane()
        self.genericProfilesJList = JList()
        self.newProfileJButton = JButton()
        self.deleteProfileJButton = JButton()
        self.jPanel1 = JPanel()
        self.screenCaptureJRadioButton = JRadioButton()
        self.jLabel1 = JLabel()
        self.jLabel2 = JLabel()
        self.savedCaptureJRadioButton = JRadioButton()
        self.captureMotionAnalysisJCheckBox = JCheckBox()
        self.captureComparisonJCheckBox = JCheckBox()
        self.jLabel3 = JLabel()
        self.blankGenericProfileActionsJPanel = JPanel()
        self.newProfileJDialog.setMinimumSize(Dimension(250, 150))
        self.newProfileJDialog.setResizable(False)
        self.okNewProfileJButton.setText("Ok")
        self.okNewProfileJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okNewProfileJButtonActionPerformed(evt)
))
        self.newProfileNameJLabel.setText("New Profile Name")
        newProfileJDialogLayout: GroupLayout = GroupLayout(self.newProfileJDialog.getContentPane())
        self.newProfileJDialog.getContentPane().setLayout(newProfileJDialogLayout)
        newProfileJDialogLayout.setHorizontalGroup(newProfileJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(newProfileJDialogLayout.createSequentialGroup().addGroup(newProfileJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(80, 80, 80).addComponent(self.newProfileNameJLabel)).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(30, 30, 30).addComponent(self.newProfileNameJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 180, javax.swing.GroupLayout.PREFERRED_SIZE)).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(100, 100, 100).addComponent(self.okNewProfileJButton))).addContainerGap(35, Short.MAX_VALUE)))
        newProfileJDialogLayout.setVerticalGroup(newProfileJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(10, 10, 10).addComponent(self.newProfileNameJLabel).addGap(16, 16, 16).addComponent(self.newProfileNameJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addGap(20, 20, 20).addComponent(self.okNewProfileJButton)))
        self.setLayout(GridLayout(1, 0))
        self.setMinimumSize(Dimension(400, 300))
        self.setPreferredSize(Dimension(700, 700))
        self.genericJTabbedPane.setToolTipText(self.stringUtil.EMPTY_STRING)
        self.genericJTabbedPane.setMinimumSize(Dimension(800, 600))
        self.genericProfilesJPanel.setMinimumSize(Dimension(400, 300))
        self.genericProfilesJPanel.setPreferredSize(Dimension(0, 0))
        self.genericProfilesJList.addListSelectionListener((ListSelectionListener()  # Java anonymous class body:
#             
# 
#             def valueChanged(self, evt: ListSelectionEvent) -> None:
#                 self.genericProfilesJListValueChanged(evt)
))
        self.genericProfilesJScrollPane.setViewportView(self.genericProfilesJList)
        self.newProfileJButton.setText("New")
        self.newProfileJButton.setToolTipText("Creates a new profile")
        self.newProfileJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.newProfileJButtonActionPerformed(evt)
))
        self.deleteProfileJButton.setText("Delete")
        self.deleteProfileJButton.setToolTipText("Deletes the selected profile")
        self.deleteProfileJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.deleteProfileJButtonActionPerformed(evt)
))
        self.jPanel1.setPreferredSize(Dimension(1000, 100))
        self.screenCaptureJRadioButton.setText("Screen Captures")
        self.screenCaptureJRadioButton.setToolTipText("Records the screen into memory for logical processing")
        self.screenCaptureJRadioButton.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.screenCaptureJRadioButton.setMargin(Insets(0, 0, 0, 0))
        self.screenCaptureJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.screenCaptureJRadioButtonActionPerformed(evt)
))
        self.jLabel1.setText("Profile Options")
        self.jLabel2.setText("Process From:")
        self.savedCaptureJRadioButton.setText("Saved Images")
        self.savedCaptureJRadioButton.setToolTipText("Loads images from files for logical processing.  Usually for debugging your profile actions")
        self.savedCaptureJRadioButton.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.savedCaptureJRadioButton.setMargin(Insets(0, 0, 0, 0))
        self.savedCaptureJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.savedCaptureJRadioButtonActionPerformed(evt)
))
        self.captureMotionAnalysisJCheckBox.setText("Motion Analysis")
        self.captureMotionAnalysisJCheckBox.setToolTipText("Uses image comparison and contraints to locate moving objects")
        self.captureMotionAnalysisJCheckBox.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.captureMotionAnalysisJCheckBox.setMargin(Insets(0, 0, 0, 0))
        self.captureMotionAnalysisJCheckBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.captureMotionAnalysisJCheckBoxActionPerformed(evt)
))
        self.captureComparisonJCheckBox.setText("Comparison")
        self.captureComparisonJCheckBox.setToolTipText("Compares the last two input images for multi image logic")
        self.captureComparisonJCheckBox.setBorder(javax.swing.BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.captureComparisonJCheckBox.setMargin(Insets(0, 0, 0, 0))
        self.captureComparisonJCheckBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.captureComparisonJCheckBoxActionPerformed(evt)
))
        self.jLabel3.setText("Image Processing:")
        self.jLabel3.setToolTipText("Turns on/off various extended image processing")
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.screenCaptureJRadioButton).addComponent(self.jLabel1).addComponent(self.jLabel2).addComponent(self.savedCaptureJRadioButton).addComponent(self.captureMotionAnalysisJCheckBox).addComponent(self.captureComparisonJCheckBox).addComponent(self.jLabel3)).addContainerGap(22, Short.MAX_VALUE)))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel2).addGap(7, 7, 7).addComponent(self.screenCaptureJRadioButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.savedCaptureJRadioButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel3).addGap(7, 7, 7).addComponent(self.captureComparisonJCheckBox).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.captureMotionAnalysisJCheckBox).addContainerGap(106, Short.MAX_VALUE)))
        genericProfilesJPanelLayout: GroupLayout = GroupLayout(self.genericProfilesJPanel)
        self.genericProfilesJPanel.setLayout(genericProfilesJPanelLayout)
        genericProfilesJPanelLayout.setHorizontalGroup(genericProfilesJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addGroup(genericProfilesJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addComponent(self.newProfileJButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.deleteProfileJButton)).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addComponent(self.genericProfilesJScrollPane, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 119, Short.MAX_VALUE))).addContainerGap()))
        genericProfilesJPanelLayout.setVerticalGroup(genericProfilesJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addGroup(genericProfilesJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.newProfileJButton).addComponent(self.deleteProfileJButton)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(genericProfilesJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 246, Short.MAX_VALUE).addComponent(self.genericProfilesJScrollPane, javax.swing.GroupLayout.DEFAULT_SIZE, 246, Short.MAX_VALUE))))
        self.genericJTabbedPane.addTab("Profiles", self.genericProfilesJPanel)
        blankGenericProfileActionsJPanelLayout: GroupLayout = GroupLayout(self.blankGenericProfileActionsJPanel)
        self.blankGenericProfileActionsJPanel.setLayout(blankGenericProfileActionsJPanelLayout)
        blankGenericProfileActionsJPanelLayout.setHorizontalGroup(blankGenericProfileActionsJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE))
        blankGenericProfileActionsJPanelLayout.setVerticalGroup(blankGenericProfileActionsJPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 275, Short.MAX_VALUE))
        self.genericJTabbedPane.addTab("Actions", self.blankGenericProfileActionsJPanel)
        self.add(self.genericJTabbedPane)
    

    def savedCaptureJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            if self.savedCaptureJRadioButton.isSelected():
                self.logUtil.putF("Selected", self, "savedCaptureJRadioButtonActionPerformed")
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.SAVED_CAPTURE)
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.SCREEN_CAPTURE)
                self.screenCaptureJRadioButton.setSelected(False)
                self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "savedCaptureJRadioButtonActionPerformed", e)
    

    def screenCaptureJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            if self.screenCaptureJRadioButton.isSelected():
                self.logUtil.putF("Selected", self, "screenCaptureJRadioButtonActionPerformed")
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.SCREEN_CAPTURE)
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.SAVED_CAPTURE)
                self.savedCaptureJRadioButton.setSelected(False)
                self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "screenCaptureJRadioButtonActionPerformed", e)
    

    def captureMotionAnalysisJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        try:
            if self.captureMotionAnalysisJCheckBox.isSelected():
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.MOTION)
            else:
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.MOTION)
            self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "captureComparisonJCheckBoxActionPerformed", e)
    

    def captureComparisonJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        try:
            if self.captureComparisonJCheckBox.isSelected():
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.COMPARISON)
            else:
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.COMPARISON)
            self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "captureComparisonJCheckBoxActionPerformed", e)
    

    # throws Exception
    def updateProfileUI(self, profileNameString: str) -> None:
        self.getBlankGenericProfileActionsJPanel().removeAll()
        if profileNameString is not None:
            genericProfileActionsJPanel: GenericProfileActionsJPanel = GenericProfileActionsJPanel()
            self.setSelectedGenericProfile(self.getGenericProfiles().get(profileNameString))
            self.getSelectedGenericProfile().setGenericProfileActions(GenericProfileActions(genericProfileActionsJPanel, profileNameString))
            genericProfileActionsJPanel.setGenericProfileActions(self.getSelectedGenericProfile().getGenericProfileActions())
            genericProfileActionsJPanel.selectFirstElement()
            layout: GroupLayout = self.getBlankGenericProfileActionsJPanel().getLayout()
            layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE).addComponent(genericProfileActionsJPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
            layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGap(0, 256, Short.MAX_VALUE).addComponent(genericProfileActionsJPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
            self.updateProfileOptions()
            self.logUtil.putF("Setting Configuration Profile JPanel", self, "updateProfileUI")
        else:
            self.logUtil.putF("Null Configuration Profile", self, "updateProfileUI")
    

    # throws Exception
    def selectFirstElement(self) -> None:
        self.genericProfilesJList.setModel(self.getGenericProfiles().getDefaultListModelHelper().getListModel())
        if self.genericProfilesJList.getModel().getSize() > 0:
            self.genericProfilesJList.setSelectedValue(self.genericProfilesJList.getModel().getElementAt(0), True)
            self.updateProfileUI(self.genericProfilesJList.getModel().getElementAt(0))
    

    # throws Exception
    def updateProfileOptions(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "updateProfileOptions")
        genericProfile: GenericProfile = self.getSelectedGenericProfile()
        vector: BasicArrayList = genericProfile.getGenericProfileDataWorkerTypeVector()
        self.screenCaptureJRadioButton.setSelected(False)
        self.savedCaptureJRadioButton.setSelected(False)
        self.captureComparisonJCheckBox.setSelected(False)
        self.captureMotionAnalysisJCheckBox.setSelected(False)
        size: int = vector.size()
        for index in range(0, size):
            genericProfileDataWorkerType: GenericProfileDataWorkerType = vector.get(index)
            self.logUtil.putF(genericProfile.getName() + " has GenericProfileDataWorkerType: " + str(genericProfileDataWorkerType), self, "updateProfileOptions")
            if genericProfileDataWorkerType == GenericProfileDataWorkerType.SCREEN_CAPTURE:
                self.logUtil.putF("Screen Capture Selected", self, "updateProfileOptions")
                self.screenCaptureJRadioButton.setSelected(True)
            elif genericProfileDataWorkerType == GenericProfileDataWorkerType.SAVED_CAPTURE:
                self.logUtil.putF("Saved Capture Selected", self, "updateProfileOptions")
                self.savedCaptureJRadioButton.setSelected(True)
            elif genericProfileDataWorkerType == GenericProfileDataWorkerType.COMPARISON:
                self.logUtil.putF("Checking Comparison Box", self, "updateProfileOptions")
                self.captureComparisonJCheckBox.setSelected(True)
            elif genericProfileDataWorkerType == GenericProfileDataWorkerType.MOTION:
                self.logUtil.putF("Checking Motion Box", self, "updateProfileOptions")
                self.captureMotionAnalysisJCheckBox.setSelected(True)
        if not self.screenCaptureJRadioButton.isSelected() and not self.savedCaptureJRadioButton.isSelected():
            self.screenCaptureJRadioButton.setSelected(True)
            self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.SCREEN_CAPTURE)
        self.logUtil.putF(self.commonStrings.END, self, "updateProfileOptions")
    

    def getBlankGenericProfileActionsJPanel(self) -> JPanel:
        return self.blankGenericProfileActionsJPanel
    

    def setBlankGenericProfileActionsJPanel(self, blankGenericProfileActionsJPanel: JPanel) -> None:
        self.blankGenericProfileActionsJPanel = blankGenericProfileActionsJPanel
    

    def getGenericProfiles(self) -> GenericProfiles:
        return self.genericProfiles
    

    def setGenericProfiles(self, genericProfiles: GenericProfiles) -> None:
        self.genericProfiles = genericProfiles
    

    def getSelectedGenericProfile(self) -> GenericProfile:
        return self.selectedGenericProfile
    

    def setSelectedGenericProfile(self, selectedGenericProfile: GenericProfile) -> None:
        self.selectedGenericProfile = selectedGenericProfile
    

    def genericProfilesJListValueChanged(self, evt: ListSelectionEvent) -> None:
        try:
            profileNameString: str = self.genericProfilesJList.getSelectedValue()
            self.updateProfileUI(profileNameString)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "genericProfilesJListValueChanged", e)
    

    def deleteProfileJButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            anyType: list[object] = self.genericProfilesJList.getSelectedValues()
            for index in range(0, len(anyType)):
                nextSelectedValueString: str = anyType[index]
                self.getGenericProfiles().remove(nextSelectedValueString)
            self.selectFirstElement()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "deleteProfileJButtonActionPerformed", e)
    

    def okNewProfileJButtonActionPerformed(self, evt: ActionEvent) -> None:
        try:
            newProfileName: str = self.newProfileNameJTextField.getText()
            self.getGenericProfiles().add(newProfileName)
            self.genericProfilesJList.setModel(self.getGenericProfiles().getDefaultListModelHelper().getListModel())
            self.genericProfilesJList.setSelectedValue(newProfileName, True)
            self.newProfileJDialog.setVisible(False)
            self.updateProfileUI(newProfileName)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "okNewProfileJButtonActionPerformed", e)
    

    def newProfileJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.newProfileJDialog.setVisible(True)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfiles import GenericProfiles
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActions import GenericProfileActions
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionsJPanel import GenericProfileActionsJPanel
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


