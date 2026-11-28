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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class ImageActionScriptOutputJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("capturedImageActionScriptOutputInterface", None)
        vars(self).setdefault("capturedImageActionJButton", None)
        vars(self).setdefault("capturedImageActionJDialog", None)
        vars(self).setdefault("displayJCheckBox", None)
        vars(self).setdefault("itemTypesJList", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jScrollPane1", None)
        vars(self).setdefault("okJButton", None)
        vars(self).setdefault("saveJCheckBox", None)
        vars(self).setdefault("titleJLabel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "capturedImageActionScriptOutputInterface" not in vars(self): self.capturedImageActionScriptOutputInterface: ImageActionScriptOutputInterface = None
        if "capturedImageActionJButton" not in vars(self): self.capturedImageActionJButton: JButton = None
        if "capturedImageActionJDialog" not in vars(self): self.capturedImageActionJDialog: JDialog = None
        if "displayJCheckBox" not in vars(self): self.displayJCheckBox: JCheckBox = None
        if "itemTypesJList" not in vars(self): self.itemTypesJList: JList = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jScrollPane1" not in vars(self): self.jScrollPane1: JScrollPane = None
        if "okJButton" not in vars(self): self.okJButton: JButton = None
        if "saveJCheckBox" not in vars(self): self.saveJCheckBox: JCheckBox = None
        if "titleJLabel" not in vars(self): self.titleJLabel: JLabel = None
    

    def __init__(self, capturedImageActionScriptOutputInterface: ImageActionScriptOutputInterface) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.capturedImageActionScriptOutputInterface = capturedImageActionScriptOutputInterface
        self.set()
    

    def set(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.input.media.image.InputImageType import InputImageType
        self.setImageTypeJlistModel()
        imageTypes: ImageTypes = self.capturedImageActionScriptOutputInterface.getImageTypes()
        vector: BasicArrayList = imageTypes.getVector()
        selectedArray: list[int] = [0] * (vector.size())
        size: int = vector.size()
        for index in range(0, size):
            imageType: InputImageType = vector.get(index)
            selectedArray[((index := index + 1) - 1)] = imageType.getIndex()
        self.itemTypesJList.setSelectedIndices(selectedArray)
        if java_predicate(self.capturedImageActionScriptOutputInterface, "isSaved"):
            self.saveJCheckBox.setSelected(True)
        if java_predicate(self.capturedImageActionScriptOutputInterface, "isSaved"):
            self.displayJCheckBox.setSelected(True)
        self.capturedImageActionScriptOutputInterface.log()
    

    def update(self) -> None:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageTypes import ImageTypes
        anyType: list[object] = self.itemTypesJList.getSelectedValues()
        imageTypes: ImageTypes = ImageTypes.valueOf(anyType)
        self.capturedImageActionScriptOutputInterface.setImageTypes(imageTypes)
        if java_predicate(self.saveJCheckBox, "isSelected"):
            self.capturedImageActionScriptOutputInterface.setSaved(True)
        else:
            self.capturedImageActionScriptOutputInterface.setSaved(False)
        if java_predicate(self.displayJCheckBox, "isSelected"):
            self.capturedImageActionScriptOutputInterface.setDisplay(True)
        else:
            self.capturedImageActionScriptOutputInterface.setDisplay(False)
        self.capturedImageActionScriptOutputInterface.log()
    

    def setImageTypeJlistModel(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.input.media.image.InputImageType import InputImageType
        defaultListModel: DefaultListModel = DefaultListModel()
        vector: BasicArrayList = InputImageType.getAllAsVector()
        size: int = vector.size()
        for index in range(0, size):
            imageType: InputImageType = vector.get(index)
            defaultListModel.addElement(imageType.getName())
        self.itemTypesJList.setModel(defaultListModel)
    

    def getCapturedImageActionJDialog(self) -> JDialog:
        return self.capturedImageActionJDialog
    

    def setCapturedImageActionJDialog(self, capturedImageActionJDialog: JDialog) -> None:
        self.capturedImageActionJDialog = capturedImageActionJDialog
    

    def initComponents(self) -> None:
        self.capturedImageActionJDialog = JDialog()
        self.titleJLabel = JLabel()
        self.okJButton = JButton()
        self.saveJCheckBox = JCheckBox()
        self.displayJCheckBox = JCheckBox()
        self.jScrollPane1 = JScrollPane()
        self.itemTypesJList = JList()
        self.capturedImageActionJButton = JButton()
        self.jLabel1 = JLabel()
        self.capturedImageActionJDialog.setMinimumSize(Dimension(250, 250))
        self.titleJLabel.setText("Image Output Options")
        self.okJButton.setText("OK")
        _java_listener_owner = self
        class _JavaListenerN68305(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "okJButtonActionPerformed") else _java_listener_owner).okJButtonActionPerformed(evt)
        self.okJButton.addActionListener(_JavaListenerN68305()
            )
        self.saveJCheckBox.setText("Save To File")
        self.saveJCheckBox.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.saveJCheckBox.setMargin(Insets(0, 0, 0, 0))
        self.displayJCheckBox.setText("Display")
        self.displayJCheckBox.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0))
        self.displayJCheckBox.setMargin(Insets(0, 0, 0, 0))
        _java_listener_owner = self
        class _JavaListenerN68710(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "displayJCheckBoxActionPerformed") else _java_listener_owner).displayJCheckBoxActionPerformed(evt)
        self.displayJCheckBox.addActionListener(_JavaListenerN68710()
            )
        self.itemTypesJList.setModel((AbstractListModel()  # Java anonymous class body:
#             self.strings: list[str] = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
#             
# 
#             def getSize(self) -> int:
#                 return len(self.strings)
#             
# 
#             def getElementAt(self, i: int) -> object:
#                 return self.strings[i]
))
        self.jScrollPane1.setViewportView(self.itemTypesJList)
        capturedImageActionJDialogLayout: GroupLayout = GroupLayout(self.capturedImageActionJDialog.getContentPane())
        self.capturedImageActionJDialog.getContentPane().setLayout(capturedImageActionJDialogLayout)
        capturedImageActionJDialogLayout.setHorizontalGroup(capturedImageActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(capturedImageActionJDialogLayout.createSequentialGroup().addGroup(capturedImageActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(capturedImageActionJDialogLayout.createSequentialGroup().addGap(61, 61, 61).addComponent(self.titleJLabel)).addGroup(capturedImageActionJDialogLayout.createSequentialGroup().addContainerGap().addGroup(capturedImageActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(capturedImageActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.displayJCheckBox).addComponent(self.saveJCheckBox, GroupLayout.Alignment.TRAILING)).addGroup(capturedImageActionJDialogLayout.createSequentialGroup().addGap(84, 84, 84).addComponent(self.okJButton)))).addGroup(capturedImageActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.jScrollPane1, GroupLayout.DEFAULT_SIZE, 216, Short.MAX_VALUE))).addContainerGap()))
        capturedImageActionJDialogLayout.setVerticalGroup(capturedImageActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(capturedImageActionJDialogLayout.createSequentialGroup().addComponent(self.titleJLabel).addGap(5, 5, 5).addComponent(self.jScrollPane1, GroupLayout.DEFAULT_SIZE, 105, Short.MAX_VALUE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.saveJCheckBox).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.displayJCheckBox).addGap(9, 9, 9).addComponent(self.okJButton).addContainerGap()))
        self.setMinimumSize(Dimension(100, 0))
        self.capturedImageActionJButton.setText("Edit")
        _java_listener_owner = self
        class _JavaListenerN70175(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "capturedImageActionJButtonActionPerformed") else _java_listener_owner).capturedImageActionJButtonActionPerformed(evt)
        self.capturedImageActionJButton.addActionListener(_JavaListenerN70175()
            )
        self.jLabel1.setText("Capture Image:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.capturedImageActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.capturedImageActionJButton)))
    

    def displayJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.update()
        self.getCapturedImageActionJDialog().setVisible(False)
    

    def capturedImageActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getCapturedImageActionJDialog().setVisible(True)
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.swing.DefaultListModel import DefaultListModel
# from org.allbinary.input.media.image.InputImageType import InputImageType
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.Insets import Insets
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.AbstractListModel import AbstractListModel
# from javax.swing.BorderFactory import BorderFactory
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JCheckBox import JCheckBox
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.JList import JList
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.LayoutStyle import LayoutStyle


