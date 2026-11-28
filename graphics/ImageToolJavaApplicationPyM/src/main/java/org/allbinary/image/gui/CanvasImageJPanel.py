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
class CanvasImageJPanel(*java_bases(JPanel, ImageProcessedVisitor)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("commonSeps", None)
        vars(self).setdefault("imageStrings", None)
        vars(self).setdefault("imageProcessorInput", None)
        vars(self).setdefault("result", None)
        vars(self).setdefault("generateJButton", None)
        vars(self).setdefault("heightReductionTextField", None)
        vars(self).setdefault("heightReductionTextField1", None)
        vars(self).setdefault("jLabel4", None)
        vars(self).setdefault("jLabel5", None)
        vars(self).setdefault("jLabel6", None)
        vars(self).setdefault("jLabel7", None)
        vars(self).setdefault("jLabel8", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("jPanel2", None)
        vars(self).setdefault("widthReductionTextField", None)
        vars(self).setdefault("widthReductionTextField1", None)
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
        if "heightReductionTextField1" not in vars(self): self.heightReductionTextField1: JTextField = None
        if "jLabel4" not in vars(self): self.jLabel4: JLabel = None
        if "jLabel5" not in vars(self): self.jLabel5: JLabel = None
        if "jLabel6" not in vars(self): self.jLabel6: JLabel = None
        if "jLabel7" not in vars(self): self.jLabel7: JLabel = None
        if "jLabel8" not in vars(self): self.jLabel8: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "jPanel2" not in vars(self): self.jPanel2: JPanel = None
        if "widthReductionTextField" not in vars(self): self.widthReductionTextField: JTextField = None
        if "widthReductionTextField1" not in vars(self): self.widthReductionTextField1: JTextField = None
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
        from org.allbinary.media.image.CanvasExpandUtil import CanvasExpandUtil
        from org.allbinary.media.image.CanvasTrimUtil import CanvasTrimUtil
        _java_listener_owner = self
        class _JavaListenerN66627(Thread):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.media.image.CanvasExpandUtil import CanvasExpandUtil
                from org.allbinary.media.image.CanvasTrimUtil import CanvasTrimUtil
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    canvasTrimUtil: CanvasTrimUtil = CanvasTrimUtil.getInstance()
                    canvasExpandUtil: CanvasExpandUtil = CanvasExpandUtil.getInstance()
                    leftReduction: int = str(_java_listener_owner.widthReductionTextField1.getText())
                    topReduction: int = str(_java_listener_owner.heightReductionTextField1.getText())
                    widthReduction: int = str(_java_listener_owner.widthReductionTextField.getText())
                    heightReduction: int = str(_java_listener_owner.heightReductionTextField.getText())
                    if leftReduction <= 0 or topReduction <= 0 or widthReduction <= 0 or heightReduction <= 0:
                        canvasTrimUtil.process(_java_listener_owner.getImageProcessorInput(), -leftReduction, -topReduction, -widthReduction, -heightReduction, _java_listener_owner)
                    else:
                        canvasExpandUtil.process(_java_listener_owner.getImageProcessorInput(), leftReduction, topReduction, _java_listener_owner)
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN66627()
            .start()
    

    def initComponents(self) -> None:
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        self.writeOverOriginalJCheckBox = JCheckBox()
        _java_listener_owner = self
        class _JavaListenerN67525(JPanel):
            
            

            def paint(self, graphics: Graphics) -> None:
                if _java_listener_owner.result is not None:
                    graphics.drawImage(_java_listener_owner.result, 0, 0, _java_listener_owner.result.getWidth(None), _java_listener_owner.result.getHeight(None), None)
        self.jPanel1 = _JavaListenerN67525()
            
        self.generateJButton = JButton()
        self.jLabel4 = JLabel()
        self.jPanel2 = JPanel()
        self.jLabel5 = JLabel()
        self.widthReductionTextField = JTextField()
        self.jLabel6 = JLabel()
        self.heightReductionTextField = JTextField()
        self.widthReductionTextField1 = JTextField()
        self.jLabel7 = JLabel()
        self.jLabel8 = JLabel()
        self.heightReductionTextField1 = JTextField()
        self.writeOverOriginalJCheckBox.setSelected(True)
        self.writeOverOriginalJCheckBox.setText("Write Over Original")
        _java_listener_owner = self
        class _JavaListenerN68167(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "writeOverOriginalJCheckBoxActionPerformed") else _java_listener_owner).writeOverOriginalJCheckBoxActionPerformed(evt)
        self.writeOverOriginalJCheckBox.addActionListener(_JavaListenerN68167()
            )
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 0, Short.MAX_VALUE))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 196, Short.MAX_VALUE))
        self.generateJButton.setText("Generate")
        _java_listener_owner = self
        class _JavaListenerN68595(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateJButtonActionPerformed") else _java_listener_owner).generateJButtonActionPerformed(evt)
        self.generateJButton.addActionListener(_JavaListenerN68595()
            )
        self.jLabel4.setText("Results:")
        self.jLabel5.setText("Right:")
        self.widthReductionTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        _java_listener_owner = self
        class _JavaListenerN68814(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "widthReductionTextFieldActionPerformed") else _java_listener_owner).widthReductionTextFieldActionPerformed(evt)
        self.widthReductionTextField.addActionListener(_JavaListenerN68814()
            )
        self.jLabel6.setText("Bottom")
        self.heightReductionTextField.setText(CommonPhoneStrings.getInstance().ZERO)
        self.widthReductionTextField1.setText(CommonPhoneStrings.getInstance().ZERO)
        _java_listener_owner = self
        class _JavaListenerN69053(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "widthReductionTextField1ActionPerformed") else _java_listener_owner).widthReductionTextField1ActionPerformed(evt)
        self.widthReductionTextField1.addActionListener(_JavaListenerN69053()
            )
        self.jLabel7.setText("Top")
        self.jLabel8.setText("Left:")
        self.heightReductionTextField1.setText(CommonPhoneStrings.getInstance().ZERO)
        jPanel2Layout: GroupLayout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel2Layout.createSequentialGroup().addContainerGap().addComponent(self.jLabel8).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.widthReductionTextField1, GroupLayout.PREFERRED_SIZE, 41, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel5).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.widthReductionTextField, GroupLayout.PREFERRED_SIZE, 41, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel7).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.heightReductionTextField1, GroupLayout.PREFERRED_SIZE, 46, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel6).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.heightReductionTextField, GroupLayout.PREFERRED_SIZE, 46, GroupLayout.PREFERRED_SIZE).addContainerGap(140, Short.MAX_VALUE)))
        jPanel2Layout.setVerticalGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup().addGap(0, 16, Short.MAX_VALUE).addGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel6).addComponent(self.heightReductionTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel8).addComponent(self.widthReductionTextField1, GroupLayout.PREFERRED_SIZE, 22, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel7).addComponent(self.heightReductionTextField1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addGroup(jPanel2Layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel5).addComponent(self.widthReductionTextField, GroupLayout.PREFERRED_SIZE, 22, GroupLayout.PREFERRED_SIZE)))))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jPanel2, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addGap(78, 78, 78)).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addComponent(self.jPanel1, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.jLabel4).addGroup(layout.createSequentialGroup().addComponent(self.writeOverOriginalJCheckBox).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.generateJButton))).addGap(0, 0, Short.MAX_VALUE))).addContainerGap()))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jPanel2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.generateJButton).addComponent(self.writeOverOriginalJCheckBox)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel4).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
    

    def writeOverOriginalJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def generateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def widthReductionTextFieldActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def widthReductionTextField1ActionPerformed(self, evt: ActionEvent) -> None:
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
# from org.allbinary.media.image.CanvasExpandUtil import CanvasExpandUtil
# from org.allbinary.media.image.CanvasTrimUtil import CanvasTrimUtil
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageStrings import ImageStrings
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JCheckBox import JCheckBox
# from javax.swing.JLabel import JLabel
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle


