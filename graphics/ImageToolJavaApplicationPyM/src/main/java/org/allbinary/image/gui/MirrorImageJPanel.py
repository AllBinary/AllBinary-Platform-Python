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
from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
from org.allbinary.image.gui.JPanel import JPanel


class MirrorImageJPanel(JPanel, ImageProcessorInputCompositeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageStrings: ImageStrings = ImageStrings.getInstance()
        self.imageProcessorInput: ImageProcessorInput = None
        self.result: BufferedImage = None
        self.buttonGroup: ButtonGroup = None
        self.generateJButton: JButton = None
        self.horizontalJCheckBox: JCheckBox = None
        self.jLabel2: JLabel = None
        self.jLayeredPane1: JLayeredPane = None
        self.jPanel1: JPanel = None
        self.jPanel2: JPanel = None
        self.jPanel3: JPanel = None
        self.renameJRadioButton: JRadioButton = None
        self.verticleJCheckBox: JCheckBox = None
        self.writeOverOriginalJRadioButton: JRadioButton = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        super().__init__()
        self._init_fields()
        self.logUtil.putF("Starting", self, self.commonStrings.CONSTRUCTOR)
        self.initComponents()
        self.imageProcessorInput = imageProcessorInput
    

    def process(self) -> None:
        (threading.Thread()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     imageProcessorInput: ImageProcessorInput = self.getImageProcessorInput()
#                     bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
#                     for index in range(0, len(bufferedImageArray)):
#                         self.result = MirrorImageUtil.getInstance().getImage(bufferedImageArray[index], self.verticleJCheckBox.isSelected(), self.horizontalJCheckBox.isSelected())
#                         file: File = imageProcessorInput.getFiles()[index]
#                         if self.writeOverOriginalJRadioButton.isSelected():
#                             pass
#                         elif self.renameJRadioButton.isSelected():
#                             filePath: str = file.getAbsolutePath()
#                             extensionIndex: int = filePath.find(self.imageStrings.PNG_EXTENSION)
#                             filePath = filePath[0:extensionIndex] + "_mirror" + str(self.imageStrings.PNG_EXTENSION)
#                             logUtil.putF("Renamed File: " + filePath, self, self.commonStrings.RUN)
#                             file = File(filePath)
#                         isWritten: bool = ImageIO.write(self.result, self.imageStrings.PNG, file)
#                         logUtil.putF("File: " + str(file) + " Wrote: " + str(isWritten), self, self.commonStrings.RUN)
#                         self.getParent().repaint()
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.JLayeredPane import JLayeredPane
        from org.allbinary.image.gui.ButtonGroup import ButtonGroup
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JCheckBox import JCheckBox
        from org.allbinary.image.gui.JCheckBox import JCheckBox
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JRadioButton import JRadioButton
        from org.allbinary.image.gui.JRadioButton import JRadioButton
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        self.jLayeredPane1 = JLayeredPane()
        self.buttonGroup = ButtonGroup()
        self.jPanel1 = (JPanel()  # Java anonymous class body:
#             
# 
#             def paint(self, graphics: Graphics) -> None:
#                 if self.result is not None:
#                     graphics.drawImage(self.result, 0, 0, self.result.getWidth(None), self.result.getHeight(None), None)
)
        self.jPanel2 = JPanel()
        self.horizontalJCheckBox = JCheckBox()
        self.verticleJCheckBox = JCheckBox()
        self.generateJButton = JButton()
        self.renameJRadioButton = JRadioButton()
        self.writeOverOriginalJRadioButton = JRadioButton()
        self.jPanel3 = JPanel()
        self.jLabel2 = JLabel()
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(0, 522, Short.MAX_VALUE))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(0, 230, Short.MAX_VALUE))
        self.horizontalJCheckBox.setSelected(True)
        self.horizontalJCheckBox.setText("Horizontal")
        self.horizontalJCheckBox.setEnabled(False)
        self.verticleJCheckBox.setText("Verticle")
        self.verticleJCheckBox.setEnabled(False)
        self.generateJButton.setText("Generate")
        self.generateJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.generateJButtonActionPerformed(evt)
))
        self.renameJRadioButton.setText("Save As filename_mirror")
        self.renameJRadioButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.renameJRadioButtonActionPerformed(evt)
))
        self.writeOverOriginalJRadioButton.setText("Write Over Original")
        jPanel2Layout: GroupLayout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(jPanel2Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(jPanel2Layout.createSequentialGroup().addContainerGap(org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(self.verticleJCheckBox).addPreferredGap(org.jdesktop.layout.LayoutStyle.UNRELATED).add(self.horizontalJCheckBox).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.writeOverOriginalJRadioButton).addPreferredGap(org.jdesktop.layout.LayoutStyle.UNRELATED).add(self.renameJRadioButton).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.generateJButton).add(37, 37, 37)))
        jPanel2Layout.setVerticalGroup(jPanel2Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(jPanel2Layout.createSequentialGroup().add(jPanel2Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.BASELINE).add(self.horizontalJCheckBox).add(self.verticleJCheckBox).add(self.writeOverOriginalJRadioButton).add(self.renameJRadioButton).add(self.generateJButton)).addContainerGap()))
        self.jLabel2.setText("Results:")
        jPanel3Layout: GroupLayout = GroupLayout(self.jPanel3)
        self.jPanel3.setLayout(jPanel3Layout)
        jPanel3Layout.setHorizontalGroup(jPanel3Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(jPanel3Layout.createSequentialGroup().add(self.jLabel2).addContainerGap(433, Short.MAX_VALUE)))
        jPanel3Layout.setVerticalGroup(jPanel3Layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(self.jLabel2))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(org.jdesktop.layout.GroupLayout.TRAILING, layout.createSequentialGroup().addContainerGap().add(self.jPanel3, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addContainerGap()).add(self.jPanel1, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).add(layout.createSequentialGroup().add(self.jPanel2, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addContainerGap(org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(layout.createSequentialGroup().add(self.jPanel2, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, 25, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.jPanel3, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(self.jPanel1, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
    

    def generateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def renameJRadioButtonActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        self.imageProcessorInput = imageProcessorInput
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from java.io.File import File
# from javax.imageio.ImageIO import ImageIO
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
from org.allbinary.media.image.ImageStrings import ImageStrings
from org.allbinary.media.image.MirrorImageUtil import MirrorImageUtil
from org.allbinary.string.CommonStrings import CommonStrings


