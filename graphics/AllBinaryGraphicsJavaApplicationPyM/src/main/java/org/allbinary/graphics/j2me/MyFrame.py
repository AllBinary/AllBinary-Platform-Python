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
# package org.allbinary.graphics.j2me

from __future__ import annotations

import sys
import threading
from org.allbinary.gui.dialog.FileJDialogListenerInterface import FileJDialogListenerInterface
from org.allbinary.gui.dialog.HashMapJDialogListenerInterface import HashMapJDialogListenerInterface
from org.allbinary.graphics.j2me.JFrame import JFrame
from org.allbinary.graphics.j2me.KeyListener import KeyListener


class MyFrame(JFrame, FileJDialogListenerInterface, HashMapJDialogListenerInterface, KeyListener):
    MAXWORKAREAS: int = 10
    numberOfWorkAreas: int = 0
    PATH: str = "G:/mnt/bc/mydev/work/graphics/AllBinaryGraphicsJavaApplication"
    SAVE_PATH: str = None
    TEMPLATE_EXPORT_PATH: str = None
    statusJLabel: JLabel = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.guiLog: GuiLog = GuiLog.getInstance()
        self.xslHelper: XslHelper = XslHelper.getInstance()
        self.JAVA_TEMPLATE: str = "svgExport.xsl"
        self.SAVEEXTENSION: str = ".gxml"
        self.JAVAEXTENSION: str = ".javax"
        self.fileJDialog: FileJDialog = None
        self.rotateJDialog: RotateJDialog = None
        self.animateJButton: JButton = None
        self.autoDamageJMenuItem: JMenuItem = None
        self.autoExplodeJMenuItem: JMenuItem = None
        self.autoGrowJMenuItem: JMenuItem = None
        self.autoRotateGenerationJMenuItem: JMenuItem = None
        self.autoSheildMenuItem: JMenuItem = None
        self.autoShrinkJMenuItem: JMenuItem = None
        self.centerJMenuItem: JMenuItem = None
        self.copyJMenuItem1: JMenuItem = None
        self.exitJMenuItem: JMenuItem = None
        self.explodeAllJMenuItem: JMenuItem = None
        self.exportJMenuItem1: JMenuItem = None
        self.fileJMenu: JMenu = None
        self.frameJMenu: JMenu = None
        self.generateJMenu: JMenu = None
        self.insertAfterJMenuItem: JMenuItem = None
        self.insertBeforeJMenuItem: JMenuItem = None
        self.jButton1: JButton = None
        self.jButton2: JButton = None
        self.jButton3: JButton = None
        self.jButton4: JButton = None
        self.jButton41: JButton = None
        self.jButton5: JButton = None
        self.jMenu1: JMenu = None
        self.jMenuItem1: JMenuItem = None
        self.jPanel1: JPanel = None
        self.jTabbedPane: JTabbedPane = None
        self.jToolBar1: JToolBar = None
        self.mainJPanel: JPanel = None
        self.menuJMenuBar: JMenuBar = None
        self.newJMenuItem: JMenuItem = None
        self.nextFrameJMenuItem: JMenuItem = None
        self.objectJMenu: JMenu = None
        self.openJButton: JButton = None
        self.openJMenuItem: JMenuItem = None
        self.playJButton: JButton = None
        self.previousFrameJMenuItem: JMenuItem = None
        self.removeJMenuItem: JMenuItem = None
        self.saveAsJMenuItem: JMenuItem = None
        self.saveJButton: JButton = None
        self.saveJMenuItem: JMenuItem = None
        self.statusJPanel: JPanel = None
        self.stopJjButton: JButton = None
        self.viewJMenu: JMenu = None
        self.zoomInJMenuItem: JMenuItem = None
        self.zoomOutJMenuItem: JMenuItem = None
    

    def __init__(self) -> None:
        from org.allbinary.graphics.j2me.Dimension import Dimension
        from org.allbinary.graphics.j2me.Dimension import Dimension
        from org.allbinary.graphics.j2me.Dimension import Dimension
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.setSize(Dimension(550, 400))
        self.mainJPanel.setSize(Dimension(550, 400))
        self.jTabbedPane.setSize(Dimension(550, 400))
        self.fileJDialog = FileJDialog()
        self.fileJDialog.addFinishedListener(self)
        self.rotateJDialog = RotateJDialog(self, False)
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.JToolBar import JToolBar
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JButton import JButton
        from org.allbinary.graphics.j2me.JPanel import JPanel
        from org.allbinary.graphics.j2me.JPanel import JPanel
        from org.allbinary.graphics.j2me.JTabbedPane import JTabbedPane
        from org.allbinary.graphics.j2me.JPanel import JPanel
        from org.allbinary.graphics.j2me.JLabel import JLabel
        from org.allbinary.graphics.j2me.JMenuBar import JMenuBar
        from org.allbinary.graphics.j2me.JMenu import JMenu
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenu import JMenu
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenu import JMenu
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenu import JMenu
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenu import JMenu
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenuItem import JMenuItem
        from org.allbinary.graphics.j2me.JMenu import JMenu
        from org.allbinary.graphics.j2me.WindowAdapter import WindowAdapter
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.Dimension import Dimension
        from org.allbinary.graphics.j2me.ChangeListener import ChangeListener
        from org.allbinary.graphics.j2me.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.ActionListener import ActionListener
        from org.allbinary.graphics.j2me.MouseAdapter import MouseAdapter
        self.jToolBar1 = JToolBar()
        self.jButton2 = JButton()
        self.saveJButton = JButton()
        self.jButton1 = JButton()
        self.openJButton = JButton()
        self.jButton3 = JButton()
        self.jButton4 = JButton()
        self.jButton41 = JButton()
        self.jButton5 = JButton()
        self.animateJButton = JButton()
        self.playJButton = JButton()
        self.stopJjButton = JButton()
        self.jPanel1 = JPanel()
        self.mainJPanel = JPanel()
        self.jTabbedPane = JTabbedPane()
        self.statusJPanel = JPanel()
        MyFrame.statusJLabel = JLabel()
        self.menuJMenuBar = JMenuBar()
        self.fileJMenu = JMenu()
        self.newJMenuItem = JMenuItem()
        self.openJMenuItem = JMenuItem()
        self.saveJMenuItem = JMenuItem()
        self.saveAsJMenuItem = JMenuItem()
        self.exportJMenuItem1 = JMenuItem()
        self.exitJMenuItem = JMenuItem()
        self.viewJMenu = JMenu()
        self.zoomInJMenuItem = JMenuItem()
        self.zoomOutJMenuItem = JMenuItem()
        self.objectJMenu = JMenu()
        self.explodeAllJMenuItem = JMenuItem()
        self.frameJMenu = JMenu()
        self.previousFrameJMenuItem = JMenuItem()
        self.nextFrameJMenuItem = JMenuItem()
        self.removeJMenuItem = JMenuItem()
        self.copyJMenuItem1 = JMenuItem()
        self.insertAfterJMenuItem = JMenuItem()
        self.insertBeforeJMenuItem = JMenuItem()
        self.generateJMenu = JMenu()
        self.centerJMenuItem = JMenuItem()
        self.autoDamageJMenuItem = JMenuItem()
        self.autoExplodeJMenuItem = JMenuItem()
        self.autoGrowJMenuItem = JMenuItem()
        self.jMenuItem1 = JMenuItem()
        self.autoRotateGenerationJMenuItem = JMenuItem()
        self.autoSheildMenuItem = JMenuItem()
        self.autoShrinkJMenuItem = JMenuItem()
        self.jMenu1 = JMenu()
        self.addWindowListener((WindowAdapter()  # Java anonymous class body:
#             
# 
#             def windowClosing(self, evt: WindowEvent) -> None:
#                 self.exitForm(evt)
))
        self.jButton2.setText("New")
        self.jButton2.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jButton2ActionPerformed(evt)
))
        self.jToolBar1.add(self.jButton2)
        self.saveJButton.setText("Save")
        self.saveJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.saveJButtonActionPerformed(evt)
))
        self.jToolBar1.add(self.saveJButton)
        self.jButton1.setText("Export")
        self.jButton1.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jButton1ActionPerformed(evt)
))
        self.jToolBar1.add(self.jButton1)
        self.openJButton.setText("Open")
        self.openJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.openJButtonActionPerformed(evt)
))
        self.jToolBar1.add(self.openJButton)
        self.jButton3.setText("Copy")
        self.jToolBar1.add(self.jButton3)
        self.jButton4.setText("Insert Before")
        self.jToolBar1.add(self.jButton4)
        self.jButton41.setText("Insert After")
        self.jToolBar1.add(self.jButton41)
        self.jButton5.setText("Delete")
        self.jToolBar1.add(self.jButton5)
        self.animateJButton.setText("AnimateEdit")
        self.jToolBar1.add(self.animateJButton)
        self.playJButton.setText("Play")
        self.playJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.playJButtonMousePressed(evt)
))
        self.jToolBar1.add(self.playJButton)
        self.stopJjButton.setText("Stop")
        self.stopJjButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.stopJjButtonMousePressed(evt)
))
        self.jToolBar1.add(self.stopJjButton)
        self.getContentPane().add(self.jToolBar1, java.awt.BorderLayout.NORTH)
        self.jPanel1.setLayout(GridLayout(1, 0))
        self.mainJPanel.setLayout(GridLayout(1, 0))
        self.jTabbedPane.setMinimumSize(Dimension(550, 400))
        self.jTabbedPane.addChangeListener((ChangeListener()  # Java anonymous class body:
#             
# 
#             def stateChanged(self, evt: ChangeEvent) -> None:
#                 self.jTabbedPaneStateChanged(evt)
))
        self.mainJPanel.add(self.jTabbedPane)
        self.jPanel1.add(self.mainJPanel)
        self.getContentPane().add(self.jPanel1, java.awt.BorderLayout.CENTER)
        self.statusJPanel.setLayout(GridLayout(1, 0))
        MyFrame.statusJLabel.setText("Status Bar")
        self.statusJPanel.add(MyFrame.statusJLabel)
        self.getContentPane().add(self.statusJPanel, java.awt.BorderLayout.SOUTH)
        self.fileJMenu.setText("File")
        self.fileJMenu.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.fileJMenuActionPerformed(evt)
))
        self.newJMenuItem.setText("New")
        self.newJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.newJMenuItemActionPerformed(evt)
))
        self.fileJMenu.add(self.newJMenuItem)
        self.openJMenuItem.setText("Open")
        self.openJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.openJMenuItemActionPerformed(evt)
))
        self.fileJMenu.add(self.openJMenuItem)
        self.saveJMenuItem.setText("Save")
        self.saveJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.saveJMenuItemMousePressed(evt)
))
        self.fileJMenu.add(self.saveJMenuItem)
        self.saveAsJMenuItem.setText("SaveAs")
        self.fileJMenu.add(self.saveAsJMenuItem)
        self.exportJMenuItem1.setText("Export")
        self.exportJMenuItem1.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.exportJMenuItem1ActionPerformed(evt)
))
        self.fileJMenu.add(self.exportJMenuItem1)
        self.exitJMenuItem.setText("Exit")
        self.exitJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.exitJMenuItemActionPerformed(evt)
))
        self.fileJMenu.add(self.exitJMenuItem)
        self.menuJMenuBar.add(self.fileJMenu)
        self.viewJMenu.setText("View")
        self.zoomInJMenuItem.setText("Zoom In")
        self.zoomInJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.zoomInJMenuItemMousePressed(evt)
))
        self.viewJMenu.add(self.zoomInJMenuItem)
        self.zoomOutJMenuItem.setText("Zoom Out")
        self.zoomOutJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.zoomOutJMenuItemMousePressed(evt)
))
        self.viewJMenu.add(self.zoomOutJMenuItem)
        self.menuJMenuBar.add(self.viewJMenu)
        self.objectJMenu.setText("Objects")
        self.explodeAllJMenuItem.setText("Explode All")
        self.explodeAllJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.explodeAllJMenuItemMousePressed(evt)
))
        self.objectJMenu.add(self.explodeAllJMenuItem)
        self.menuJMenuBar.add(self.objectJMenu)
        self.frameJMenu.setText("Frame")
        self.frameJMenu.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.frameJMenuActionPerformed(evt)
))
        self.previousFrameJMenuItem.setText("Previous")
        self.frameJMenu.add(self.previousFrameJMenuItem)
        self.nextFrameJMenuItem.setText(CommonLabels.getInstance().NEXT)
        self.frameJMenu.add(self.nextFrameJMenuItem)
        self.removeJMenuItem.setText("Remove")
        self.frameJMenu.add(self.removeJMenuItem)
        self.copyJMenuItem1.setText("Copy")
        self.frameJMenu.add(self.copyJMenuItem1)
        self.insertAfterJMenuItem.setText("Ins After")
        self.frameJMenu.add(self.insertAfterJMenuItem)
        self.insertBeforeJMenuItem.setText("Ins Before")
        self.frameJMenu.add(self.insertBeforeJMenuItem)
        self.menuJMenuBar.add(self.frameJMenu)
        self.generateJMenu.setText("Generate")
        self.centerJMenuItem.setText("Center")
        self.centerJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.centerJMenuItemActionPerformed(evt)
))
        self.generateJMenu.add(self.centerJMenuItem)
        self.autoDamageJMenuItem.setText("Damage")
        self.generateJMenu.add(self.autoDamageJMenuItem)
        self.autoExplodeJMenuItem.setText("Explode")
        self.autoExplodeJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.autoExplodeJMenuItemMousePressed(evt)
))
        self.generateJMenu.add(self.autoExplodeJMenuItem)
        self.autoGrowJMenuItem.setText("Grow")
        self.generateJMenu.add(self.autoGrowJMenuItem)
        self.jMenuItem1.setText("Mirror")
        self.jMenuItem1.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jMenuItem1ActionPerformed(evt)
))
        self.generateJMenu.add(self.jMenuItem1)
        self.autoRotateGenerationJMenuItem.setText("Rotate")
        self.autoRotateGenerationJMenuItem.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.autoRotateGenerationJMenuItemMousePressed(evt)
))
        self.generateJMenu.add(self.autoRotateGenerationJMenuItem)
        self.autoSheildMenuItem.setText("Shield")
        self.generateJMenu.add(self.autoSheildMenuItem)
        self.autoShrinkJMenuItem.setText("Shrink")
        self.generateJMenu.add(self.autoShrinkJMenuItem)
        self.menuJMenuBar.add(self.generateJMenu)
        self.jMenu1.setText("Help")
        self.menuJMenuBar.add(self.jMenu1)
        self.setJMenuBar(self.menuJMenuBar)
        self.pack()
    

    def explodeAllJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        try:
            MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.EXPLODE, None)))
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "explodeAllJMenuItemMousePressed", e)
    

    def autoExplodeJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        try:
            MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.AUTOEXPLODE, None)))
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "autoExplodeJMenuItemMousePressed", e)
    

    def stopJjButtonMousePressed(self, evt: MouseEvent) -> None:
        self.getSelectedWorkArea().stop()
    

    def playJButtonMousePressed(self, evt: MouseEvent) -> None:
        self.getSelectedWorkArea().play()
    

    def autoRotateGenerationJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        self.rotateJDialog.setVisible(True)
    

    def zoomOutJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        self.getSelectedWorkArea().changeZoom(-1)
    

    def zoomInJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        self.getSelectedWorkArea().changeZoom(1)
    

    def openJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        self.openGraphics()
    

    def exportJMenuItem1ActionPerformed(self, evt: ActionEvent) -> None:
        self.export()
    

    def saveJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        self.save()
    

    def jTabbedPaneStateChanged(self, evt: ChangeEvent) -> None:
        self.updateSelectedWorkArea()
    

    def frameJMenuActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def exitJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        sys.exit(0)
    

    def newJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        self.newGraphics()
    

    def fileJMenuActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def exitForm(self, evt: WindowEvent) -> None:
        sys.exit(0)
    

    def openJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.openGraphics()
    

    def jButton2ActionPerformed(self, evt: ActionEvent) -> None:
        self.newGraphics()
    

    def centerJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        try:
            MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.CENTER, None)))
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "centerJMenuItemActionPerformed", e)
    

    def saveJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.save()
    

    def jButton1ActionPerformed(self, evt: ActionEvent) -> None:
        self.export()
    

    def jMenuItem1ActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.getSelectedWorkArea().autoMirror()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "centerJMenuItemActionPerformed", e)
    

    def onFiles(self, files: list[File]) -> None:
        from org.allbinary.graphics.j2me.GridLayout import GridLayout
        try:
            self.logUtil.putF("Reading: " + str(files), self, "onFiles")
            for index in range(0, len(files)):
                document: Document = DomHelper.getInstance().createDocument(files[index])
                workAreaJPanel: WorkAreaJPanel = WorkAreaJPanel(WorkAreaDom(document), self.getSize())
                workAreaJPanel.setLayout(GridLayout(1, 1))
                self.add(workAreaJPanel)
            self.fileJDialog.setVisible(False)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onFiles", e)
    

    def newGraphics(self) -> None:
        try:
            newName: str = "graphic" + str(MyFrame.numberOfWorkAreas)
            dim: Dimension = self.getSize()
            newDialog: NewWorkAreaJDialog = NewWorkAreaJDialog(self, False, dim, newName)
        except Exception as e:
            if self.LOGGING.contains(self.LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "newJMenuItemActionPerformed", e)
    

    def openGraphics(self) -> None:
        try:
            self.logUtil.putF("Starting", self, "openImageJMenuItemActionPerformed")
            self.fileJDialog.setVisible(True)
        except Exception as e:
            if self.LOGGING.contains(self.LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "open", e)
    

    def export(self) -> None:
        try:
            workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getSelectedComponent()
            file: File = File(self.SAVE_PATH + "/" + workAreaJPanel.getName() + self.JAVAEXTENSION)
            document: Document = workAreaJPanel.toDocument()
            self.logUtil.putF("Export: " + DomHelper.getInstance().toString(document), self, "exportJMenuItem1ActionPerformed")
            self.xslHelper.export(file, str(MyFrame.TEMPLATE_EXPORT_PATH) + "/" + self.JAVA_TEMPLATE, document)
        except Exception as e:
            if self.LOGGING.contains(self.LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "export", e)
    

    def save(self) -> None:
        try:
            workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getSelectedComponent()
            DomHelper.getInstance().save(File(self.SAVE_PATH + "/" + workAreaJPanel.getName() + self.SAVEEXTENSION), workAreaJPanel.toDocument())
        except Exception as e:
            if self.LOGGING.contains(self.LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, self.commonStrings.SAVE, e)
    

    # throws Exception
    def onHashMap(self, hashMap: dict) -> None:
        angleIncrementInteger: int = hashMap.get(str(0))
        totalRotationInteger: int = hashMap.get(str(1))
        self.getSelectedWorkArea().autoRotate(int(angleIncrementInteger), int(totalRotationInteger))
    

    def getSelectedWorkArea(self) -> WorkAreaJPanelInterface:
        return self.jTabbedPane.getSelectedComponent()
    

    def updateSelectedWorkArea(self) -> None:
        numberOfTabs: int = self.jTabbedPane.getTabCount()
        for index in range(0, numberOfTabs):
            workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getComponentAt(index)
            workAreaJPanel.deselect()
        workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getSelectedComponent()
        if workAreaJPanel is not None:
            workAreaJPanel.select()
    

    # throws Exception
    def add(self, newCanvasInterface: WorkAreaJPanelInterface) -> None:
        try:
            self.numberOfWorkAreas += 1
            if self.numberOfWorkAreas == MyFrame.MAXWORKAREAS:
                raise Exception()
            self.jTabbedPane.addTab(newCanvasInterface.getName(), newCanvasInterface)
            self.jTabbedPane.setSelectedComponent(newCanvasInterface)
            animationThread: threading.Thread = threading.Thread(target=newCanvasInterface.run)
            animationThread.start()
            self.updateSelectedWorkArea()
        except Exception as e:
            if self.LOGGING.contains(self.LOGGING.GRAPHICSCREATION):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "addNewCanvas", e)
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        self.getSelectedWorkArea().keyPressed(keyEvent)
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        pass
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        pass
    

    @staticmethod
    def main(args: list[str]) -> None:
        try:
            AngleFactory.getInstance()
            SmallIntegerSingletonFactory.getInstance().init()
            MyFrame().show()
        except Exception as e:
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.put(CommonStrings.getInstance().EXCEPTION, None, "main", e)
# from java.awt import *
# from java.io.File import File
# from java.util.HashMap import HashMap
# from javax.swing import *
from org.allbinary.data.tree.dom.XslHelper import XslHelper
from org.allbinary.dom.DomHelper import DomHelper
from org.allbinary.graphics.j2me.dialog.NewWorkAreaJDialog import NewWorkAreaJDialog
from org.allbinary.graphics.j2me.dialog.RotateJDialog import RotateJDialog
from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
from org.allbinary.gui.dialog.FileJDialog import FileJDialog
from org.allbinary.log.LOGGING import LOGGING
from org.allbinary.logic.communication.log.GuiLog import GuiLog
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document


MyFrame.SAVE_PATH = str(MyFrame.PATH) + "/save"

MyFrame.TEMPLATE_EXPORT_PATH = str(MyFrame.PATH) + "/templates/export"

