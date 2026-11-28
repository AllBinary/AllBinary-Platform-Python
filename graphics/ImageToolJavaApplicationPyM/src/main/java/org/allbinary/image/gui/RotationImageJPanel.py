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
class RotationImageJPanel(*java_bases(JPanel, ImageProcessedVisitor)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("imageStrings", None)
        vars(self).setdefault("imageProcessorInput", None)
        vars(self).setdefault("result", None)
        vars(self).setdefault("generateJButton", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("jLabel3", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("jPanel2", None)
        vars(self).setdefault("jPanel3", None)
        vars(self).setdefault("totalAngleJComboBox", None)
        vars(self).setdefault("writeOverOriginalJCheckBox", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.ImageStrings import ImageStrings
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageStrings: ImageStrings = ImageStrings.getInstance()
        if "imageProcessorInput" not in vars(self): self.imageProcessorInput: ImageProcessorInput = None
        if "result" not in vars(self): self.result: BufferedImage = None
        if "generateJButton" not in vars(self): self.generateJButton: JButton = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "jLabel3" not in vars(self): self.jLabel3: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "jPanel2" not in vars(self): self.jPanel2: JPanel = None
        if "jPanel3" not in vars(self): self.jPanel3: JPanel = None
        if "totalAngleJComboBox" not in vars(self): self.totalAngleJComboBox: JComboBox = None
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
        from org.allbinary.media.image.ImageArrayRotationUtil import ImageArrayRotationUtil
        _java_listener_owner = self
        class _JavaListenerN66464(Thread):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.media.image.ImageArrayRotationUtil import ImageArrayRotationUtil
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    angleAsString: str = _java_listener_owner.totalAngleJComboBox.getSelectedItem()
                    ImageArrayRotationUtil.getInstance().process(_java_listener_owner.getImageProcessorInput(), angleAsString, _java_listener_owner)
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN66464()
            .start()
    

    def initComponents(self) -> None:
        _java_listener_owner = self
        class _JavaListenerN66840(JPanel):
            
            

            def paint(self, graphics: Graphics) -> None:
                if _java_listener_owner.result is not None:
                    graphics.drawImage(_java_listener_owner.result, 0, 0, _java_listener_owner.result.getWidth(None), _java_listener_owner.result.getHeight(None), None)
        self.jPanel1 = _JavaListenerN66840()
            
        self.jPanel2 = JPanel()
        self.jLabel1 = JLabel()
        self.generateJButton = JButton()
        self.totalAngleJComboBox = JComboBox()
        self.jLabel3 = JLabel()
        self.writeOverOriginalJCheckBox = JCheckBox()
        self.jPanel3 = JPanel()
        self.jLabel2 = JLabel()
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(0, 436, Short.MAX_VALUE))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(0, 227, Short.MAX_VALUE))
        self.generateJButton.setText("Generate")
        _java_listener_owner = self
        class _JavaListenerN67725(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateJButtonActionPerformed") else _java_listener_owner).generateJButtonActionPerformed(evt)
        self.generateJButton.addActionListener(_JavaListenerN67725()
            )
        self.totalAngleJComboBox.setModel(DefaultComboBoxModel([self.commonStrings.UP, self.commonStrings.DOWN, "-90", "90"]))
        _java_listener_owner = self
        class _JavaListenerN67946(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "totalAngleJComboBoxActionPerformed") else _java_listener_owner).totalAngleJComboBoxActionPerformed(evt)
        self.totalAngleJComboBox.addActionListener(_JavaListenerN67946()
            )
        self.jLabel3.setText("Total Angle:")
        self.writeOverOriginalJCheckBox.setText("Write Over Original")
        jPanel2Layout: GroupLayout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(jPanel2Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(jPanel2Layout.createSequentialGroup().add(8, 8, 8).add(self.jLabel1).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.jLabel3).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.totalAngleJComboBox, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.writeOverOriginalJCheckBox).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.generateJButton).addContainerGap(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        jPanel2Layout.setVerticalGroup(jPanel2Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(jPanel2Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.BASELINE).add(self.jLabel1).add(self.generateJButton).add(self.totalAngleJComboBox, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).add(self.jLabel3).add(self.writeOverOriginalJCheckBox)))
        self.jLabel2.setText("Results:")
        jPanel3Layout: GroupLayout = GroupLayout(self.jPanel3)
        self.jPanel3.setLayout(jPanel3Layout)
        jPanel3Layout.setHorizontalGroup(jPanel3Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(jPanel3Layout.createSequentialGroup().add(self.jLabel2).addContainerGap(377, Short.MAX_VALUE)))
        jPanel3Layout.setVerticalGroup(jPanel3Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(self.jLabel2))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING, self.jPanel2, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(layout.createSequentialGroup().addContainerGap().add(self.jPanel3, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addContainerGap()).add(self.jPanel1, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(layout.createSequentialGroup().add(self.jPanel2, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.UNRELATED).add(self.jPanel3, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.jPanel1, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
    

    def generateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def totalAngleJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
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
        from org.allbinary.string.CommonSeps import CommonSeps
        self.result = generatedBufferedImage
        self.getParent().repaint()
        file: File = self.imageProcessorInput.getFiles()[index]
        if not (java_predicate(self.writeOverOriginalJCheckBox, "isSelected")):
            filePath: str = file.getAbsolutePath()
            extensionIndex: int = filePath.find(self.imageStrings.PNG_EXTENSION)
            filePath = str(StringMaker().append(filePath[0:extensionIndex]).append(CommonSeps.getInstance().UNDERSCORE).append(name).append(self.imageStrings.PNG_EXTENSION))
            file = File(filePath)
        isWritten: bool = ImageIO.write(self.result, self.imageStrings.PNG, file)
        self.logUtil.putF("File: " + str(file) + " Wrote: " + str(isWritten), self, self.commonStrings.RUN)
# from java.awt.Graphics import Graphics
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from java.io.File import File
# from java.io.IOException import IOException
# from javax.imageio.ImageIO import ImageIO
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.media.image.ImageArrayRotationUtil import ImageArrayRotationUtil
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageStrings import ImageStrings
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.DefaultComboBoxModel import DefaultComboBoxModel
# from javax.swing.JButton import JButton
# from javax.swing.JCheckBox import JCheckBox
# from javax.swing.JComboBox import JComboBox
# from javax.swing.JLabel import JLabel


