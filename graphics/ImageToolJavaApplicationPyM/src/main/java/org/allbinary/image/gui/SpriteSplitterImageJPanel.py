# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.image.gui

from __future__ import annotations

import threading
from org.allbinary.media.image.ImageProcessedVisitor import ImageProcessedVisitor
from org.allbinary.image.gui.JPanel import JPanel


class SpriteSplitterImageJPanel(JPanel, ImageProcessedVisitor):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.imageStrings: ImageStrings = ImageStrings.getInstance()
        self.imageProcessorInput: ImageProcessorInput = None
        self.result: BufferedImage = None
        self.generateJButton: JButton = None
        self.heightReductionTextField: JTextField = None
        self.increaseHeightTextField: JTextField = None
        self.increaseWidthTextField: JTextField = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.jLabel3: JLabel = None
        self.jLabel4: JLabel = None
        self.jLabel5: JLabel = None
        self.jLabel6: JLabel = None
        self.jLabel7: JLabel = None
        self.jLabel8: JLabel = None
        self.jPanel1: JPanel = None
        self.jPanel2: JPanel = None
        self.spriteTypeJComboBox: JComboBox[str] = None
        self.totalAnimationsJComboBox: JComboBox[str] = None
        self.totalFramesJComboBox: JComboBox[str] = None
        self.widthReductionTextField: JTextField = None
        self.writeOverOriginalJCheckBox: JCheckBox = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.imageProcessorInput = imageProcessorInput
    

    def process(self) -> None:
        (threading.Thread()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     spriteSplitterUtil: SpriteSplitterUtil = SpriteSplitterUtil.getInstance()
#                     spriteType: str = self.spriteTypeJComboBox.getSelectedItem()
#                     totalFrames: int = str(self.totalFramesJComboBox.getSelectedItem())
#                     totalAnimations: int = str(self.totalAnimationsJComboBox.getSelectedItem())
#                     widthReduction: int = str(self.widthReductionTextField.getText())
#                     heightReduction: int = str(self.heightReductionTextField.getText())
#                     increaseWidth: int = str(self.increaseWidthTextField.getText())
#                     increaseHeight: int = str(self.increaseHeightTextField.getText())
#                     spriteSplitterUtil.process(self.getImageProcessorInput(), totalFrames, totalAnimations, widthReduction, heightReduction, increaseWidth, increaseHeight, spriteType, self)
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.JCheckBox import JCheckBox
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JComboBox import JComboBox
        from org.allbinary.image.gui.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JComboBox import JComboBox
        from org.allbinary.image.gui.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JComboBox import JComboBox
        from org.allbinary.image.gui.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        self.writeOverOriginalJCheckBox = JCheckBox()
        self.widthReductionTextField = JTextField()
        self.jLabel5 = JLabel()
        self.jPanel1 = (JPanel()  # Java anonymous class body:
#             
# 
#             def paint(self, graphics: Graphics) -> None:
#                 if self.result is not None:
#                     graphics.drawImage(self.result, 0, 0, self.result.getWidth(None), self.result.getHeight(None), None)
)
        self.jLabel4 = JLabel()
        self.jLabel6 = JLabel()
        self.heightReductionTextField = JTextField()
        self.generateJButton = JButton()
        self.jPanel2 = JPanel()
        self.jLabel1 = JLabel()
        self.totalFramesJComboBox = JComboBox()
        size: int = 70
        animationStringArray2: list[str] = [None] * (size - 1)
        for index in range(1, size):
            animationStringArray2[index - 1] = str(index)
        self.totalFramesJComboBox.setModel(DefaultComboBoxModel(animationStringArray2))
        self.jLabel2 = JLabel()
        self.totalAnimationsJComboBox = JComboBox()
        animationStringArray: list[str] = [None] * (size - 1)
        for index in range(1, size):
            animationStringArray[index - 1] = str(index)
        self.totalAnimationsJComboBox.setModel(DefaultComboBoxModel(animationStringArray))
        self.jLabel3 = JLabel()
        self.spriteTypeJComboBox = JComboBox()
        self.spriteTypeJComboBox.setModel(DefaultComboBoxModel([org.allbinary.media.image.SpriteSplitterUtil.getInstance().DIRECTIONAL_ANIMATIONS, org.allbinary.media.image.SpriteSplitterUtil.getInstance().HORIZONTAL_ANIMATIONS, org.allbinary.media.image.SpriteSplitterUtil.getInstance().HORIZONTAL_SPRITE]))
        self.jLabel7 = JLabel()
        self.increaseWidthTextField = JTextField()
        self.jLabel8 = JLabel()
        self.increaseHeightTextField = JTextField()
        self.writeOverOriginalJCheckBox.setText("Write Over Original")
        self.writeOverOriginalJCheckBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.writeOverOriginalJCheckBoxActionPerformed(evt)
))
        self.widthReductionTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.widthReductionTextField.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.widthReductionTextFieldActionPerformed(evt)
))
        self.jLabel5.setText("Less Width:")
        self.jLabel4.setText("Results:")
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.jLabel4).addGap(0, 0, Short.MAX_VALUE)))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.jLabel4).addGap(0, 184, Short.MAX_VALUE)))
        self.jLabel6.setText("Less Height:")
        self.heightReductionTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.generateJButton.setText("Generate")
        self.generateJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.generateJButtonActionPerformed(evt)
))
        self.jLabel1.setText("Row Total:")
        self.totalFramesJComboBox.setSelectedIndex(1)
        self.totalFramesJComboBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.totalFramesJComboBoxActionPerformed(evt)
))
        self.jLabel2.setText("Column Total :")
        self.totalAnimationsJComboBox.setSelectedIndex(3)
        self.totalAnimationsJComboBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.totalAnimationsJComboBoxActionPerformed(evt)
))
        self.jLabel3.setText("Type:")
        self.spriteTypeJComboBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.spriteTypeJComboBoxActionPerformed(evt)
))
        jPanel2Layout: GroupLayout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup().addContainerGap().addComponent(self.jLabel1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.totalFramesJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 48, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel2).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.totalAnimationsJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 39, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel3).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.spriteTypeJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 172, javax.swing.GroupLayout.PREFERRED_SIZE).addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        jPanel2Layout.setVerticalGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(jPanel2Layout.createSequentialGroup().addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.totalFramesJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2).addComponent(self.totalAnimationsJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel3).addComponent(self.spriteTypeJComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))))
        self.jLabel7.setText("More Width:")
        self.increaseWidthTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.increaseWidthTextField.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.increaseWidthTextFieldActionPerformed(evt)
))
        self.jLabel8.setText("More Height:")
        self.increaseHeightTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, 415, Short.MAX_VALUE).addGap(78, 78, 78)).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.writeOverOriginalJCheckBox).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.generateJButton)).addGroup(layout.createSequentialGroup().addComponent(self.jLabel5).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.widthReductionTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 41, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel6).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.heightReductionTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 46, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel7).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.increaseWidthTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 41, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel8).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.increaseHeightTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 46, javax.swing.GroupLayout.PREFERRED_SIZE))).addGap(0, 0, Short.MAX_VALUE))).addContainerGap()))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel7).addComponent(self.increaseWidthTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 22, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel8).addComponent(self.increaseHeightTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel5).addComponent(self.widthReductionTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 22, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel6).addComponent(self.heightReductionTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.writeOverOriginalJCheckBox).addComponent(self.generateJButton)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
    

    def writeOverOriginalJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def generateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def spriteTypeJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        spriteSplitterUtil: SpriteSplitterUtil = SpriteSplitterUtil.getInstance()
        self.jLabel1.setText(spriteSplitterUtil.ANIMATIONS_LABELS[self.spriteTypeJComboBox.getSelectedIndex()])
        self.jLabel2.setText(spriteSplitterUtil.ANIMATIONS_LABELS[self.spriteTypeJComboBox.getSelectedIndex() + 1])
    

    def totalAnimationsJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def totalFramesJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def widthReductionTextFieldActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def increaseWidthTextFieldActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        self.imageProcessorInput = imageProcessorInput
    

    # throws IOException
    def visit(self, generatedBufferedImage: BufferedImage, name: str, index: int) -> None:
        self.logUtil.putF(self.commonStrings.VISIT, self, self.commonStrings.VISIT)
        self.result = generatedBufferedImage
        self.getParent().repaint()
        file: File = self.imageProcessorInput.getFiles()[index]
        if not self.writeOverOriginalJCheckBox.isSelected():
            filePath: str = file.getAbsolutePath()
            extensionIndex: int = filePath.find(self.imageStrings.PNG_EXTENSION)
            filePath = str(StringMaker().append(filePath[0:extensionIndex]).append(self.commonSeps.UNDERSCORE).append(name).append(self.imageStrings.PNG_EXTENSION))
            file = File(filePath)
        isWritten: bool = ImageIO.write(self.result, self.imageStrings.PNG, file)
        self.logUtil.putF(str(StringMaker().append("File: ").append(StringUtil.getInstance().toString(file)).append(" Wrote: ").appendboolean(isWritten)), self, self.commonStrings.RUN)
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from java.io.File import File
# from java.io.IOException import IOException
# from javax.imageio.ImageIO import ImageIO
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
from org.allbinary.media.image.ImageStrings import ImageStrings
from org.allbinary.media.image.SpriteSplitterUtil import SpriteSplitterUtil
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


