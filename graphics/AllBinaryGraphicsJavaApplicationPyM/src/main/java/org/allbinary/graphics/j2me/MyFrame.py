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

from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import sys
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.gui.dialog.FileJDialogListenerInterface import FileJDialogListenerInterface
from org.allbinary.gui.dialog.HashMapJDialogListenerInterface import HashMapJDialogListenerInterface
# from java.awt.event.KeyListener import KeyListener
# from javax.swing.JFrame import JFrame


@java_inherited_overloads
class MyFrame(*java_bases(JFrame, FileJDialogListenerInterface, HashMapJDialogListenerInterface, KeyListener)):
    MAXWORKAREAS: int = 10
    numberOfWorkAreas: int = 0
    PATH: str = "G:/mnt/bc/mydev/work/graphics/AllBinaryGraphicsJavaApplication"
    SAVE_PATH: str = None
    TEMPLATE_EXPORT_PATH: str = None
    statusJLabel: JLabel = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("guiLog", None)
        vars(self).setdefault("xslHelper", None)
        vars(self).setdefault("JAVA_TEMPLATE", None)
        vars(self).setdefault("SAVEEXTENSION", None)
        vars(self).setdefault("JAVAEXTENSION", None)
        vars(self).setdefault("fileJDialog", None)
        vars(self).setdefault("rotateJDialog", None)
        vars(self).setdefault("animateJButton", None)
        vars(self).setdefault("autoDamageJMenuItem", None)
        vars(self).setdefault("autoExplodeJMenuItem", None)
        vars(self).setdefault("autoGrowJMenuItem", None)
        vars(self).setdefault("autoRotateGenerationJMenuItem", None)
        vars(self).setdefault("autoSheildMenuItem", None)
        vars(self).setdefault("autoShrinkJMenuItem", None)
        vars(self).setdefault("centerJMenuItem", None)
        vars(self).setdefault("copyJMenuItem1", None)
        vars(self).setdefault("exitJMenuItem", None)
        vars(self).setdefault("explodeAllJMenuItem", None)
        vars(self).setdefault("exportJMenuItem1", None)
        vars(self).setdefault("fileJMenu", None)
        vars(self).setdefault("frameJMenu", None)
        vars(self).setdefault("generateJMenu", None)
        vars(self).setdefault("insertAfterJMenuItem", None)
        vars(self).setdefault("insertBeforeJMenuItem", None)
        vars(self).setdefault("jButton1", None)
        vars(self).setdefault("jButton2", None)
        vars(self).setdefault("jButton3", None)
        vars(self).setdefault("jButton4", None)
        vars(self).setdefault("jButton41", None)
        vars(self).setdefault("jButton5", None)
        vars(self).setdefault("jMenu1", None)
        vars(self).setdefault("jMenuItem1", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("jTabbedPane", None)
        vars(self).setdefault("jToolBar1", None)
        vars(self).setdefault("mainJPanel", None)
        vars(self).setdefault("menuJMenuBar", None)
        vars(self).setdefault("newJMenuItem", None)
        vars(self).setdefault("nextFrameJMenuItem", None)
        vars(self).setdefault("objectJMenu", None)
        vars(self).setdefault("openJButton", None)
        vars(self).setdefault("openJMenuItem", None)
        vars(self).setdefault("playJButton", None)
        vars(self).setdefault("previousFrameJMenuItem", None)
        vars(self).setdefault("removeJMenuItem", None)
        vars(self).setdefault("saveAsJMenuItem", None)
        vars(self).setdefault("saveJButton", None)
        vars(self).setdefault("saveJMenuItem", None)
        vars(self).setdefault("statusJPanel", None)
        vars(self).setdefault("stopJjButton", None)
        vars(self).setdefault("viewJMenu", None)
        vars(self).setdefault("zoomInJMenuItem", None)
        vars(self).setdefault("zoomOutJMenuItem", None)

    def _init_fields(self) -> None:
        from org.allbinary.data.tree.dom.XslHelper import XslHelper
        from org.allbinary.logic.communication.log.GuiLog import GuiLog
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.guiLog: GuiLog = GuiLog.getInstance()
        self.xslHelper: XslHelper = XslHelper.getInstance()
        self.JAVA_TEMPLATE: str = "svgExport.xsl"
        self.SAVEEXTENSION: str = ".gxml"
        self.JAVAEXTENSION: str = ".javax"
        if "fileJDialog" not in vars(self): self.fileJDialog: FileJDialog = None
        if "rotateJDialog" not in vars(self): self.rotateJDialog: RotateJDialog = None
        if "animateJButton" not in vars(self): self.animateJButton: JButton = None
        if "autoDamageJMenuItem" not in vars(self): self.autoDamageJMenuItem: JMenuItem = None
        if "autoExplodeJMenuItem" not in vars(self): self.autoExplodeJMenuItem: JMenuItem = None
        if "autoGrowJMenuItem" not in vars(self): self.autoGrowJMenuItem: JMenuItem = None
        if "autoRotateGenerationJMenuItem" not in vars(self): self.autoRotateGenerationJMenuItem: JMenuItem = None
        if "autoSheildMenuItem" not in vars(self): self.autoSheildMenuItem: JMenuItem = None
        if "autoShrinkJMenuItem" not in vars(self): self.autoShrinkJMenuItem: JMenuItem = None
        if "centerJMenuItem" not in vars(self): self.centerJMenuItem: JMenuItem = None
        if "copyJMenuItem1" not in vars(self): self.copyJMenuItem1: JMenuItem = None
        if "exitJMenuItem" not in vars(self): self.exitJMenuItem: JMenuItem = None
        if "explodeAllJMenuItem" not in vars(self): self.explodeAllJMenuItem: JMenuItem = None
        if "exportJMenuItem1" not in vars(self): self.exportJMenuItem1: JMenuItem = None
        if "fileJMenu" not in vars(self): self.fileJMenu: JMenu = None
        if "frameJMenu" not in vars(self): self.frameJMenu: JMenu = None
        if "generateJMenu" not in vars(self): self.generateJMenu: JMenu = None
        if "insertAfterJMenuItem" not in vars(self): self.insertAfterJMenuItem: JMenuItem = None
        if "insertBeforeJMenuItem" not in vars(self): self.insertBeforeJMenuItem: JMenuItem = None
        if "jButton1" not in vars(self): self.jButton1: JButton = None
        if "jButton2" not in vars(self): self.jButton2: JButton = None
        if "jButton3" not in vars(self): self.jButton3: JButton = None
        if "jButton4" not in vars(self): self.jButton4: JButton = None
        if "jButton41" not in vars(self): self.jButton41: JButton = None
        if "jButton5" not in vars(self): self.jButton5: JButton = None
        if "jMenu1" not in vars(self): self.jMenu1: JMenu = None
        if "jMenuItem1" not in vars(self): self.jMenuItem1: JMenuItem = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "jTabbedPane" not in vars(self): self.jTabbedPane: JTabbedPane = None
        if "jToolBar1" not in vars(self): self.jToolBar1: JToolBar = None
        if "mainJPanel" not in vars(self): self.mainJPanel: JPanel = None
        if "menuJMenuBar" not in vars(self): self.menuJMenuBar: JMenuBar = None
        if "newJMenuItem" not in vars(self): self.newJMenuItem: JMenuItem = None
        if "nextFrameJMenuItem" not in vars(self): self.nextFrameJMenuItem: JMenuItem = None
        if "objectJMenu" not in vars(self): self.objectJMenu: JMenu = None
        if "openJButton" not in vars(self): self.openJButton: JButton = None
        if "openJMenuItem" not in vars(self): self.openJMenuItem: JMenuItem = None
        if "playJButton" not in vars(self): self.playJButton: JButton = None
        if "previousFrameJMenuItem" not in vars(self): self.previousFrameJMenuItem: JMenuItem = None
        if "removeJMenuItem" not in vars(self): self.removeJMenuItem: JMenuItem = None
        if "saveAsJMenuItem" not in vars(self): self.saveAsJMenuItem: JMenuItem = None
        if "saveJButton" not in vars(self): self.saveJButton: JButton = None
        if "saveJMenuItem" not in vars(self): self.saveJMenuItem: JMenuItem = None
        if "statusJPanel" not in vars(self): self.statusJPanel: JPanel = None
        if "stopJjButton" not in vars(self): self.stopJjButton: JButton = None
        if "viewJMenu" not in vars(self): self.viewJMenu: JMenu = None
        if "zoomInJMenuItem" not in vars(self): self.zoomInJMenuItem: JMenuItem = None
        if "zoomOutJMenuItem" not in vars(self): self.zoomOutJMenuItem: JMenuItem = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.j2me.dialog.RotateJDialog import RotateJDialog
        from org.allbinary.gui.dialog.FileJDialog import FileJDialog
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        self.setSize(Dimension(550, 400))
        self.mainJPanel.setSize(Dimension(550, 400))
        self.jTabbedPane.setSize(Dimension(550, 400))
        self.fileJDialog = FileJDialog()
        self.fileJDialog.addFinishedListener(self)
        self.rotateJDialog = RotateJDialog(self, False)
    

    def initComponents(self) -> None:
        from org.allbinary.string.CommonLabels import CommonLabels
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
        _java_listener_owner = self
        class _JavaListenerN69289(WindowAdapter):
            
            

            def windowClosing(self, evt: WindowEvent) -> None:
                (self if hasattr(self, "exitForm") else _java_listener_owner).exitForm(evt)
        self.addWindowListener(_JavaListenerN69289()
            )
        self.jButton2.setText("New")
        _java_listener_owner = self
        class _JavaListenerN69428(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jButton2ActionPerformed") else _java_listener_owner).jButton2ActionPerformed(evt)
        self.jButton2.addActionListener(_JavaListenerN69428()
            )
        self.jToolBar1.add(self.jButton2)
        self.saveJButton.setText("Save")
        _java_listener_owner = self
        class _JavaListenerN69604(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "saveJButtonActionPerformed") else _java_listener_owner).saveJButtonActionPerformed(evt)
        self.saveJButton.addActionListener(_JavaListenerN69604()
            )
        self.jToolBar1.add(self.saveJButton)
        self.jButton1.setText("Export")
        _java_listener_owner = self
        class _JavaListenerN69780(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jButton1ActionPerformed") else _java_listener_owner).jButton1ActionPerformed(evt)
        self.jButton1.addActionListener(_JavaListenerN69780()
            )
        self.jToolBar1.add(self.jButton1)
        self.openJButton.setText("Open")
        _java_listener_owner = self
        class _JavaListenerN69956(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "openJButtonActionPerformed") else _java_listener_owner).openJButtonActionPerformed(evt)
        self.openJButton.addActionListener(_JavaListenerN69956()
            )
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
        _java_listener_owner = self
        class _JavaListenerN70467(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "playJButtonMousePressed") else _java_listener_owner).playJButtonMousePressed(evt)
        self.playJButton.addMouseListener(_JavaListenerN70467()
            )
        self.jToolBar1.add(self.playJButton)
        self.stopJjButton.setText("Stop")
        _java_listener_owner = self
        class _JavaListenerN70643(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "stopJjButtonMousePressed") else _java_listener_owner).stopJjButtonMousePressed(evt)
        self.stopJjButton.addMouseListener(_JavaListenerN70643()
            )
        self.jToolBar1.add(self.stopJjButton)
        self.getContentPane().add(self.jToolBar1, BorderLayout.NORTH)
        self.jPanel1.setLayout(GridLayout(1, 0))
        self.mainJPanel.setLayout(GridLayout(1, 0))
        self.jTabbedPane.setMinimumSize(Dimension(550, 400))
        _java_listener_owner = self
        class _JavaListenerN70986(ChangeListener):
            
            

            def stateChanged(self, evt: ChangeEvent) -> None:
                (self if hasattr(self, "jTabbedPaneStateChanged") else _java_listener_owner).jTabbedPaneStateChanged(evt)
        self.jTabbedPane.addChangeListener(_JavaListenerN70986()
            )
        self.mainJPanel.add(self.jTabbedPane)
        self.jPanel1.add(self.mainJPanel)
        self.getContentPane().add(self.jPanel1, BorderLayout.CENTER)
        self.statusJPanel.setLayout(GridLayout(1, 0))
        MyFrame.statusJLabel.setText("Status Bar")
        self.statusJPanel.add(MyFrame.statusJLabel)
        self.getContentPane().add(self.statusJPanel, BorderLayout.SOUTH)
        self.fileJMenu.setText("File")
        _java_listener_owner = self
        class _JavaListenerN71425(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "fileJMenuActionPerformed") else _java_listener_owner).fileJMenuActionPerformed(evt)
        self.fileJMenu.addActionListener(_JavaListenerN71425()
            )
        self.newJMenuItem.setText("New")
        _java_listener_owner = self
        class _JavaListenerN71564(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "newJMenuItemActionPerformed") else _java_listener_owner).newJMenuItemActionPerformed(evt)
        self.newJMenuItem.addActionListener(_JavaListenerN71564()
            )
        self.fileJMenu.add(self.newJMenuItem)
        self.openJMenuItem.setText("Open")
        _java_listener_owner = self
        class _JavaListenerN71740(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "openJMenuItemActionPerformed") else _java_listener_owner).openJMenuItemActionPerformed(evt)
        self.openJMenuItem.addActionListener(_JavaListenerN71740()
            )
        self.fileJMenu.add(self.openJMenuItem)
        self.saveJMenuItem.setText("Save")
        _java_listener_owner = self
        class _JavaListenerN71916(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "saveJMenuItemMousePressed") else _java_listener_owner).saveJMenuItemMousePressed(evt)
        self.saveJMenuItem.addMouseListener(_JavaListenerN71916()
            )
        self.fileJMenu.add(self.saveJMenuItem)
        self.saveAsJMenuItem.setText("SaveAs")
        self.fileJMenu.add(self.saveAsJMenuItem)
        self.exportJMenuItem1.setText("Export")
        _java_listener_owner = self
        class _JavaListenerN72159(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "exportJMenuItem1ActionPerformed") else _java_listener_owner).exportJMenuItem1ActionPerformed(evt)
        self.exportJMenuItem1.addActionListener(_JavaListenerN72159()
            )
        self.fileJMenu.add(self.exportJMenuItem1)
        self.exitJMenuItem.setText("Exit")
        _java_listener_owner = self
        class _JavaListenerN72335(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "exitJMenuItemActionPerformed") else _java_listener_owner).exitJMenuItemActionPerformed(evt)
        self.exitJMenuItem.addActionListener(_JavaListenerN72335()
            )
        self.fileJMenu.add(self.exitJMenuItem)
        self.menuJMenuBar.add(self.fileJMenu)
        self.viewJMenu.setText("View")
        self.zoomInJMenuItem.setText("Zoom In")
        _java_listener_owner = self
        class _JavaListenerN72578(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "zoomInJMenuItemMousePressed") else _java_listener_owner).zoomInJMenuItemMousePressed(evt)
        self.zoomInJMenuItem.addMouseListener(_JavaListenerN72578()
            )
        self.viewJMenu.add(self.zoomInJMenuItem)
        self.zoomOutJMenuItem.setText("Zoom Out")
        _java_listener_owner = self
        class _JavaListenerN72754(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "zoomOutJMenuItemMousePressed") else _java_listener_owner).zoomOutJMenuItemMousePressed(evt)
        self.zoomOutJMenuItem.addMouseListener(_JavaListenerN72754()
            )
        self.viewJMenu.add(self.zoomOutJMenuItem)
        self.menuJMenuBar.add(self.viewJMenu)
        self.objectJMenu.setText("Objects")
        self.explodeAllJMenuItem.setText("Explode All")
        _java_listener_owner = self
        class _JavaListenerN72997(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "explodeAllJMenuItemMousePressed") else _java_listener_owner).explodeAllJMenuItemMousePressed(evt)
        self.explodeAllJMenuItem.addMouseListener(_JavaListenerN72997()
            )
        self.objectJMenu.add(self.explodeAllJMenuItem)
        self.menuJMenuBar.add(self.objectJMenu)
        self.frameJMenu.setText("Frame")
        _java_listener_owner = self
        class _JavaListenerN73210(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "frameJMenuActionPerformed") else _java_listener_owner).frameJMenuActionPerformed(evt)
        self.frameJMenu.addActionListener(_JavaListenerN73210()
            )
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
        _java_listener_owner = self
        class _JavaListenerN73838(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "centerJMenuItemActionPerformed") else _java_listener_owner).centerJMenuItemActionPerformed(evt)
        self.centerJMenuItem.addActionListener(_JavaListenerN73838()
            )
        self.generateJMenu.add(self.centerJMenuItem)
        self.autoDamageJMenuItem.setText("Damage")
        self.generateJMenu.add(self.autoDamageJMenuItem)
        self.autoExplodeJMenuItem.setText("Explode")
        _java_listener_owner = self
        class _JavaListenerN74081(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "autoExplodeJMenuItemMousePressed") else _java_listener_owner).autoExplodeJMenuItemMousePressed(evt)
        self.autoExplodeJMenuItem.addMouseListener(_JavaListenerN74081()
            )
        self.generateJMenu.add(self.autoExplodeJMenuItem)
        self.autoGrowJMenuItem.setText("Grow")
        self.generateJMenu.add(self.autoGrowJMenuItem)
        self.jMenuItem1.setText("Mirror")
        _java_listener_owner = self
        class _JavaListenerN74324(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jMenuItem1ActionPerformed") else _java_listener_owner).jMenuItem1ActionPerformed(evt)
        self.jMenuItem1.addActionListener(_JavaListenerN74324()
            )
        self.generateJMenu.add(self.jMenuItem1)
        self.autoRotateGenerationJMenuItem.setText("Rotate")
        _java_listener_owner = self
        class _JavaListenerN74500(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "autoRotateGenerationJMenuItemMousePressed") else _java_listener_owner).autoRotateGenerationJMenuItemMousePressed(evt)
        self.autoRotateGenerationJMenuItem.addMouseListener(_JavaListenerN74500()
            )
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
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
        try:
            MyCanvasEventService.fire(MyCanvasEvent(MyCanvasEventSource(MyCanvasEventService.EXPLODE, None)))
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "explodeAllJMenuItemMousePressed", e)
    

    def autoExplodeJMenuItemMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
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
        __import__("java.lang.System", fromlist=["System"]).System.exit(0)
    

    def newJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        self.newGraphics()
    

    def fileJMenuActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def exitForm(self, evt: WindowEvent) -> None:
        __import__("java.lang.System", fromlist=["System"]).System.exit(0)
    

    def openJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.openGraphics()
    

    def jButton2ActionPerformed(self, evt: ActionEvent) -> None:
        self.newGraphics()
    

    def centerJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
        from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
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
        from java.io.File import File
        from org.allbinary.dom.DomHelper import DomHelper
        from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
        from org.w3c.dom.Document import Document
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
        from org.allbinary.graphics.j2me.dialog.NewWorkAreaJDialog import NewWorkAreaJDialog
        from org.allbinary.log.LOGGING import LOGGING
        try:
            newName: str = "graphic" + str(MyFrame.numberOfWorkAreas)
            dim: Dimension = self.getSize()
            newDialog: NewWorkAreaJDialog = NewWorkAreaJDialog(self, False, dim, newName)
        except Exception as e:
            if LOGGING.contains(LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "newJMenuItemActionPerformed", e)
    

    def openGraphics(self) -> None:
        from org.allbinary.log.LOGGING import LOGGING
        try:
            self.logUtil.putF("Starting", self, "openImageJMenuItemActionPerformed")
            self.fileJDialog.setVisible(True)
        except Exception as e:
            if LOGGING.contains(LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "open", e)
    

    def export(self) -> None:
        from java.io.File import File
        from org.allbinary.dom.DomHelper import DomHelper
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
        from org.allbinary.log.LOGGING import LOGGING
        from org.w3c.dom.Document import Document
        try:
            workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getSelectedComponent()
            file: File = File(MyFrame.SAVE_PATH + "/" + workAreaJPanel.getName() + self.JAVAEXTENSION)
            document: Document = workAreaJPanel.toDocument()
            self.logUtil.putF("Export: " + DomHelper.getInstance().toString(document), self, "exportJMenuItem1ActionPerformed")
            self.xslHelper.export(file, str(MyFrame.TEMPLATE_EXPORT_PATH) + "/" + self.JAVA_TEMPLATE, document)
        except Exception as e:
            if LOGGING.contains(LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "export", e)
    

    def save(self) -> None:
        from java.io.File import File
        from org.allbinary.dom.DomHelper import DomHelper
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
        from org.allbinary.log.LOGGING import LOGGING
        try:
            workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getSelectedComponent()
            DomHelper.getInstance().save(File(MyFrame.SAVE_PATH + "/" + workAreaJPanel.getName() + self.SAVEEXTENSION), workAreaJPanel.toDocument())
        except Exception as e:
            if LOGGING.contains(LOGGING.MENUEVENT):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, self.commonStrings.SAVE, e)
    

    # throws Exception
    def onHashMap(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        angleIncrementInteger: int = hashMap.get(str(0))
        totalRotationInteger: int = hashMap.get(str(1))
        self.getSelectedWorkArea().autoRotate(int(angleIncrementInteger), int(totalRotationInteger))
    

    def getSelectedWorkArea(self) -> WorkAreaJPanelInterface:
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
        return self.jTabbedPane.getSelectedComponent()
    

    def updateSelectedWorkArea(self) -> None:
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
        numberOfTabs: int = self.jTabbedPane.getTabCount()
        for index in range(0, numberOfTabs):
            workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getComponentAt(index)
            workAreaJPanel.deselect()
        workAreaJPanel: WorkAreaJPanelInterface = self.jTabbedPane.getSelectedComponent()
        if workAreaJPanel is not None:
            workAreaJPanel.select()
    

    # throws Exception
    def add(self, newCanvasInterface: WorkAreaJPanelInterface) -> None:
        from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
        from org.allbinary.log.LOGGING import LOGGING
        try:
            MyFrame.numberOfWorkAreas += 1
            if MyFrame.numberOfWorkAreas == MyFrame.MAXWORKAREAS:
                raise Exception()
            self.jTabbedPane.addTab(newCanvasInterface.getName(), newCanvasInterface)
            self.jTabbedPane.setSelectedComponent(newCanvasInterface)
            animationThread: JavaThread = JavaThread(target=newCanvasInterface.run)
            animationThread.start()
            self.updateSelectedWorkArea()
        except Exception as e:
            if LOGGING.contains(LOGGING.GRAPHICSCREATION):
                self.guiLog.put(self.commonStrings.EXCEPTION, self, "addNewCanvas", e)
    

    def keyPressed(self, keyEvent: KeyEvent) -> None:
        self.getSelectedWorkArea().keyPressed(keyEvent)
    

    def keyReleased(self, keyEvent: KeyEvent) -> None:
        pass
    

    def keyTyped(self, keyEvent: KeyEvent) -> None:
        pass
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
        from org.allbinary.math.AngleFactory import AngleFactory
        from org.allbinary.string.CommonStrings import CommonStrings
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
# from org.allbinary.data.tree.dom.XslHelper import XslHelper
# from org.allbinary.dom.DomHelper import DomHelper
# from org.allbinary.graphics.j2me.dialog.NewWorkAreaJDialog import NewWorkAreaJDialog
# from org.allbinary.graphics.j2me.dialog.RotateJDialog import RotateJDialog
# from org.allbinary.graphics.j2me.workarea.WorkAreaDom import WorkAreaDom
# from org.allbinary.graphics.j2me.workarea.WorkAreaJPanel import WorkAreaJPanel
# from org.allbinary.graphics.j2me.workarea.WorkAreaJPanelInterface import WorkAreaJPanelInterface
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEvent import MyCanvasEvent
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventService import MyCanvasEventService
# from org.allbinary.graphics.j2me.workarea.canvas.event.MyCanvasEventSource import MyCanvasEventSource
# from org.allbinary.gui.dialog.FileJDialog import FileJDialog
# from org.allbinary.log.LOGGING import LOGGING
# from org.allbinary.logic.communication.log.GuiLog import GuiLog
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from java.awt.BorderLayout import BorderLayout
# from java.awt.Dimension import Dimension
# from java.awt.GridLayout import GridLayout
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from java.awt.event.KeyEvent import KeyEvent
# from java.awt.event.MouseAdapter import MouseAdapter
# from java.awt.event.MouseEvent import MouseEvent
# from java.awt.event.WindowAdapter import WindowAdapter
# from java.awt.event.WindowEvent import WindowEvent
# from javax.swing.JButton import JButton
# from javax.swing.JLabel import JLabel
# from javax.swing.JMenu import JMenu
# from javax.swing.JMenuBar import JMenuBar
# from javax.swing.JMenuItem import JMenuItem
# from javax.swing.JPanel import JPanel
# from javax.swing.JTabbedPane import JTabbedPane
# from javax.swing.JToolBar import JToolBar
# from javax.swing.event.ChangeEvent import ChangeEvent
# from javax.swing.event.ChangeListener import ChangeListener


def _MyFrame_SAVE_PATH() -> object:
    return str(MyFrame.PATH) + "/save"

lazy_static(MyFrame, "SAVE_PATH", _MyFrame_SAVE_PATH)

def _MyFrame_TEMPLATE_EXPORT_PATH() -> object:
    return str(MyFrame.PATH) + "/templates/export"

lazy_static(MyFrame, "TEMPLATE_EXPORT_PATH", _MyFrame_TEMPLATE_EXPORT_PATH)

