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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
# from javax.swing.JPanel import JPanel
from org.allbinary.input.automation.module.generic.configuration.GenericModuleConfigurationInterface import GenericModuleConfigurationInterface


@java_inherited_overloads
class GenericModuleConfigurationJPanel(*java_bases(JPanel, GenericModuleConfigurationInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("stringUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("genericProfiles", None)
        vars(self).setdefault("selectedGenericProfile", None)
        vars(self).setdefault("blankGenericProfileActionsJPanel", None)
        vars(self).setdefault("buttonGroup2", None)
        vars(self).setdefault("captureComparisonJCheckBox", None)
        vars(self).setdefault("captureMotionAnalysisJCheckBox", None)
        vars(self).setdefault("deleteProfileJButton", None)
        vars(self).setdefault("genericJTabbedPane", None)
        vars(self).setdefault("genericProfilesJList", None)
        vars(self).setdefault("genericProfilesJPanel", None)
        vars(self).setdefault("genericProfilesJScrollPane", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("jLabel3", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("newProfileJButton", None)
        vars(self).setdefault("newProfileJDialog", None)
        vars(self).setdefault("newProfileNameJLabel", None)
        vars(self).setdefault("newProfileNameJTextField", None)
        vars(self).setdefault("okNewProfileJButton", None)
        vars(self).setdefault("savedCaptureJRadioButton", None)
        vars(self).setdefault("screenCaptureJRadioButton", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "genericProfiles" not in vars(self): self.genericProfiles: GenericProfiles = None
        if "selectedGenericProfile" not in vars(self): self.selectedGenericProfile: GenericProfile = None
        if "blankGenericProfileActionsJPanel" not in vars(self): self.blankGenericProfileActionsJPanel: JPanel = None
        if "buttonGroup2" not in vars(self): self.buttonGroup2: ButtonGroup = None
        if "captureComparisonJCheckBox" not in vars(self): self.captureComparisonJCheckBox: JCheckBox = None
        if "captureMotionAnalysisJCheckBox" not in vars(self): self.captureMotionAnalysisJCheckBox: JCheckBox = None
        if "deleteProfileJButton" not in vars(self): self.deleteProfileJButton: JButton = None
        if "genericJTabbedPane" not in vars(self): self.genericJTabbedPane: JTabbedPane = None
        if "genericProfilesJList" not in vars(self): self.genericProfilesJList: JList = None
        if "genericProfilesJPanel" not in vars(self): self.genericProfilesJPanel: JPanel = None
        if "genericProfilesJScrollPane" not in vars(self): self.genericProfilesJScrollPane: JScrollPane = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "jLabel3" not in vars(self): self.jLabel3: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "newProfileJButton" not in vars(self): self.newProfileJButton: JButton = None
        if "newProfileJDialog" not in vars(self): self.newProfileJDialog: JDialog = None
        if "newProfileNameJLabel" not in vars(self): self.newProfileNameJLabel: JLabel = None
        if "newProfileNameJTextField" not in vars(self): self.newProfileNameJTextField: JTextField = None
        if "okNewProfileJButton" not in vars(self): self.okNewProfileJButton: JButton = None
        if "savedCaptureJRadioButton" not in vars(self): self.savedCaptureJRadioButton: JRadioButton = None
        if "screenCaptureJRadioButton" not in vars(self): self.screenCaptureJRadioButton: JRadioButton = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfiles import GenericProfiles
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        self.setGenericProfiles(GenericProfiles(GenericProfiles.DEFAULT_FILE))
        self.selectFirstElement()
    

    def initComponents(self) -> None:
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
        _java_listener_owner = self
        class _JavaListenerN67566(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "okNewProfileJButtonActionPerformed") else _java_listener_owner).okNewProfileJButtonActionPerformed(evt)
        self.okNewProfileJButton.addActionListener(_JavaListenerN67566()
            )
        self.newProfileNameJLabel.setText("New Profile Name")
        newProfileJDialogLayout: GroupLayout = GroupLayout(self.newProfileJDialog.getContentPane())
        self.newProfileJDialog.getContentPane().setLayout(newProfileJDialogLayout)
        newProfileJDialogLayout.setHorizontalGroup(newProfileJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(newProfileJDialogLayout.createSequentialGroup().addGroup(newProfileJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(80, 80, 80).addComponent(self.newProfileNameJLabel)).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(30, 30, 30).addComponent(self.newProfileNameJTextField, GroupLayout.PREFERRED_SIZE, 180, GroupLayout.PREFERRED_SIZE)).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(100, 100, 100).addComponent(self.okNewProfileJButton))).addContainerGap(35, Short.MAX_VALUE)))
        newProfileJDialogLayout.setVerticalGroup(newProfileJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(newProfileJDialogLayout.createSequentialGroup().addGap(10, 10, 10).addComponent(self.newProfileNameJLabel).addGap(16, 16, 16).addComponent(self.newProfileNameJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addGap(20, 20, 20).addComponent(self.okNewProfileJButton)))
        self.setLayout(GridLayout(1, 0))
        self.setMinimumSize(Dimension(400, 300))
        self.setPreferredSize(Dimension(700, 700))
        self.genericJTabbedPane.setToolTipText(self.stringUtil.EMPTY_STRING)
        self.genericJTabbedPane.setMinimumSize(Dimension(800, 600))
        self.genericProfilesJPanel.setMinimumSize(Dimension(400, 300))
        self.genericProfilesJPanel.setPreferredSize(Dimension(0, 0))
        _java_listener_owner = self
        class _JavaListenerN68802(ListSelectionListener):
            
            

            def valueChanged(self, evt: ListSelectionEvent) -> None:
                (self if hasattr(self, "genericProfilesJListValueChanged") else _java_listener_owner).genericProfilesJListValueChanged(evt)
        self.genericProfilesJList.addListSelectionListener(_JavaListenerN68802()
            )
        self.genericProfilesJScrollPane.setViewportView(self.genericProfilesJList)
        self.newProfileJButton.setText("New")
        self.newProfileJButton.setToolTipText("Creates a new profile")
        _java_listener_owner = self
        class _JavaListenerN69008(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "newProfileJButtonActionPerformed") else _java_listener_owner).newProfileJButtonActionPerformed(evt)
        self.newProfileJButton.addActionListener(_JavaListenerN69008()
            )
        self.deleteProfileJButton.setText("Delete")
        self.deleteProfileJButton.setToolTipText("Deletes the selected profile")
        _java_listener_owner = self
        class _JavaListenerN69177(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "deleteProfileJButtonActionPerformed") else _java_listener_owner).deleteProfileJButtonActionPerformed(evt)
        self.deleteProfileJButton.addActionListener(_JavaListenerN69177()
            )
        self.jPanel1.setPreferredSize(Dimension(1000, 100))
        self.screenCaptureJRadioButton.setText("Screen Captures")
        self.screenCaptureJRadioButton.setToolTipText("Records the screen into memory for logical processing")
        self.screenCaptureJRadioButton.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.screenCaptureJRadioButton.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN69513(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "screenCaptureJRadioButtonActionPerformed") else _java_listener_owner).screenCaptureJRadioButtonActionPerformed(evt)
        self.screenCaptureJRadioButton.addActionListener(_JavaListenerN69513()
            )
        self.jLabel1.setText("Profile Options")
        self.jLabel2.setText("Process From:")
        self.savedCaptureJRadioButton.setText("Saved Images")
        self.savedCaptureJRadioButton.setToolTipText("Loads images from files for logical processing.  Usually for debugging your profile actions")
        self.savedCaptureJRadioButton.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.savedCaptureJRadioButton.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN69860(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "savedCaptureJRadioButtonActionPerformed") else _java_listener_owner).savedCaptureJRadioButtonActionPerformed(evt)
        self.savedCaptureJRadioButton.addActionListener(_JavaListenerN69860()
            )
        self.captureMotionAnalysisJCheckBox.setText("Motion Analysis")
        self.captureMotionAnalysisJCheckBox.setToolTipText("Uses image comparison and contraints to locate moving objects")
        self.captureMotionAnalysisJCheckBox.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.captureMotionAnalysisJCheckBox.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN70147(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "captureMotionAnalysisJCheckBoxActionPerformed") else _java_listener_owner).captureMotionAnalysisJCheckBoxActionPerformed(evt)
        self.captureMotionAnalysisJCheckBox.addActionListener(_JavaListenerN70147()
            )
        self.captureComparisonJCheckBox.setText("Comparison")
        self.captureComparisonJCheckBox.setToolTipText("Compares the last two input images for multi image logic")
        self.captureComparisonJCheckBox.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.captureComparisonJCheckBox.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN70434(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "captureComparisonJCheckBoxActionPerformed") else _java_listener_owner).captureComparisonJCheckBoxActionPerformed(evt)
        self.captureComparisonJCheckBox.addActionListener(_JavaListenerN70434()
            )
        self.jLabel3.setText("Image Processing:")
        self.jLabel3.setToolTipText("Turns on/off various extended image processing")
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.screenCaptureJRadioButton).addComponent(self.jLabel1).addComponent(self.jLabel2).addComponent(self.savedCaptureJRadioButton).addComponent(self.captureMotionAnalysisJCheckBox).addComponent(self.captureComparisonJCheckBox).addComponent(self.jLabel3)).addContainerGap(22, Short.MAX_VALUE)))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel2).addGap(7, 7, 7).addComponent(self.screenCaptureJRadioButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.savedCaptureJRadioButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel3).addGap(7, 7, 7).addComponent(self.captureComparisonJCheckBox).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.captureMotionAnalysisJCheckBox).addContainerGap(106, Short.MAX_VALUE)))
        genericProfilesJPanelLayout: GroupLayout = GroupLayout(self.genericProfilesJPanel)
        self.genericProfilesJPanel.setLayout(genericProfilesJPanelLayout)
        genericProfilesJPanelLayout.setHorizontalGroup(genericProfilesJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addGroup(genericProfilesJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addComponent(self.newProfileJButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.deleteProfileJButton)).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addComponent(self.genericProfilesJScrollPane, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, GroupLayout.DEFAULT_SIZE, 119, Short.MAX_VALUE))).addContainerGap()))
        genericProfilesJPanelLayout.setVerticalGroup(genericProfilesJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(genericProfilesJPanelLayout.createSequentialGroup().addGroup(genericProfilesJPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.newProfileJButton).addComponent(self.deleteProfileJButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(genericProfilesJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.jPanel1, GroupLayout.DEFAULT_SIZE, 246, Short.MAX_VALUE).addComponent(self.genericProfilesJScrollPane, GroupLayout.DEFAULT_SIZE, 246, Short.MAX_VALUE))))
        self.genericJTabbedPane.addTab("Profiles", self.genericProfilesJPanel)
        blankGenericProfileActionsJPanelLayout: GroupLayout = GroupLayout(self.blankGenericProfileActionsJPanel)
        self.blankGenericProfileActionsJPanel.setLayout(blankGenericProfileActionsJPanelLayout)
        blankGenericProfileActionsJPanelLayout.setHorizontalGroup(blankGenericProfileActionsJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE))
        blankGenericProfileActionsJPanelLayout.setVerticalGroup(blankGenericProfileActionsJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 275, Short.MAX_VALUE))
        self.genericJTabbedPane.addTab("Actions", self.blankGenericProfileActionsJPanel)
        self.add(self.genericJTabbedPane)
    

    def savedCaptureJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
        try:
            if java_predicate(self.savedCaptureJRadioButton, "isSelected"):
                self.logUtil.putF("Selected", self, "savedCaptureJRadioButtonActionPerformed")
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.SAVED_CAPTURE)
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.SCREEN_CAPTURE)
                self.screenCaptureJRadioButton.setSelected(False)
                self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "savedCaptureJRadioButtonActionPerformed", e)
    

    def screenCaptureJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
        try:
            if java_predicate(self.screenCaptureJRadioButton, "isSelected"):
                self.logUtil.putF("Selected", self, "screenCaptureJRadioButtonActionPerformed")
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.SCREEN_CAPTURE)
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.SAVED_CAPTURE)
                self.savedCaptureJRadioButton.setSelected(False)
                self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "screenCaptureJRadioButtonActionPerformed", e)
    

    def captureMotionAnalysisJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
        try:
            if java_predicate(self.captureMotionAnalysisJCheckBox, "isSelected"):
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.MOTION)
            else:
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.MOTION)
            self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "captureComparisonJCheckBoxActionPerformed", e)
    

    def captureComparisonJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
        try:
            if java_predicate(self.captureComparisonJCheckBox, "isSelected"):
                self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.COMPARISON)
            else:
                self.getSelectedGenericProfile().remove(GenericProfileDataWorkerType.COMPARISON)
            self.getGenericProfiles().save()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "captureComparisonJCheckBoxActionPerformed", e)
    

    # throws Exception
    def updateProfileUI(self, profileNameString: str) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActions import GenericProfileActions
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionsJPanel import GenericProfileActionsJPanel
        self.getBlankGenericProfileActionsJPanel().removeAll()
        if profileNameString is not None:
            genericProfileActionsJPanel: GenericProfileActionsJPanel = GenericProfileActionsJPanel()
            self.setSelectedGenericProfile(self.getGenericProfiles().get(profileNameString))
            self.getSelectedGenericProfile().setGenericProfileActions(GenericProfileActions(genericProfileActionsJPanel, profileNameString))
            genericProfileActionsJPanel.setGenericProfileActions(self.getSelectedGenericProfile().getGenericProfileActions())
            genericProfileActionsJPanel.selectFirstElement()
            layout: GroupLayout = self.getBlankGenericProfileActionsJPanel().getLayout()
            layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE).addComponent(genericProfileActionsJPanel, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
            layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 256, Short.MAX_VALUE).addComponent(genericProfileActionsJPanel, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
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
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
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
        if not (java_predicate(self.screenCaptureJRadioButton, "isSelected")) and not (java_predicate(self.savedCaptureJRadioButton, "isSelected")):
            self.screenCaptureJRadioButton.setSelected(True)
            self.getSelectedGenericProfile().add(GenericProfileDataWorkerType.SCREEN_CAPTURE)
        self.logUtil.putF(self.commonStrings.END, self, "updateProfileOptions")
    

    def getBlankGenericProfileActionsJPanel(self) -> JPanel:
        return self.blankGenericProfileActionsJPanel
    

    def setBlankGenericProfileActionsJPanel(self, blankGenericProfileActionsJPanel: JPanel) -> None:
        self.blankGenericProfileActionsJPanel = blankGenericProfileActionsJPanel
    

    def getGenericProfiles(self) -> GenericProfiles:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfiles import GenericProfiles
        return self.genericProfiles
    

    def setGenericProfiles(self, genericProfiles: GenericProfiles) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfiles import GenericProfiles
        self.genericProfiles = genericProfiles
    

    def getSelectedGenericProfile(self) -> GenericProfile:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
        return self.selectedGenericProfile
    

    def setSelectedGenericProfile(self, selectedGenericProfile: GenericProfile) -> None:
        from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
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
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
# from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
# from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfiles import GenericProfiles
# from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActions import GenericProfileActions
# from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionsJPanel import GenericProfileActionsJPanel
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.GridLayout import GridLayout
# from java.awt.Insets import Insets
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.BorderFactory import BorderFactory
# from javax.swing.ButtonGroup import ButtonGroup
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JCheckBox import JCheckBox
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.JList import JList
# from javax.swing.JRadioButton import JRadioButton
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.JTabbedPane import JTabbedPane
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle
# from javax.swing.event.ListSelectionEvent import ListSelectionEvent
# from javax.swing.event.ListSelectionListener import ListSelectionListener


