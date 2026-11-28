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
# package org.allbinary.input.automation.actions.script.condition

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class ColorAtActionScriptConditionJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("colorAtActionScriptConditionInterface", None)
        vars(self).setdefault("blueJLabel", None)
        vars(self).setdefault("colorAtActionJButton", None)
        vars(self).setdefault("colorAtActionJDialog", None)
        vars(self).setdefault("colorAtXJTextField", None)
        vars(self).setdefault("colorAtYJTextField", None)
        vars(self).setdefault("colorRangeJLabel", None)
        vars(self).setdefault("greenJLabel", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("locationJLabel", None)
        vars(self).setdefault("maxBlueJTextField", None)
        vars(self).setdefault("maxGreenJTextField", None)
        vars(self).setdefault("maxJLabel", None)
        vars(self).setdefault("maxRedJTextField", None)
        vars(self).setdefault("minBlueJTextField", None)
        vars(self).setdefault("minGreenJTextField", None)
        vars(self).setdefault("minJLabel", None)
        vars(self).setdefault("minRedJTextField", None)
        vars(self).setdefault("okJButton", None)
        vars(self).setdefault("redJLabel", None)
        vars(self).setdefault("titleJLabel", None)
        vars(self).setdefault("xJLabel", None)
        vars(self).setdefault("yJLabel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "colorAtActionScriptConditionInterface" not in vars(self): self.colorAtActionScriptConditionInterface: ColorAtActionScriptConditionInterface = None
        if "blueJLabel" not in vars(self): self.blueJLabel: JLabel = None
        if "colorAtActionJButton" not in vars(self): self.colorAtActionJButton: JButton = None
        if "colorAtActionJDialog" not in vars(self): self.colorAtActionJDialog: JDialog = None
        if "colorAtXJTextField" not in vars(self): self.colorAtXJTextField: JTextField = None
        if "colorAtYJTextField" not in vars(self): self.colorAtYJTextField: JTextField = None
        if "colorRangeJLabel" not in vars(self): self.colorRangeJLabel: JLabel = None
        if "greenJLabel" not in vars(self): self.greenJLabel: JLabel = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "locationJLabel" not in vars(self): self.locationJLabel: JLabel = None
        if "maxBlueJTextField" not in vars(self): self.maxBlueJTextField: JTextField = None
        if "maxGreenJTextField" not in vars(self): self.maxGreenJTextField: JTextField = None
        if "maxJLabel" not in vars(self): self.maxJLabel: JLabel = None
        if "maxRedJTextField" not in vars(self): self.maxRedJTextField: JTextField = None
        if "minBlueJTextField" not in vars(self): self.minBlueJTextField: JTextField = None
        if "minGreenJTextField" not in vars(self): self.minGreenJTextField: JTextField = None
        if "minJLabel" not in vars(self): self.minJLabel: JLabel = None
        if "minRedJTextField" not in vars(self): self.minRedJTextField: JTextField = None
        if "okJButton" not in vars(self): self.okJButton: JButton = None
        if "redJLabel" not in vars(self): self.redJLabel: JLabel = None
        if "titleJLabel" not in vars(self): self.titleJLabel: JLabel = None
        if "xJLabel" not in vars(self): self.xJLabel: JLabel = None
        if "yJLabel" not in vars(self): self.yJLabel: JLabel = None
    

    def __init__(self, colorAtActionScriptConditionInterface: ColorAtActionScriptConditionInterface) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.colorAtActionScriptConditionInterface = colorAtActionScriptConditionInterface
        self.set()
    

    def set(self) -> None:
        from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
        colorRangeInterface: ColorRangeInterface = self.colorAtActionScriptConditionInterface.getColorRangeInterface()
        self.getMinRedJTextField().setText(str(colorRangeInterface.getMinRed()))
        self.getMaxRedJTextField().setText(str(colorRangeInterface.getMaxRed()))
        self.getMinGreenJTextField().setText(str(colorRangeInterface.getMinGreen()))
        self.getMaxGreenJTextField().setText(str(colorRangeInterface.getMaxGreen()))
        self.getMinBlueJTextField().setText(str(colorRangeInterface.getMinBlue()))
        self.getMaxBlueJTextField().setText(str(colorRangeInterface.getMaxBlue()))
        self.getColorAtXJTextField().setText(str(self.colorAtActionScriptConditionInterface.getPoint().x))
        self.getColorAtYJTextField().setText(str(self.colorAtActionScriptConditionInterface.getPoint().y))
        self.colorAtActionScriptConditionInterface.log()
    

    def update(self) -> None:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
        colorRangeInterface: ColorRangeInterface = self.colorAtActionScriptConditionInterface.getColorRangeInterface()
        colorRangeInterface.setMinRed(int(str(self.getMinRedJTextField().getText())))
        colorRangeInterface.setMaxRed(int(str(self.getMaxRedJTextField().getText())))
        colorRangeInterface.setMinGreen(int(str(self.getMinGreenJTextField().getText())))
        colorRangeInterface.setMaxGreen(int(str(self.getMaxGreenJTextField().getText())))
        colorRangeInterface.setMinBlue(int(str(self.getMinBlueJTextField().getText())))
        colorRangeInterface.setMaxBlue(int(str(self.getMaxBlueJTextField().getText())))
        xString: str = self.getColorAtXJTextField().getText()
        if not (StringValidationUtil.getInstance().isEmpty(xString)) and StringValidationUtil.getInstance().isNumber(xString):
            self.colorAtActionScriptConditionInterface.getPoint().x = int(xString)
        yString: str = self.getColorAtYJTextField().getText()
        if not (StringValidationUtil.getInstance().isEmpty(yString)) and StringValidationUtil.getInstance().isNumber(yString):
            self.colorAtActionScriptConditionInterface.getPoint().y = int(xString)
        self.colorAtActionScriptConditionInterface.log()
    

    def getColorAtXJTextField(self) -> JTextField:
        return self.colorAtXJTextField
    

    def setColorAtXJTextField(self, colorAtXJTextField: JTextField) -> None:
        self.colorAtXJTextField = colorAtXJTextField
    

    def getColorAtYJTextField(self) -> JTextField:
        return self.colorAtYJTextField
    

    def setColorAtYJTextField(self, colorAtYJTextField: JTextField) -> None:
        self.colorAtYJTextField = colorAtYJTextField
    

    def getMaxBlueJTextField(self) -> JTextField:
        return self.maxBlueJTextField
    

    def setMaxBlueJTextField(self, maxBlueJTextField: JTextField) -> None:
        self.maxBlueJTextField = maxBlueJTextField
    

    def getMaxGreenJTextField(self) -> JTextField:
        return self.maxGreenJTextField
    

    def setMaxGreenJTextField(self, maxGreenJTextField: JTextField) -> None:
        self.maxGreenJTextField = maxGreenJTextField
    

    def getMaxRedJTextField(self) -> JTextField:
        return self.maxRedJTextField
    

    def setMaxRedJTextField(self, maxRedJTextField: JTextField) -> None:
        self.maxRedJTextField = maxRedJTextField
    

    def getMinBlueJTextField(self) -> JTextField:
        return self.minBlueJTextField
    

    def setMinBlueJTextField(self, minBlueJTextField: JTextField) -> None:
        self.minBlueJTextField = minBlueJTextField
    

    def getMinGreenJTextField(self) -> JTextField:
        return self.minGreenJTextField
    

    def setMinGreenJTextField(self, minGreenJTextField: JTextField) -> None:
        self.minGreenJTextField = minGreenJTextField
    

    def getMinRedJTextField(self) -> JTextField:
        return self.minRedJTextField
    

    def setMinRedJTextField(self, minRedJTextField: JTextField) -> None:
        self.minRedJTextField = minRedJTextField
    

    def getYJLabel(self) -> JLabel:
        return self.yJLabel
    

    def setYJLabel(self, yJLabel: JLabel) -> None:
        self.yJLabel = yJLabel
    

    def getColorAtActionJDialog(self) -> JDialog:
        return self.colorAtActionJDialog
    

    def setColorAtActionJDialog(self, colorAtActionJDialog: JDialog) -> None:
        self.colorAtActionJDialog = colorAtActionJDialog
    

    def initComponents(self) -> None:
        self.colorAtActionJDialog = JDialog()
        self.titleJLabel = JLabel()
        self.locationJLabel = JLabel()
        self.colorAtXJTextField = JTextField()
        self.xJLabel = JLabel()
        self.yJLabel = JLabel()
        self.colorAtYJTextField = JTextField()
        self.colorRangeJLabel = JLabel()
        self.redJLabel = JLabel()
        self.minJLabel = JLabel()
        self.maxJLabel = JLabel()
        self.greenJLabel = JLabel()
        self.blueJLabel = JLabel()
        self.minRedJTextField = JTextField()
        self.maxRedJTextField = JTextField()
        self.maxGreenJTextField = JTextField()
        self.minBlueJTextField = JTextField()
        self.maxBlueJTextField = JTextField()
        self.okJButton = JButton()
        self.minGreenJTextField = JTextField()
        self.colorAtActionJButton = JButton()
        self.jLabel1 = JLabel()
        self.colorAtActionJDialog.setMinimumSize(Dimension(350, 250))
        self.titleJLabel.setText("              Color At Action Options            ")
        self.locationJLabel.setText("Location:")
        self.xJLabel.setText("X:")
        self.yJLabel.setText("Y:")
        self.colorRangeJLabel.setText("Color Range")
        self.redJLabel.setText("Red:")
        self.minJLabel.setText("Minimum")
        self.maxJLabel.setText("Maximum")
        self.greenJLabel.setText("Green:")
        self.blueJLabel.setText("Blue:")
        self.okJButton.setText("OK")
        _java_listener_owner = self
        class _JavaListenerN70055(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "okJButtonActionPerformed") else _java_listener_owner).okJButtonActionPerformed(evt)
        self.okJButton.addActionListener(_JavaListenerN70055()
            )
        colorAtActionJDialogLayout: GroupLayout = GroupLayout(self.colorAtActionJDialog.getContentPane())
        self.colorAtActionJDialog.getContentPane().setLayout(colorAtActionJDialogLayout)
        colorAtActionJDialogLayout.setHorizontalGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addContainerGap().addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.TRAILING).addComponent(self.okJButton).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.blueJLabel).addComponent(self.greenJLabel).addComponent(self.redJLabel).addComponent(self.colorRangeJLabel)).addGap(29, 29, 29)).addGroup(GroupLayout.Alignment.TRAILING, colorAtActionJDialogLayout.createSequentialGroup().addComponent(self.locationJLabel).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.xJLabel).addGap(18, 18, 18))).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.minBlueJTextField, GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE).addComponent(self.minGreenJTextField, GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE).addComponent(self.minJLabel, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.minRedJTextField, GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE).addComponent(self.colorAtXJTextField, GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE)).addGap(16, 16, 16))).addGap(6, 6, 6).addComponent(self.yJLabel).addGap(24, 24, 24).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.TRAILING).addComponent(self.maxJLabel, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addGroup(GroupLayout.Alignment.LEADING, colorAtActionJDialogLayout.createSequentialGroup().addGap(1, 1, 1).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False).addComponent(self.maxBlueJTextField, GroupLayout.Alignment.TRAILING).addComponent(self.maxRedJTextField, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 43, Short.MAX_VALUE).addComponent(self.maxGreenJTextField, GroupLayout.Alignment.TRAILING, GroupLayout.PREFERRED_SIZE, 43, GroupLayout.PREFERRED_SIZE))).addComponent(self.colorAtYJTextField, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 44, Short.MAX_VALUE)).addGap(22, 22, 22)).addGroup(GroupLayout.Alignment.TRAILING, colorAtActionJDialogLayout.createSequentialGroup().addComponent(self.titleJLabel).addGap(33, 33, 33)))))
        colorAtActionJDialogLayout.setVerticalGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.titleJLabel).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGap(15, 15, 15).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.xJLabel).addComponent(self.locationJLabel).addComponent(self.colorAtXJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.yJLabel)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.minJLabel).addComponent(self.colorRangeJLabel)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.minRedJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.redJLabel)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.greenJLabel).addComponent(self.minGreenJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.blueJLabel).addComponent(self.minBlueJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 17, Short.MAX_VALUE).addComponent(self.okJButton)).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGap(14, 14, 14).addComponent(self.colorAtYJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxJLabel).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxRedJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxGreenJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxBlueJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))).addContainerGap()))
        self.setPreferredSize(Dimension(100, 0))
        self.colorAtActionJButton.setText("Edit")
        _java_listener_owner = self
        class _JavaListenerN73808(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "colorAtActionJButtonActionPerformed") else _java_listener_owner).colorAtActionJButtonActionPerformed(evt)
        self.colorAtActionJButton.addActionListener(_JavaListenerN73808()
            )
        self.jLabel1.setText("Color At:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 15, Short.MAX_VALUE).addComponent(self.colorAtActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.colorAtActionJButton)))
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.update()
        self.getColorAtActionJDialog().setVisible(False)
    

    def colorAtActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getColorAtActionJDialog().setVisible(True)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle


