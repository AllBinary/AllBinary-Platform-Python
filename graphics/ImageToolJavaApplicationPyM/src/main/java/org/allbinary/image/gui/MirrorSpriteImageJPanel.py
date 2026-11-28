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
from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class MirrorSpriteImageJPanel(*java_bases(JPanel, ImageProcessorInputCompositeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("imageStrings", None)
        vars(self).setdefault("imageProcessorInput", None)
        vars(self).setdefault("result", None)
        vars(self).setdefault("generateJButton", None)
        vars(self).setdefault("horizontalJCheckBox", None)
        vars(self).setdefault("imageHeightIsFrameSizeJCheckBox", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("jLayeredPane1", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("jPanel2", None)
        vars(self).setdefault("jPanel3", None)
        vars(self).setdefault("verticleJCheckBox", None)
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
        if "horizontalJCheckBox" not in vars(self): self.horizontalJCheckBox: JCheckBox = None
        if "imageHeightIsFrameSizeJCheckBox" not in vars(self): self.imageHeightIsFrameSizeJCheckBox: JCheckBox = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "jLayeredPane1" not in vars(self): self.jLayeredPane1: JLayeredPane = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "jPanel2" not in vars(self): self.jPanel2: JPanel = None
        if "jPanel3" not in vars(self): self.jPanel3: JPanel = None
        if "verticleJCheckBox" not in vars(self): self.verticleJCheckBox: JCheckBox = None
        if "writeOverOriginalJCheckBox" not in vars(self): self.writeOverOriginalJCheckBox: JCheckBox = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        super().__init__()
        __class__._init_fields(self)
        self.logUtil.putF("Starting", self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.imageProcessorInput = imageProcessorInput
    

    def process(self) -> None:
        from java.io.File import File
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.BufferedImageUtil2 import BufferedImageUtil2
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        from org.allbinary.media.image.MirrorImageUtil import MirrorImageUtil
        _java_listener_owner = self
        class _JavaListenerN66451(Thread):
            
            

            def run(self) -> None:
                from java.io.File import File
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.media.image.BufferedImageUtil2 import BufferedImageUtil2
                from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
                from org.allbinary.media.image.MirrorImageUtil import MirrorImageUtil
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    generatedBufferedImageArray: list[BufferedImage] = None
                    imageProcessorInput: ImageProcessorInput = _java_listener_owner.getImageProcessorInput()
                    bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
                    for index in range(0, len(bufferedImageArray)):
                        generatedBufferedImageArray = MirrorImageUtil.getInstance().getImages(bufferedImageArray[index], java_predicate(_java_listener_owner.verticleJCheckBox, "isSelected"), java_predicate(_java_listener_owner.horizontalJCheckBox, "isSelected"))
                        _java_listener_owner.result = BufferedImageUtil2.getInstance().createSpriteImage(generatedBufferedImageArray)
                        _java_listener_owner.getParent().repaint()
                        file: File = imageProcessorInput.getFiles()[index]
                        if not (java_predicate(_java_listener_owner.writeOverOriginalJCheckBox, "isSelected")):
                            filePath: str = file.getAbsolutePath()
                            extensionIndex: int = filePath.find(_java_listener_owner.imageStrings.PNG_EXTENSION)
                            filePath = filePath[0:extensionIndex] + "_mirror" + str(_java_listener_owner.imageStrings.PNG_EXTENSION)
                            logUtil.putF("Renamed File: " + filePath, self, _java_listener_owner.commonStrings.RUN)
                            file = File(filePath)
                        isWritten: bool = ImageIO.write(_java_listener_owner.result, _java_listener_owner.imageStrings.PNG, file)
                        logUtil.putF("File: " + str(file) + " Wrote: " + str(isWritten), self, _java_listener_owner.commonStrings.RUN)
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN66451()
            .start()
    

    def initComponents(self) -> None:
        self.jLayeredPane1 = JLayeredPane()
        _java_listener_owner = self
        class _JavaListenerN67690(JPanel):
            
            

            def paint(self, graphics: Graphics) -> None:
                if _java_listener_owner.result is not None:
                    graphics.drawImage(_java_listener_owner.result, 0, 0, _java_listener_owner.result.getWidth(None), _java_listener_owner.result.getHeight(None), None)
        self.jPanel1 = _JavaListenerN67690()
            
        self.jPanel2 = JPanel()
        self.imageHeightIsFrameSizeJCheckBox = JCheckBox()
        self.horizontalJCheckBox = JCheckBox()
        self.verticleJCheckBox = JCheckBox()
        self.writeOverOriginalJCheckBox = JCheckBox()
        self.generateJButton = JButton()
        self.jPanel3 = JPanel()
        self.jLabel2 = JLabel()
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(0, 507, Short.MAX_VALUE))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(0, 230, Short.MAX_VALUE))
        self.imageHeightIsFrameSizeJCheckBox.setSelected(True)
        self.imageHeightIsFrameSizeJCheckBox.setText("Image Height Is Frame Size")
        self.imageHeightIsFrameSizeJCheckBox.setEnabled(False)
        _java_listener_owner = self
        class _JavaListenerN68635(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "imageHeightIsFrameSizeJCheckBoxActionPerformed") else _java_listener_owner).imageHeightIsFrameSizeJCheckBoxActionPerformed(evt)
        self.imageHeightIsFrameSizeJCheckBox.addActionListener(_JavaListenerN68635()
            )
        self.horizontalJCheckBox.setSelected(True)
        self.horizontalJCheckBox.setText("Horizontal")
        self.horizontalJCheckBox.setEnabled(False)
        self.verticleJCheckBox.setText("Verticle")
        self.verticleJCheckBox.setEnabled(False)
        self.writeOverOriginalJCheckBox.setText("Write Over Original")
        self.generateJButton.setText("Generate")
        _java_listener_owner = self
        class _JavaListenerN68958(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateJButtonActionPerformed") else _java_listener_owner).generateJButtonActionPerformed(evt)
        self.generateJButton.addActionListener(_JavaListenerN68958()
            )
        jPanel2Layout: GroupLayout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(jPanel2Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(jPanel2Layout.createSequentialGroup().addContainerGap(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(self.verticleJCheckBox).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.UNRELATED).add(self.horizontalJCheckBox).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.imageHeightIsFrameSizeJCheckBox).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.writeOverOriginalJCheckBox).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.generateJButton)))
        jPanel2Layout.setVerticalGroup(jPanel2Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(jPanel2Layout.createSequentialGroup().add(jPanel2Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.BASELINE).add(self.imageHeightIsFrameSizeJCheckBox, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(self.horizontalJCheckBox).add(self.verticleJCheckBox).add(self.writeOverOriginalJCheckBox).add(self.generateJButton, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, 25, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE)).addContainerGap()))
        self.jLabel2.setText("Results:")
        jPanel3Layout: GroupLayout = GroupLayout(self.jPanel3)
        self.jPanel3.setLayout(jPanel3Layout)
        jPanel3Layout.setHorizontalGroup(jPanel3Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(jPanel3Layout.createSequentialGroup().add(self.jLabel2).addContainerGap(448, Short.MAX_VALUE)))
        jPanel3Layout.setVerticalGroup(jPanel3Layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(self.jLabel2))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING, layout.createSequentialGroup().addContainerGap().add(self.jPanel3, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addContainerGap()).add(self.jPanel1, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(layout.createSequentialGroup().add(self.jPanel2, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addContainerGap(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(layout.createSequentialGroup().add(self.jPanel2, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, 25, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.jPanel3, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(self.jPanel1, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
    

    def generateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def imageHeightIsFrameSizeJCheckBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        self.imageProcessorInput = imageProcessorInput
# from java.awt.Graphics import Graphics
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from java.io.File import File
# from javax.imageio.ImageIO import ImageIO
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.media.image.BufferedImageUtil2 import BufferedImageUtil2
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageStrings import ImageStrings
# from org.allbinary.media.image.MirrorImageUtil import MirrorImageUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.JButton import JButton
# from javax.swing.JCheckBox import JCheckBox
# from javax.swing.JLabel import JLabel
# from javax.swing.JLayeredPane import JLayeredPane


