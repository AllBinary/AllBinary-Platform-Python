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

import threading
from org.allbinary.media.image.ImageProcessedVisitor import ImageProcessedVisitor
from org.allbinary.image.gui.JPanel import JPanel


class RotationImageJPanel(JPanel, ImageProcessedVisitor):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageStrings: ImageStrings = ImageStrings.getInstance()
        self.imageProcessorInput: ImageProcessorInput = None
        self.result: BufferedImage = None
        self.generateJButton: JButton = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.jLabel3: JLabel = None
        self.jPanel1: JPanel = None
        self.jPanel2: JPanel = None
        self.jPanel3: JPanel = None
        self.totalAngleJComboBox: JComboBox = None
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
#                     angleAsString: str = self.totalAngleJComboBox.getSelectedItem()
#                     ImageArrayRotationUtil.getInstance().process(self.getImageProcessorInput(), angleAsString, self)
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JComboBox import JComboBox
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JCheckBox import JCheckBox
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        self.jPanel1 = (JPanel()  # Java anonymous class body:
#             
# 
#             def paint(self, graphics: Graphics) -> None:
#                 if self.result is not None:
#                     graphics.drawImage(self.result, 0, 0, self.result.getWidth(None), self.result.getHeight(None), None)
)
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
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(0, 436, Short.MAX_VALUE))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(0, 227, Short.MAX_VALUE))
        self.generateJButton.setText("Generate")
        self.generateJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.generateJButtonActionPerformed(evt)
))
        self.totalAngleJComboBox.setModel(DefaultComboBoxModel([self.commonStrings.UP, self.commonStrings.DOWN, "-90", "90"]))
        self.totalAngleJComboBox.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.totalAngleJComboBoxActionPerformed(evt)
))
        self.jLabel3.setText("Total Angle:")
        self.writeOverOriginalJCheckBox.setText("Write Over Original")
        jPanel2Layout: GroupLayout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(jPanel2Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(jPanel2Layout.createSequentialGroup().add(8, 8, 8).add(self.jLabel1).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.jLabel3).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.totalAngleJComboBox, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.writeOverOriginalJCheckBox).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.generateJButton).addContainerGap(org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        jPanel2Layout.setVerticalGroup(jPanel2Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(jPanel2Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.BASELINE).add(self.jLabel1).add(self.generateJButton).add(self.totalAngleJComboBox, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).add(self.jLabel3).add(self.writeOverOriginalJCheckBox)))
        self.jLabel2.setText("Results:")
        jPanel3Layout: GroupLayout = GroupLayout(self.jPanel3)
        self.jPanel3.setLayout(jPanel3Layout)
        jPanel3Layout.setHorizontalGroup(jPanel3Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(jPanel3Layout.createSequentialGroup().add(self.jLabel2).addContainerGap(377, Short.MAX_VALUE)))
        jPanel3Layout.setVerticalGroup(jPanel3Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(self.jLabel2))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(org.jdesktop.layout.GroupLayout.TRAILING, self.jPanel2, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(layout.createSequentialGroup().addContainerGap().add(self.jPanel3, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addContainerGap()).add(self.jPanel1, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(layout.createSequentialGroup().add(self.jPanel2, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).addPreferredGap(org.jdesktop.layout.LayoutStyle.UNRELATED).add(self.jPanel3, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.jPanel1, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
    

    def generateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def totalAngleJComboBoxActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        self.imageProcessorInput = imageProcessorInput
    

    # throws IOException
    def visit(self, generatedBufferedImage: BufferedImage, name: str, index: int) -> None:
        self.result = generatedBufferedImage
        self.getParent().repaint()
        file: File = self.imageProcessorInput.getFiles()[index]
        if not self.writeOverOriginalJCheckBox.isSelected():
            filePath: str = file.getAbsolutePath()
            extensionIndex: int = filePath.find(self.imageStrings.PNG_EXTENSION)
            filePath = str(StringMaker().append(filePath[0:extensionIndex]).append(CommonSeps.getInstance().UNDERSCORE).append(name).append(self.imageStrings.PNG_EXTENSION))
            file = File(filePath)
        isWritten: bool = ImageIO.write(self.result, self.imageStrings.PNG, file)
        self.logUtil.putF("File: " + str(file) + " Wrote: " + str(isWritten), self, self.commonStrings.RUN)
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from java.io.File import File
# from java.io.IOException import IOException
# from javax.imageio.ImageIO import ImageIO
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.image.ImageArrayRotationUtil import ImageArrayRotationUtil
from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
from org.allbinary.media.image.ImageStrings import ImageStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


