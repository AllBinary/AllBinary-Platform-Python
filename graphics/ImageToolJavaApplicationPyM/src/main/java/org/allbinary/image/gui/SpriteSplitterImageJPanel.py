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

from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.media.image.ImageProcessedVisitor import ImageProcessedVisitor
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class SpriteSplitterImageJPanel(*java_bases(JPanel, ImageProcessedVisitor)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("commonSeps", None)
        vars(self).setdefault("imageStrings", None)
        vars(self).setdefault("imageProcessorInput", None)
        vars(self).setdefault("result", None)
        vars(self).setdefault("generateJButton", None)
        vars(self).setdefault("heightReductionTextField", None)
        vars(self).setdefault("increaseHeightTextField", None)
        vars(self).setdefault("increaseWidthTextField", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("jLabel3", None)
        vars(self).setdefault("jLabel4", None)
        vars(self).setdefault("jLabel5", None)
        vars(self).setdefault("jLabel6", None)
        vars(self).setdefault("jLabel7", None)
        vars(self).setdefault("jLabel8", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("jPanel2", None)
        vars(self).setdefault("spriteTypeJComboBox", None)
        vars(self).setdefault("totalAnimationsJComboBox", None)
        vars(self).setdefault("totalFramesJComboBox", None)
        vars(self).setdefault("widthReductionTextField", None)
        vars(self).setdefault("writeOverOriginalJCheckBox", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.ImageStrings import ImageStrings
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.imageStrings: ImageStrings = ImageStrings.getInstance()
        if "imageProcessorInput" not in vars(self): self.imageProcessorInput: ImageProcessorInput = None
        if "result" not in vars(self): self.result: BufferedImage = None
        if "generateJButton" not in vars(self): self.generateJButton: JButton = None
        if "heightReductionTextField" not in vars(self): self.heightReductionTextField: JTextField = None
        if "increaseHeightTextField" not in vars(self): self.increaseHeightTextField: JTextField = None
        if "increaseWidthTextField" not in vars(self): self.increaseWidthTextField: JTextField = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "jLabel3" not in vars(self): self.jLabel3: JLabel = None
        if "jLabel4" not in vars(self): self.jLabel4: JLabel = None
        if "jLabel5" not in vars(self): self.jLabel5: JLabel = None
        if "jLabel6" not in vars(self): self.jLabel6: JLabel = None
        if "jLabel7" not in vars(self): self.jLabel7: JLabel = None
        if "jLabel8" not in vars(self): self.jLabel8: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "jPanel2" not in vars(self): self.jPanel2: JPanel = None
        if "spriteTypeJComboBox" not in vars(self): self.spriteTypeJComboBox: JComboBox[str] = None
        if "totalAnimationsJComboBox" not in vars(self): self.totalAnimationsJComboBox: JComboBox[str] = None
        if "totalFramesJComboBox" not in vars(self): self.totalFramesJComboBox: JComboBox[str] = None
        if "widthReductionTextField" not in vars(self): self.widthReductionTextField: JTextField = None
        if "writeOverOriginalJCheckBox" not in vars(self): self.writeOverOriginalJCheckBox: JCheckBox = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        self.imageProcessorInput = imageProcessorInput
    

    def process(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.SpriteSplitterUtil import SpriteSplitterUtil
        _java_listener_owner = self
        class _JavaListenerN66637(Thread):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.media.image.SpriteSplitterUtil import SpriteSplitterUtil
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    spriteSplitterUtil: SpriteSplitterUtil = SpriteSplitterUtil.getInstance()
                    spriteType: str = _java_listener_owner.spriteTypeJComboBox.getSelectedItem()
                    totalFrames: int = str(_java_listener_owner.totalFramesJComboBox.getSelectedItem())
                    totalAnimations: int = str(_java_listener_owner.totalAnimationsJComboBox.getSelectedItem())
                    widthReduction: int = str(_java_listener_owner.widthReductionTextField.getText())
                    heightReduction: int = str(_java_listener_owner.heightReductionTextField.getText())
                    increaseWidth: int = str(_java_listener_owner.increaseWidthTextField.getText())
                    increaseHeight: int = str(_java_listener_owner.increaseHeightTextField.getText())
                    spriteSplitterUtil.process(_java_listener_owner.getImageProcessorInput(), totalFrames, totalAnimations, widthReduction, heightReduction, increaseWidth, increaseHeight, spriteType, _java_listener_owner)
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN66637()
            .start()
    

    def initComponents(self) -> None:
        from org.allbinary.media.image.SpriteSplitterUtil import SpriteSplitterUtil
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        self.writeOverOriginalJCheckBox = JCheckBox()
        self.widthReductionTextField = JTextField()
        self.jLabel5 = JLabel()
        _java_listener_owner = self
        class _JavaListenerN67613(JPanel):
            
            

            def paint(self, graphics: Graphics) -> None:
                if _java_listener_owner.result is not None:
                    graphics.drawImage(_java_listener_owner.result, 0, 0, _java_listener_owner.result.getWidth(None), _java_listener_owner.result.getHeight(None), None)
        self.jPanel1 = _JavaListenerN67613()
            
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
        self.spriteTypeJComboBox.setModel(DefaultComboBoxModel([SpriteSplitterUtil.getInstance().DIRECTIONAL_ANIMATIONS, SpriteSplitterUtil.getInstance().HORIZONTAL_ANIMATIONS, SpriteSplitterUtil.getInstance().HORIZONTAL_SPRITE]))
        self.jLabel7 = JLabel()
        self.increaseWidthTextField = JTextField()
        self.jLabel8 = JLabel()
        self.increaseHeightTextField = JTextField()
        self.writeOverOriginalJCheckBox.setText("Write Over Original")
        _java_listener_owner = self
        class _JavaListenerN69064(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "writeOverOriginalJCheckBoxActionPerformed") else _java_listener_owner).writeOverOriginalJCheckBoxActionPerformed(evt)
        self.writeOverOriginalJCheckBox.addActionListener(_JavaListenerN69064()
            )
        self.widthReductionTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        _java_listener_owner = self
        class _JavaListenerN69223(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "widthReductionTextFieldActionPerformed") else _java_listener_owner).widthReductionTextFieldActionPerformed(evt)
        self.widthReductionTextField.addActionListener(_JavaListenerN69223()
            )
        self.jLabel5.setText("Less Width:")
        self.jLabel4.setText("Results:")
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.jLabel4).addGap(0, 0, Short.MAX_VALUE)))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.jLabel4).addGap(0, 184, Short.MAX_VALUE)))
        self.jLabel6.setText("Less Height:")
        self.heightReductionTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.generateJButton.setText("Generate")
        _java_listener_owner = self
        class _JavaListenerN69883(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateJButtonActionPerformed") else _java_listener_owner).generateJButtonActionPerformed(evt)
        self.generateJButton.addActionListener(_JavaListenerN69883()
            )
        self.jLabel1.setText("Row Total:")
        self.totalFramesJComboBox.setSelectedIndex(1)
        _java_listener_owner = self
        class _JavaListenerN70052(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "totalFramesJComboBoxActionPerformed") else _java_listener_owner).totalFramesJComboBoxActionPerformed(evt)
        self.totalFramesJComboBox.addActionListener(_JavaListenerN70052()
            )
        self.jLabel2.setText("Column Total :")
        self.totalAnimationsJComboBox.setSelectedIndex(3)
        _java_listener_owner = self
        class _JavaListenerN70221(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "totalAnimationsJComboBoxActionPerformed") else _java_listener_owner).totalAnimationsJComboBoxActionPerformed(evt)
        self.totalAnimationsJComboBox.addActionListener(_JavaListenerN70221()
            )
        self.jLabel3.setText("Type:")
        _java_listener_owner = self
        class _JavaListenerN70360(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "spriteTypeJComboBoxActionPerformed") else _java_listener_owner).spriteTypeJComboBoxActionPerformed(evt)
        self.spriteTypeJComboBox.addActionListener(_JavaListenerN70360()
            )
        jPanel2Layout: GroupLayout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup().addContainerGap().addComponent(self.jLabel1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.totalFramesJComboBox, GroupLayout.PREFERRED_SIZE, 48, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel2).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.totalAnimationsJComboBox, GroupLayout.PREFERRED_SIZE, 39, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel3).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.spriteTypeJComboBox, GroupLayout.PREFERRED_SIZE, 172, GroupLayout.PREFERRED_SIZE).addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        jPanel2Layout.setVerticalGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel2Layout.createSequentialGroup().addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.totalFramesJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2).addComponent(self.totalAnimationsJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel3).addComponent(self.spriteTypeJComboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))))
        self.jLabel7.setText("More Width:")
        self.increaseWidthTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        _java_listener_owner = self
        class _JavaListenerN71649(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "increaseWidthTextFieldActionPerformed") else _java_listener_owner).increaseWidthTextFieldActionPerformed(evt)
        self.increaseWidthTextField.addActionListener(_JavaListenerN71649()
            )
        self.jLabel8.setText("More Height:")
        self.increaseHeightTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jPanel2, GroupLayout.PREFERRED_SIZE, 415, Short.MAX_VALUE).addGap(78, 78, 78)).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.jPanel1, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.writeOverOriginalJCheckBox).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.generateJButton)).addGroup(layout.createSequentialGroup().addComponent(self.jLabel5).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.widthReductionTextField, GroupLayout.PREFERRED_SIZE, 41, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel6).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.heightReductionTextField, GroupLayout.PREFERRED_SIZE, 46, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel7).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.increaseWidthTextField, GroupLayout.PREFERRED_SIZE, 41, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel8).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.increaseHeightTextField, GroupLayout.PREFERRED_SIZE, 46, GroupLayout.PREFERRED_SIZE))).addGap(0, 0, Short.MAX_VALUE))).addContainerGap()))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jPanel2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel7).addComponent(self.increaseWidthTextField, GroupLayout.PREFERRED_SIZE, 22, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel8).addComponent(self.increaseHeightTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel5).addComponent(self.widthReductionTextField, GroupLayout.PREFERRED_SIZE, 22, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel6).addComponent(self.heightReductionTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.writeOverOriginalJCheckBox).addComponent(self.generateJButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
    

    def writeOverOriginalJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def generateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def spriteTypeJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.media.image.SpriteSplitterUtil import SpriteSplitterUtil
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
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        self.imageProcessorInput = imageProcessorInput
    

    # throws IOException
    def visit(self, generatedBufferedImage: BufferedImage, name: str, index: int) -> None:
        from java.io.File import File
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.logUtil.putF(self.commonStrings.VISIT, self, self.commonStrings.VISIT)
        self.result = generatedBufferedImage
        self.getParent().repaint()
        file: File = self.imageProcessorInput.getFiles()[index]
        if not (java_predicate(self.writeOverOriginalJCheckBox, "isSelected")):
            filePath: str = file.getAbsolutePath()
            extensionIndex: int = filePath.find(self.imageStrings.PNG_EXTENSION)
            filePath = str(StringMaker().append(filePath[0:extensionIndex]).append(self.commonSeps.UNDERSCORE).append(name).append(self.imageStrings.PNG_EXTENSION))
            file = File(filePath)
        isWritten: bool = ImageIO.write(self.result, self.imageStrings.PNG, file)
        self.logUtil.putF(str(StringMaker().append("File: ").append(StringUtil.getInstance().toString(file)).append(" Wrote: ").appendboolean(isWritten)), self, self.commonStrings.RUN)
# from java.awt.Graphics import Graphics
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from java.io.File import File
# from java.io.IOException import IOException
# from javax.imageio.ImageIO import ImageIO
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageStrings import ImageStrings
# from org.allbinary.media.image.SpriteSplitterUtil import SpriteSplitterUtil
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.DefaultComboBoxModel import DefaultComboBoxModel
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JCheckBox import JCheckBox
# from javax.swing.JComboBox import JComboBox
# from javax.swing.JLabel import JLabel
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle


