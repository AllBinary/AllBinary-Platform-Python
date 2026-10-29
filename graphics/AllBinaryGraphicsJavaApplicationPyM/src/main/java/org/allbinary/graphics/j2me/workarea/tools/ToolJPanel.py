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

from org.allbinary.graphics.j2me.workarea.tools.JPanel import JPanel


class ToolJPanel(JPanel):

    def _init_fields(self) -> None:
        self.arcJButton: JButton = None
        self.charJButton: JButton = None
        self.colorJList: JList = None
        self.colorJPanel: JPanel = None
        self.dottedArcJButton: JButton = None
        self.dottedFillArcJButton: JButton = None
        self.dottedFillRectJButton: JButton = None
        self.dottedFillRountRectJButton: JButton = None
        self.dottedLineJButton: JButton = None
        self.dottedRectButton: JButton = None
        self.fillArcJButton: JButton = None
        self.fillRectJButton: JButton = None
        self.fillRoundRectJButton: JButton = None
        self.imageJButton: JButton = None
        self.lineJButton: JButton = None
        self.rectJButton: JButton = None
        self.roundRectJButton: JButton = None
        self.stringJButton: JButton = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
    

    def initComponents(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JButton import JButton
        from org.allbinary.graphics.j2me.workarea.tools.JPanel import JPanel
        from org.allbinary.graphics.j2me.workarea.tools.JList import JList
        from org.allbinary.graphics.j2me.workarea.tools.GridLayout import GridLayout
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.Font import Font
        from org.allbinary.graphics.j2me.workarea.tools.MouseAdapter import MouseAdapter
        from org.allbinary.graphics.j2me.workarea.tools.GridLayout import GridLayout
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
        self.lineJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mouseClicked(self, evt: MouseEvent) -> None:
#                 self.lineJButtonMouseClicked(evt)
))
        self.add(self.lineJButton)
        self.rectJButton.setFont(Font("Dialog", 0, 10))
        self.rectJButton.setText("Rect")
        self.rectJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mouseClicked(self, evt: MouseEvent) -> None:
#                 self.rectJButtonMouseClicked(evt)
))
        self.add(self.rectJButton)
        self.arcJButton.setFont(Font("Dialog", 0, 10))
        self.arcJButton.setText("Arc")
        self.arcJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.arcJButtonMousePressed(evt)
))
        self.add(self.arcJButton)
        self.stringJButton.setFont(Font("Dialog", 0, 10))
        self.stringJButton.setText("String")
        self.stringJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.stringJButtonMousePressed(evt)
))
        self.add(self.stringJButton)
        self.charJButton.setFont(Font("Dialog", 0, 10))
        self.charJButton.setText("Char")
        self.charJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.charJButtonMousePressed(evt)
))
        self.add(self.charJButton)
        self.roundRectJButton.setFont(Font("Dialog", 0, 10))
        self.roundRectJButton.setText("Round Rect")
        self.roundRectJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.roundRectJButtonMousePressed(evt)
))
        self.add(self.roundRectJButton)
        self.imageJButton.setFont(Font("Dialog", 0, 10))
        self.imageJButton.setText("Image")
        self.imageJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.imageJButtonMousePressed(evt)
))
        self.add(self.imageJButton)
        self.fillArcJButton.setFont(Font("Dialog", 0, 10))
        self.fillArcJButton.setText("Fill Arc")
        self.fillArcJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.fillArcJButtonMousePressed(evt)
))
        self.add(self.fillArcJButton)
        self.fillRectJButton.setFont(Font("Dialog", 0, 10))
        self.fillRectJButton.setText("Fill Rect")
        self.fillRectJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.fillRectJButtonMousePressed(evt)
))
        self.add(self.fillRectJButton)
        self.fillRoundRectJButton.setFont(Font("Dialog", 0, 10))
        self.fillRoundRectJButton.setText("Fill Rnd Rect")
        self.fillRoundRectJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.fillRoundRectJButtonMousePressed(evt)
))
        self.add(self.fillRoundRectJButton)
        self.dottedLineJButton.setFont(Font("Dialog", 0, 10))
        self.dottedLineJButton.setText("Dot Line")
        self.dottedLineJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.dottedLineJButtonMousePressed(evt)
))
        self.add(self.dottedLineJButton)
        self.dottedRectButton.setFont(Font("Dialog", 0, 10))
        self.dottedRectButton.setText("Dot Rect")
        self.dottedRectButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.dottedRectButtonMousePressed(evt)
))
        self.add(self.dottedRectButton)
        self.dottedArcJButton.setFont(Font("Dialog", 0, 10))
        self.dottedArcJButton.setText("Dot Arc")
        self.dottedArcJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.dottedArcJButtonMousePressed(evt)
))
        self.add(self.dottedArcJButton)
        self.dottedFillRectJButton.setFont(Font("Dialog", 0, 10))
        self.dottedFillRectJButton.setText("Dot Fill Rect")
        self.dottedFillRectJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.dottedFillRectJButtonMousePressed(evt)
))
        self.add(self.dottedFillRectJButton)
        self.dottedFillArcJButton.setFont(Font("Dialog", 0, 10))
        self.dottedFillArcJButton.setText("Dot Fill Arc")
        self.dottedFillArcJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.dottedFillArcJButtonMousePressed(evt)
))
        self.add(self.dottedFillArcJButton)
        self.dottedFillRountRectJButton.setFont(Font("Dialog", 0, 10))
        self.dottedFillRountRectJButton.setText("Dot Fill Rnd Rect")
        self.dottedFillRountRectJButton.addMouseListener((MouseAdapter()  # Java anonymous class body:
#             
# 
#             def mousePressed(self, evt: MouseEvent) -> None:
#                 self.dottedFillRountRectJButtonMousePressed(evt)
))
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


