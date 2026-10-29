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

from org.allbinary.input.automation.actions.script.condition.JPanel import JPanel


class ColorAtActionScriptConditionJPanel(JPanel):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.colorAtActionScriptConditionInterface: ColorAtActionScriptConditionInterface = None
        self.blueJLabel: JLabel = None
        self.colorAtActionJButton: JButton = None
        self.colorAtActionJDialog: JDialog = None
        self.colorAtXJTextField: JTextField = None
        self.colorAtYJTextField: JTextField = None
        self.colorRangeJLabel: JLabel = None
        self.greenJLabel: JLabel = None
        self.jLabel1: JLabel = None
        self.locationJLabel: JLabel = None
        self.maxBlueJTextField: JTextField = None
        self.maxGreenJTextField: JTextField = None
        self.maxJLabel: JLabel = None
        self.maxRedJTextField: JTextField = None
        self.minBlueJTextField: JTextField = None
        self.minGreenJTextField: JTextField = None
        self.minJLabel: JLabel = None
        self.minRedJTextField: JTextField = None
        self.okJButton: JButton = None
        self.redJLabel: JLabel = None
        self.titleJLabel: JLabel = None
        self.xJLabel: JLabel = None
        self.yJLabel: JLabel = None
    

    def __init__(self, colorAtActionScriptConditionInterface: ColorAtActionScriptConditionInterface) -> None:
        super().__init__()
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.colorAtActionScriptConditionInterface = colorAtActionScriptConditionInterface
        self.set()
    

    def set(self) -> None:
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
        colorRangeInterface: ColorRangeInterface = self.colorAtActionScriptConditionInterface.getColorRangeInterface()
        colorRangeInterface.setMinRed(int(str(self.getMinRedJTextField().getText())))
        colorRangeInterface.setMaxRed(int(str(self.getMaxRedJTextField().getText())))
        colorRangeInterface.setMinGreen(int(str(self.getMinGreenJTextField().getText())))
        colorRangeInterface.setMaxGreen(int(str(self.getMaxGreenJTextField().getText())))
        colorRangeInterface.setMinBlue(int(str(self.getMinBlueJTextField().getText())))
        colorRangeInterface.setMaxBlue(int(str(self.getMaxBlueJTextField().getText())))
        xString: str = self.getColorAtXJTextField().getText()
        if not StringValidationUtil.getInstance().isEmpty(xString) and StringValidationUtil.getInstance().isNumber(xString):
            self.colorAtActionScriptConditionInterface.getPoint().x = int(xString)
        yString: str = self.getColorAtYJTextField().getText()
        if not StringValidationUtil.getInstance().isEmpty(yString) and StringValidationUtil.getInstance().isNumber(yString):
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
        from org.allbinary.input.automation.actions.script.condition.JDialog import JDialog
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.JTextField import JTextField
        from org.allbinary.input.automation.actions.script.condition.JButton import JButton
        from org.allbinary.input.automation.actions.script.condition.JLabel import JLabel
        from org.allbinary.input.automation.actions.script.condition.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.GroupLayout import GroupLayout
        from org.allbinary.input.automation.actions.script.condition.Dimension import Dimension
        from org.allbinary.input.automation.actions.script.condition.ActionListener import ActionListener
        from org.allbinary.input.automation.actions.script.condition.GroupLayout import GroupLayout
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
        self.okJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okJButtonActionPerformed(evt)
))
        colorAtActionJDialogLayout: GroupLayout = GroupLayout(self.colorAtActionJDialog.getContentPane())
        self.colorAtActionJDialog.getContentPane().setLayout(colorAtActionJDialogLayout)
        colorAtActionJDialogLayout.setHorizontalGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addContainerGap().addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addComponent(self.okJButton).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, False).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.blueJLabel).addComponent(self.greenJLabel).addComponent(self.redJLabel).addComponent(self.colorRangeJLabel)).addGap(29, 29, 29)).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, colorAtActionJDialogLayout.createSequentialGroup().addComponent(self.locationJLabel).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.xJLabel).addGap(18, 18, 18))).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.minBlueJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE).addComponent(self.minGreenJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE).addComponent(self.minJLabel, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.minRedJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE).addComponent(self.colorAtXJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 40, Short.MAX_VALUE)).addGap(16, 16, 16))).addGap(6, 6, 6).addComponent(self.yJLabel).addGap(24, 24, 24).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addComponent(self.maxJLabel, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addGroup(javax.swing.GroupLayout.Alignment.LEADING, colorAtActionJDialogLayout.createSequentialGroup().addGap(1, 1, 1).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, False).addComponent(self.maxBlueJTextField, javax.swing.GroupLayout.Alignment.TRAILING).addComponent(self.maxRedJTextField, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, 43, Short.MAX_VALUE).addComponent(self.maxGreenJTextField, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 43, javax.swing.GroupLayout.PREFERRED_SIZE))).addComponent(self.colorAtYJTextField, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 44, Short.MAX_VALUE)).addGap(22, 22, 22)).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, colorAtActionJDialogLayout.createSequentialGroup().addComponent(self.titleJLabel).addGap(33, 33, 33)))))
        colorAtActionJDialogLayout.setVerticalGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.titleJLabel).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGap(15, 15, 15).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.xJLabel).addComponent(self.locationJLabel).addComponent(self.colorAtXJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.yJLabel)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.minJLabel).addComponent(self.colorRangeJLabel)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.minRedJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.redJLabel)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.greenJLabel).addComponent(self.minGreenJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(colorAtActionJDialogLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.blueJLabel).addComponent(self.minBlueJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 17, Short.MAX_VALUE).addComponent(self.okJButton)).addGroup(colorAtActionJDialogLayout.createSequentialGroup().addGap(14, 14, 14).addComponent(self.colorAtYJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxJLabel).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxRedJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxGreenJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.maxBlueJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))).addContainerGap()))
        self.setPreferredSize(Dimension(100, 0))
        self.colorAtActionJButton.setText("Edit")
        self.colorAtActionJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.colorAtActionJButtonActionPerformed(evt)
))
        self.jLabel1.setText("Color At:")
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jLabel1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 15, Short.MAX_VALUE).addComponent(self.colorAtActionJButton)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.colorAtActionJButton)))
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.update()
        self.getColorAtActionJDialog().setVisible(False)
    

    def colorAtActionJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.getColorAtActionJDialog().setVisible(True)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
from org.allbinary.string.CommonStrings import CommonStrings


