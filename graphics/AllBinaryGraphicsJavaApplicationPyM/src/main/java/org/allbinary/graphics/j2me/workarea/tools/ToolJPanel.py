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
# package org.allbinary.graphics.j2me.workarea.tools

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class ToolJPanel(JPanel):
    def _java_defaults(self):
        vars(self).setdefault("arcJButton", None)
        vars(self).setdefault("charJButton", None)
        vars(self).setdefault("colorJList", None)
        vars(self).setdefault("colorJPanel", None)
        vars(self).setdefault("dottedArcJButton", None)
        vars(self).setdefault("dottedFillArcJButton", None)
        vars(self).setdefault("dottedFillRectJButton", None)
        vars(self).setdefault("dottedFillRountRectJButton", None)
        vars(self).setdefault("dottedLineJButton", None)
        vars(self).setdefault("dottedRectButton", None)
        vars(self).setdefault("fillArcJButton", None)
        vars(self).setdefault("fillRectJButton", None)
        vars(self).setdefault("fillRoundRectJButton", None)
        vars(self).setdefault("imageJButton", None)
        vars(self).setdefault("lineJButton", None)
        vars(self).setdefault("rectJButton", None)
        vars(self).setdefault("roundRectJButton", None)
        vars(self).setdefault("stringJButton", None)

    def _init_fields(self) -> None:
        if "arcJButton" not in vars(self): self.arcJButton: JButton = None
        if "charJButton" not in vars(self): self.charJButton: JButton = None
        if "colorJList" not in vars(self): self.colorJList: JList = None
        if "colorJPanel" not in vars(self): self.colorJPanel: JPanel = None
        if "dottedArcJButton" not in vars(self): self.dottedArcJButton: JButton = None
        if "dottedFillArcJButton" not in vars(self): self.dottedFillArcJButton: JButton = None
        if "dottedFillRectJButton" not in vars(self): self.dottedFillRectJButton: JButton = None
        if "dottedFillRountRectJButton" not in vars(self): self.dottedFillRountRectJButton: JButton = None
        if "dottedLineJButton" not in vars(self): self.dottedLineJButton: JButton = None
        if "dottedRectButton" not in vars(self): self.dottedRectButton: JButton = None
        if "fillArcJButton" not in vars(self): self.fillArcJButton: JButton = None
        if "fillRectJButton" not in vars(self): self.fillRectJButton: JButton = None
        if "fillRoundRectJButton" not in vars(self): self.fillRoundRectJButton: JButton = None
        if "imageJButton" not in vars(self): self.imageJButton: JButton = None
        if "lineJButton" not in vars(self): self.lineJButton: JButton = None
        if "rectJButton" not in vars(self): self.rectJButton: JButton = None
        if "roundRectJButton" not in vars(self): self.roundRectJButton: JButton = None
        if "stringJButton" not in vars(self): self.stringJButton: JButton = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        self.lineJButton = JButton()
        self.rectJButton = JButton()
        self.arcJButton = JButton()
        self.stringJButton = JButton()
        self.charJButton = JButton()
        self.roundRectJButton = JButton()
        self.imageJButton = JButton()
        self.fillArcJButton = JButton()
        self.fillRectJButton = JButton()
        self.fillRoundRectJButton = JButton()
        self.dottedLineJButton = JButton()
        self.dottedRectButton = JButton()
        self.dottedArcJButton = JButton()
        self.dottedFillRectJButton = JButton()
        self.dottedFillArcJButton = JButton()
        self.dottedFillRountRectJButton = JButton()
        self.colorJPanel = JPanel()
        self.colorJList = JList()
        self.setLayout(GridLayout(17, 1))
        self.lineJButton.setFont(Font("Dialog", 0, 10))
        self.lineJButton.setText(LinesGraphicItem.getStaticName())
        _java_listener_owner = self
        class _JavaListenerN66526(MouseAdapter):
            
            

            def mouseClicked(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "lineJButtonMouseClicked") else _java_listener_owner).lineJButtonMouseClicked(evt)
        self.lineJButton.addMouseListener(_JavaListenerN66526()
            )
        self.add(self.lineJButton)
        self.rectJButton.setFont(Font("Dialog", 0, 10))
        self.rectJButton.setText("Rect")
        _java_listener_owner = self
        class _JavaListenerN66744(MouseAdapter):
            
            

            def mouseClicked(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "rectJButtonMouseClicked") else _java_listener_owner).rectJButtonMouseClicked(evt)
        self.rectJButton.addMouseListener(_JavaListenerN66744()
            )
        self.add(self.rectJButton)
        self.arcJButton.setFont(Font("Dialog", 0, 10))
        self.arcJButton.setText("Arc")
        _java_listener_owner = self
        class _JavaListenerN66962(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "arcJButtonMousePressed") else _java_listener_owner).arcJButtonMousePressed(evt)
        self.arcJButton.addMouseListener(_JavaListenerN66962()
            )
        self.add(self.arcJButton)
        self.stringJButton.setFont(Font("Dialog", 0, 10))
        self.stringJButton.setText("String")
        _java_listener_owner = self
        class _JavaListenerN67180(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "stringJButtonMousePressed") else _java_listener_owner).stringJButtonMousePressed(evt)
        self.stringJButton.addMouseListener(_JavaListenerN67180()
            )
        self.add(self.stringJButton)
        self.charJButton.setFont(Font("Dialog", 0, 10))
        self.charJButton.setText("Char")
        _java_listener_owner = self
        class _JavaListenerN67398(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "charJButtonMousePressed") else _java_listener_owner).charJButtonMousePressed(evt)
        self.charJButton.addMouseListener(_JavaListenerN67398()
            )
        self.add(self.charJButton)
        self.roundRectJButton.setFont(Font("Dialog", 0, 10))
        self.roundRectJButton.setText("Round Rect")
        _java_listener_owner = self
        class _JavaListenerN67616(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "roundRectJButtonMousePressed") else _java_listener_owner).roundRectJButtonMousePressed(evt)
        self.roundRectJButton.addMouseListener(_JavaListenerN67616()
            )
        self.add(self.roundRectJButton)
        self.imageJButton.setFont(Font("Dialog", 0, 10))
        self.imageJButton.setText("Image")
        _java_listener_owner = self
        class _JavaListenerN67834(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "imageJButtonMousePressed") else _java_listener_owner).imageJButtonMousePressed(evt)
        self.imageJButton.addMouseListener(_JavaListenerN67834()
            )
        self.add(self.imageJButton)
        self.fillArcJButton.setFont(Font("Dialog", 0, 10))
        self.fillArcJButton.setText("Fill Arc")
        _java_listener_owner = self
        class _JavaListenerN68052(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "fillArcJButtonMousePressed") else _java_listener_owner).fillArcJButtonMousePressed(evt)
        self.fillArcJButton.addMouseListener(_JavaListenerN68052()
            )
        self.add(self.fillArcJButton)
        self.fillRectJButton.setFont(Font("Dialog", 0, 10))
        self.fillRectJButton.setText("Fill Rect")
        _java_listener_owner = self
        class _JavaListenerN68270(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "fillRectJButtonMousePressed") else _java_listener_owner).fillRectJButtonMousePressed(evt)
        self.fillRectJButton.addMouseListener(_JavaListenerN68270()
            )
        self.add(self.fillRectJButton)
        self.fillRoundRectJButton.setFont(Font("Dialog", 0, 10))
        self.fillRoundRectJButton.setText("Fill Rnd Rect")
        _java_listener_owner = self
        class _JavaListenerN68488(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "fillRoundRectJButtonMousePressed") else _java_listener_owner).fillRoundRectJButtonMousePressed(evt)
        self.fillRoundRectJButton.addMouseListener(_JavaListenerN68488()
            )
        self.add(self.fillRoundRectJButton)
        self.dottedLineJButton.setFont(Font("Dialog", 0, 10))
        self.dottedLineJButton.setText("Dot Line")
        _java_listener_owner = self
        class _JavaListenerN68706(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "dottedLineJButtonMousePressed") else _java_listener_owner).dottedLineJButtonMousePressed(evt)
        self.dottedLineJButton.addMouseListener(_JavaListenerN68706()
            )
        self.add(self.dottedLineJButton)
        self.dottedRectButton.setFont(Font("Dialog", 0, 10))
        self.dottedRectButton.setText("Dot Rect")
        _java_listener_owner = self
        class _JavaListenerN68924(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "dottedRectButtonMousePressed") else _java_listener_owner).dottedRectButtonMousePressed(evt)
        self.dottedRectButton.addMouseListener(_JavaListenerN68924()
            )
        self.add(self.dottedRectButton)
        self.dottedArcJButton.setFont(Font("Dialog", 0, 10))
        self.dottedArcJButton.setText("Dot Arc")
        _java_listener_owner = self
        class _JavaListenerN69142(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "dottedArcJButtonMousePressed") else _java_listener_owner).dottedArcJButtonMousePressed(evt)
        self.dottedArcJButton.addMouseListener(_JavaListenerN69142()
            )
        self.add(self.dottedArcJButton)
        self.dottedFillRectJButton.setFont(Font("Dialog", 0, 10))
        self.dottedFillRectJButton.setText("Dot Fill Rect")
        _java_listener_owner = self
        class _JavaListenerN69360(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "dottedFillRectJButtonMousePressed") else _java_listener_owner).dottedFillRectJButtonMousePressed(evt)
        self.dottedFillRectJButton.addMouseListener(_JavaListenerN69360()
            )
        self.add(self.dottedFillRectJButton)
        self.dottedFillArcJButton.setFont(Font("Dialog", 0, 10))
        self.dottedFillArcJButton.setText("Dot Fill Arc")
        _java_listener_owner = self
        class _JavaListenerN69578(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "dottedFillArcJButtonMousePressed") else _java_listener_owner).dottedFillArcJButtonMousePressed(evt)
        self.dottedFillArcJButton.addMouseListener(_JavaListenerN69578()
            )
        self.add(self.dottedFillArcJButton)
        self.dottedFillRountRectJButton.setFont(Font("Dialog", 0, 10))
        self.dottedFillRountRectJButton.setText("Dot Fill Rnd Rect")
        _java_listener_owner = self
        class _JavaListenerN69796(MouseAdapter):
            
            

            def mousePressed(self, evt: MouseEvent) -> None:
                (self if hasattr(self, "dottedFillRountRectJButtonMousePressed") else _java_listener_owner).dottedFillRountRectJButtonMousePressed(evt)
        self.dottedFillRountRectJButton.addMouseListener(_JavaListenerN69796()
            )
        self.add(self.dottedFillRountRectJButton)
        self.colorJPanel.setLayout(GridLayout(1, 1))
        self.colorJPanel.add(self.colorJList)
        self.add(self.colorJPanel)
    

    def dottedFillRountRectJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.dottedFillRountRectJButton.getText())
    

    def dottedFillArcJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.dottedFillArcJButton.getText())
    

    def dottedFillRectJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.dottedFillRectJButton.getText())
    

    def dottedArcJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.dottedArcJButton.getText())
    

    def dottedRectButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.dottedRectButton.getText())
    

    def dottedLineJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.dottedLineJButton.getText())
    

    def fillRoundRectJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.fillRoundRectJButton.getText())
    

    def fillRectJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.fillRectJButton.getText())
    

    def fillArcJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.fillArcJButton.getText())
    

    def imageJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.imageJButton.getText())
    

    def roundRectJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.roundRectJButton.getText())
    

    def charJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.charJButton.getText())
    

    def stringJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.stringJButton.getText())
    

    def arcJButtonMousePressed(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.arcJButton.getText())
    

    def rectJButtonMouseClicked(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.rectJButton.getText())
    

    def lineJButtonMouseClicked(self, evt: MouseEvent) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.ToolFactory import ToolFactory
        ToolFactory.getInstance().setSelectedTool(self.lineJButton.getText())
# from java.awt.Font import Font
# from java.awt.GridLayout import GridLayout
# from java.awt.event.MouseAdapter import MouseAdapter
# from java.awt.event.MouseEvent import MouseEvent
# from javax.swing.JButton import JButton
# from javax.swing.JList import JList


