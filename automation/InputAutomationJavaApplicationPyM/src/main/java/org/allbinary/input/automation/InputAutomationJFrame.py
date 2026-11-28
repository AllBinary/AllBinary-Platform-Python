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
# package org.allbinary.input.automation

from __future__ import annotations

from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import java_bases
# from javax.help.event.HelpSetListener import HelpSetListener
from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
from bundle.input.automation.robot.InputAutomationRobotChangeListener import InputAutomationRobotChangeListener
# from javax.swing.JFrame import JFrame


@java_inherited_overloads
class InputAutomationJFrame(*java_bases(JFrame, InputAutomationConfigurationModuleChangeListener, InputAutomationRobotChangeListener, HelpSetListener)):
    INPUTAUTOMATION_JFRAME: InputAutomationJFrame = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("inputAutomationModuleConfigurations", None)
        vars(self).setdefault("inputAutomationModuleFactory", None)
        vars(self).setdefault("inputAutomationModuleInterface", None)
        vars(self).setdefault("runnableInterface", None)
        vars(self).setdefault("thread", None)
        vars(self).setdefault("helpSet", None)
        vars(self).setdefault("uri", None)
        vars(self).setdefault("aboutJMenuItem", None)
        vars(self).setdefault("automationModuleConfigurationJPanel", None)
        vars(self).setdefault("gameRobotJTabbedPane", None)
        vars(self).setdefault("helpJMenuItem", None)
        vars(self).setdefault("inputAutomationModuleJList", None)
        vars(self).setdefault("inputAutomationModuleJPanel", None)
        vars(self).setdefault("jScrollPane1", None)
        vars(self).setdefault("mainJMenuBar", None)
        vars(self).setdefault("modulesJMenuItem", None)
        vars(self).setdefault("noModuleSelectedJDialog", None)
        vars(self).setdefault("noModuleSelectedJLabel", None)
        vars(self).setdefault("optionsJMenu", None)
        vars(self).setdefault("processingJMenu", None)
        vars(self).setdefault("startJMenuItem", None)
        vars(self).setdefault("stopJMenuItem", None)
        vars(self).setdefault("stopOnFocusJCheckBoxMenuItem", None)
        vars(self).setdefault("subscriptionJMenuItem", None)
        vars(self).setdefault("toolsJMenu", None)
        vars(self).setdefault("updatesJMenuItem", None)

    def _init_fields(self) -> None:
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfigurations import InputAutomationModuleConfigurations
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.inputAutomationModuleConfigurations: InputAutomationModuleConfigurations = InputAutomationModuleConfigurations()
        if "inputAutomationModuleFactory" not in vars(self): self.inputAutomationModuleFactory: InputAutomationModuleFactoryFactory = None
        if "inputAutomationModuleInterface" not in vars(self): self.inputAutomationModuleInterface: InputAutomationModuleFactoryInterface = None
        if "runnableInterface" not in vars(self): self.runnableInterface: RunnableInterface = None
        if "thread" not in vars(self): self.thread: JavaThread = None
        if "helpSet" not in vars(self): self.helpSet: HelpSet = None
        self.uri: URI = URI("http://geocities.com/allbinary/")
        if "aboutJMenuItem" not in vars(self): self.aboutJMenuItem: JMenuItem = None
        if "automationModuleConfigurationJPanel" not in vars(self): self.automationModuleConfigurationJPanel: JPanel = None
        if "gameRobotJTabbedPane" not in vars(self): self.gameRobotJTabbedPane: JTabbedPane = None
        if "helpJMenuItem" not in vars(self): self.helpJMenuItem: JMenuItem = None
        if "inputAutomationModuleJList" not in vars(self): self.inputAutomationModuleJList: JList = None
        if "inputAutomationModuleJPanel" not in vars(self): self.inputAutomationModuleJPanel: JPanel = None
        if "jScrollPane1" not in vars(self): self.jScrollPane1: JScrollPane = None
        if "mainJMenuBar" not in vars(self): self.mainJMenuBar: JMenuBar = None
        if "modulesJMenuItem" not in vars(self): self.modulesJMenuItem: JMenuItem = None
        if "noModuleSelectedJDialog" not in vars(self): self.noModuleSelectedJDialog: JDialog = None
        if "noModuleSelectedJLabel" not in vars(self): self.noModuleSelectedJLabel: JLabel = None
        if "optionsJMenu" not in vars(self): self.optionsJMenu: JMenu = None
        if "processingJMenu" not in vars(self): self.processingJMenu: JMenu = None
        if "startJMenuItem" not in vars(self): self.startJMenuItem: JMenuItem = None
        if "stopJMenuItem" not in vars(self): self.stopJMenuItem: JMenuItem = None
        if "stopOnFocusJCheckBoxMenuItem" not in vars(self): self.stopOnFocusJCheckBoxMenuItem: JCheckBoxMenuItem = None
        if "subscriptionJMenuItem" not in vars(self): self.subscriptionJMenuItem: JMenuItem = None
        if "toolsJMenu" not in vars(self): self.toolsJMenu: JMenu = None
        if "updatesJMenuItem" not in vars(self): self.updatesJMenuItem: JMenuItem = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from java.net.URL import URL
        from org.allbinary.logic.java.help.JavaHelpUtil import JavaHelpUtil
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        url: URL = __import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.classResource(type(self), "/help/Help.hs", False)
        self.logUtil.putF("URL: " + str(url), self, self.commonStrings.CONSTRUCTOR)
        self.helpSet = JavaHelpUtil.getInstance().getHelpSet(url)
        url = __import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.classResource(type(self), "/resources/allbinaryicon8bit.jpg", False)
        imageIcon: ImageIcon = ImageIcon(url)
        self.setIconImage(imageIcon.getImage())
        self.init()
    

    def helpSetAdded(self, helpSetEvent: HelpSetEvent) -> None:
        self.helpSet.add(helpSetEvent.getHelpSet())
    

    def helpSetRemoved(self, helpSetEvent: HelpSetEvent) -> None:
        self.helpSet.remove(helpSetEvent.getHelpSet())
    

    # throws Exception
    def init(self) -> None:
        from java.util.List import List
        from org.allbinary.gui.swing.workers.JListSwingWorker import JListSwingWorker
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationFactory import InputAutomationConfigurationFactory
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryFactory import InputAutomationModuleFactoryFactory
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfigurations import InputAutomationModuleConfigurations
        from org.allbinary.logic.system.security.licensing.InputAutomationClientInformationFactory import InputAutomationClientInformationFactory
        inputAutomationConfigurationFactory: InputAutomationConfigurationFactory = InputAutomationConfigurationFactory.getInstance()
        inputAutomationConfigurationFactory.init(InputAutomationClientInformationFactory.getInstance())
        inputAutomationModuleConfigurationList: List[InputAutomationModuleConfiguration] = inputAutomationConfigurationFactory.inputAutomationConfiguration.getInputAutomationModuleConfigurationList()
        if inputAutomationModuleConfigurationList is None:
            pass
        else:
            self.inputAutomationModuleConfigurations = InputAutomationModuleConfigurations(inputAutomationModuleConfigurationList)
        self.inputAutomationModuleFactory = InputAutomationModuleFactoryFactory(self.inputAutomationModuleConfigurations, self)
        (JListSwingWorker(self.inputAutomationModuleJList, self.inputAutomationModuleFactory.getListModel())).execute()
        self.gameRobotJTabbedPane.setEnabledAt(1, False)
        self.gameRobotJTabbedPane.setSelectedIndex(0)
    

    def initComponents(self) -> None:
        self.noModuleSelectedJDialog = JDialog()
        self.noModuleSelectedJLabel = JLabel()
        self.gameRobotJTabbedPane = JTabbedPane()
        self.inputAutomationModuleJPanel = JPanel()
        self.jScrollPane1 = JScrollPane()
        self.inputAutomationModuleJList = JList()
        self.automationModuleConfigurationJPanel = JPanel()
        self.mainJMenuBar = JMenuBar()
        self.processingJMenu = JMenu()
        self.startJMenuItem = JMenuItem()
        self.stopJMenuItem = JMenuItem()
        self.optionsJMenu = JMenu()
        self.stopOnFocusJCheckBoxMenuItem = JCheckBoxMenuItem()
        self.toolsJMenu = JMenu()
        self.helpJMenuItem = JMenuItem()
        self.updatesJMenuItem = JMenuItem()
        self.subscriptionJMenuItem = JMenuItem()
        self.modulesJMenuItem = JMenuItem()
        self.aboutJMenuItem = JMenuItem()
        self.noModuleSelectedJDialog.setMinimumSize(Dimension(200, 100))
        self.noModuleSelectedJLabel.setText("Please Select A Module")
        noModuleSelectedJDialogLayout: GroupLayout = GroupLayout(self.noModuleSelectedJDialog.getContentPane())
        self.noModuleSelectedJDialog.getContentPane().setLayout(noModuleSelectedJDialogLayout)
        noModuleSelectedJDialogLayout.setHorizontalGroup(noModuleSelectedJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(noModuleSelectedJDialogLayout.createSequentialGroup().addContainerGap().addComponent(self.noModuleSelectedJLabel).addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        noModuleSelectedJDialogLayout.setVerticalGroup(noModuleSelectedJDialogLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.noModuleSelectedJLabel, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 48, Short.MAX_VALUE))
        self.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        self.setMinimumSize(Dimension(325, 215))
        self.setResizable(False)
        _java_listener_owner = self
        class _JavaListenerN69680(WindowFocusListener):
            
            

            def windowGainedFocus(self, evt: WindowEvent) -> None:
                (self if hasattr(self, "formWindowGainedFocus") else _java_listener_owner).formWindowGainedFocus(evt)
            

            def windowLostFocus(self, evt: WindowEvent) -> None:
                (self if hasattr(self, "formWindowLostFocus") else _java_listener_owner).formWindowLostFocus(evt)
        self.addWindowFocusListener(_JavaListenerN69680()
            )
        _java_listener_owner = self
        class _JavaListenerN69846(FocusAdapter):
            
            

            def focusGained(self, evt: FocusEvent) -> None:
                (self if hasattr(self, "formFocusGained") else _java_listener_owner).formFocusGained(evt)
            

            def focusLost(self, evt: FocusEvent) -> None:
                (self if hasattr(self, "formFocusLost") else _java_listener_owner).formFocusLost(evt)
        self.addFocusListener(_JavaListenerN69846()
            )
        self.gameRobotJTabbedPane.setMinimumSize(Dimension(320, 200))
        self.inputAutomationModuleJList.setMinimumSize(Dimension(200, 0))
        _java_listener_owner = self
        class _JavaListenerN70121(ListSelectionListener):
            
            

            def valueChanged(self, evt: ListSelectionEvent) -> None:
                (self if hasattr(self, "inputAutomationModuleJListValueChanged") else _java_listener_owner).inputAutomationModuleJListValueChanged(evt)
        self.inputAutomationModuleJList.addListSelectionListener(_JavaListenerN70121()
            )
        self.jScrollPane1.setViewportView(self.inputAutomationModuleJList)
        inputAutomationModuleJPanelLayout: GroupLayout = GroupLayout(self.inputAutomationModuleJPanel)
        self.inputAutomationModuleJPanel.setLayout(inputAutomationModuleJPanelLayout)
        inputAutomationModuleJPanelLayout.setHorizontalGroup(inputAutomationModuleJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(inputAutomationModuleJPanelLayout.createSequentialGroup().addComponent(self.jScrollPane1, GroupLayout.PREFERRED_SIZE, 199, GroupLayout.PREFERRED_SIZE).addContainerGap(367, Short.MAX_VALUE)))
        inputAutomationModuleJPanelLayout.setVerticalGroup(inputAutomationModuleJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(inputAutomationModuleJPanelLayout.createSequentialGroup().addComponent(self.jScrollPane1, GroupLayout.PREFERRED_SIZE, 330, GroupLayout.PREFERRED_SIZE).addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        self.gameRobotJTabbedPane.addTab("Modules", self.inputAutomationModuleJPanel)
        automationModuleConfigurationJPanelLayout: GroupLayout = GroupLayout(self.automationModuleConfigurationJPanel)
        self.automationModuleConfigurationJPanel.setLayout(automationModuleConfigurationJPanelLayout)
        automationModuleConfigurationJPanelLayout.setHorizontalGroup(automationModuleConfigurationJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 566, Short.MAX_VALUE))
        automationModuleConfigurationJPanelLayout.setVerticalGroup(automationModuleConfigurationJPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 334, Short.MAX_VALUE))
        self.gameRobotJTabbedPane.addTab("Configuration", self.automationModuleConfigurationJPanel)
        self.processingJMenu.setText("Processing")
        self.processingJMenu.setToolTipText("Set module processing state")
        self.startJMenuItem.setText(self.commonStrings.START)
        _java_listener_owner = self
        class _JavaListenerN71194(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "startJMenuItemActionPerformed") else _java_listener_owner).startJMenuItemActionPerformed(evt)
        self.startJMenuItem.addActionListener(_JavaListenerN71194()
            )
        self.processingJMenu.add(self.startJMenuItem)
        self.stopJMenuItem.setText("Stop")
        _java_listener_owner = self
        class _JavaListenerN71370(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "stopJMenuItemActionPerformed") else _java_listener_owner).stopJMenuItemActionPerformed(evt)
        self.stopJMenuItem.addActionListener(_JavaListenerN71370()
            )
        self.processingJMenu.add(self.stopJMenuItem)
        self.mainJMenuBar.add(self.processingJMenu)
        self.optionsJMenu.setText("Options")
        _java_listener_owner = self
        class _JavaListenerN71583(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "optionsJMenuActionPerformed") else _java_listener_owner).optionsJMenuActionPerformed(evt)
        self.optionsJMenu.addActionListener(_JavaListenerN71583()
            )
        self.stopOnFocusJCheckBoxMenuItem.setSelected(True)
        self.stopOnFocusJCheckBoxMenuItem.setEnabled(False)
        self.stopOnFocusJCheckBoxMenuItem.setLabel("Stop Module On Focus")
        _java_listener_owner = self
        class _JavaListenerN71782(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "stopOnFocusJCheckBoxMenuItemActionPerformed") else _java_listener_owner).stopOnFocusJCheckBoxMenuItemActionPerformed(evt)
        self.stopOnFocusJCheckBoxMenuItem.addActionListener(_JavaListenerN71782()
            )
        self.optionsJMenu.add(self.stopOnFocusJCheckBoxMenuItem)
        self.mainJMenuBar.add(self.optionsJMenu)
        self.toolsJMenu.setText("Help")
        self.helpJMenuItem.setText("Help")
        _java_listener_owner = self
        class _JavaListenerN72025(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "helpJMenuItemActionPerformed") else _java_listener_owner).helpJMenuItemActionPerformed(evt)
        self.helpJMenuItem.addActionListener(_JavaListenerN72025()
            )
        self.toolsJMenu.add(self.helpJMenuItem)
        self.updatesJMenuItem.setText("Updates")
        _java_listener_owner = self
        class _JavaListenerN72201(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "updatesJMenuItemActionPerformed") else _java_listener_owner).updatesJMenuItemActionPerformed(evt)
        self.updatesJMenuItem.addActionListener(_JavaListenerN72201()
            )
        self.toolsJMenu.add(self.updatesJMenuItem)
        self.subscriptionJMenuItem.setText("Subscription")
        _java_listener_owner = self
        class _JavaListenerN72377(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "subscriptionJMenuItemActionPerformed") else _java_listener_owner).subscriptionJMenuItemActionPerformed(evt)
        self.subscriptionJMenuItem.addActionListener(_JavaListenerN72377()
            )
        self.toolsJMenu.add(self.subscriptionJMenuItem)
        self.modulesJMenuItem.setText("Module Manager")
        _java_listener_owner = self
        class _JavaListenerN72553(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "modulesJMenuItemActionPerformed") else _java_listener_owner).modulesJMenuItemActionPerformed(evt)
        self.modulesJMenuItem.addActionListener(_JavaListenerN72553()
            )
        self.toolsJMenu.add(self.modulesJMenuItem)
        self.aboutJMenuItem.setText("About")
        _java_listener_owner = self
        class _JavaListenerN72729(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "aboutJMenuItemActionPerformed") else _java_listener_owner).aboutJMenuItemActionPerformed(evt)
        self.aboutJMenuItem.addActionListener(_JavaListenerN72729()
            )
        self.toolsJMenu.add(self.aboutJMenuItem)
        self.mainJMenuBar.add(self.toolsJMenu)
        self.setJMenuBar(self.mainJMenuBar)
        layout: GroupLayout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.gameRobotJTabbedPane, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 571, Short.MAX_VALUE))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.gameRobotJTabbedPane, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 359, Short.MAX_VALUE))
        self.pack()
    

    def subscriptionJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        try:
            Desktop.getDesktop().browse(self.uri)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "subscriptionJMenuItemActionPerformed", e)
    

    def updatesJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        try:
            Desktop.getDesktop().browse(self.uri)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "updatesJMenuItemActionPerformed", e)
    

    def aboutJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.gui.dialog.BasicTextJDialog import BasicTextJDialog
        textJDialog: JDialog = BasicTextJDialog("Copyright (c) 2002-2007 AllBinary")
        textJDialog.setVisible(True)
        textJDialog.setLocationRelativeTo(self)
    

    def modulesJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.input.automation.osgi.DesktopBundle import DesktopBundle
        try:
            DesktopBundle().start()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "modulesJMenuItemActionPerformed", e)
    

    def helpJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.logic.java.help.JavaHelpUtil import JavaHelpUtil
        JavaHelpUtil.getInstance().show(self.helpSet)
    

    def stopOnFocusJCheckBoxMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def optionsJMenuActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def formWindowLostFocus(self, evt: WindowEvent) -> None:
        self.logUtil.putF("Nothing", self, "focusLost")
    

    def formWindowGainedFocus(self, evt: WindowEvent) -> None:
        if java_predicate(self.stopOnFocusJCheckBoxMenuItem, "isSelected"):
            self.logUtil.putF("Stopping", self, "focusGained")
            if self.runnableInterface is not None:
                self.runnableInterface.setRunning(False)
    

    def formFocusLost(self, evt: FocusEvent) -> None:
        pass
    

    def formFocusGained(self, evt: FocusEvent) -> None:
        pass
    

    def inputAutomationModuleJListValueChanged(self, evt: ListSelectionEvent) -> None:
        try:
            gameAutomationRobotModuleNameString: str = self.inputAutomationModuleJList.getSelectedValue()
            if gameAutomationRobotModuleNameString is not None:
                self.inputAutomationModuleInterface = self.inputAutomationModuleFactory.getInstance(gameAutomationRobotModuleNameString)
                self.getAutomationModuleConfigurationJPanel().removeAll()
                layout: GroupLayout = self.getAutomationModuleConfigurationJPanel().getLayout()
                layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 395, Short.MAX_VALUE).addComponent(self.inputAutomationModuleInterface.getConfigurationJPanel(), GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGap(0, 256, Short.MAX_VALUE).addComponent(self.inputAutomationModuleInterface.getConfigurationJPanel(), GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                self.gameRobotJTabbedPane.setEnabledAt(1, True)
                self.logUtil.putF("Setting Module: " + gameAutomationRobotModuleNameString + " and Configuration JPanel", self, "gameAutomationRobotModuleJListValueChanged")
            else:
                self.logUtil.putF("Module name was null", self, "gameAutomationRobotModuleJListValueChanged")
                self.gameRobotJTabbedPane.setEnabledAt(1, False)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "gameAutomationRobotModuleJListValueChanged", e)
    

    def stopJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        if self.runnableInterface is not None:
            self.runnableInterface.setRunning(False)
        else:
            self.noModuleSelectedJDialog.setVisible(True)
            self.noModuleSelectedJDialog.setLocationRelativeTo(self)
    

    def startJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.logUtil.putF("Starting", self, "startJMenuItemActionPerformed")
            if self.inputAutomationModuleInterface is not None:
                self.runnableInterface = self.inputAutomationModuleInterface.getInstance()
                if self.runnableInterface is not None:
                    self.thread = JavaThread(target=self.runnableInterface.run)
                    self.thread.setPriority(1 + 1)
                    self.thread.start()
                else:
                    self.logUtil.putF("Runnnable was null", self, "startJMenuItemActionPerformed")
                    self.noModuleSelectedJDialog.setVisible(True)
                    self.noModuleSelectedJDialog.setLocationRelativeTo(self)
            else:
                self.logUtil.putF("InputAutomationModuleInterface was null", self, "startJMenuItemActionPerformed")
                self.noModuleSelectedJDialog.setVisible(True)
                self.noModuleSelectedJDialog.setLocationRelativeTo(self)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "startJMenuItemActionPerformed", e)
    

    @staticmethod
    def getInstance() -> InputAutomationJFrame:
        return InputAutomationJFrame.INPUTAUTOMATION_JFRAME
    

    @staticmethod
    def destroy() -> None:
        InputAutomationJFrame.INPUTAUTOMATION_JFRAME.setVisible(False)
    

    @staticmethod
    def create(inputAutomationBundleActivatorListenerInterface: InputAutomationBundleActivatorListenerInterface) -> None:
        from org.allbinary.thread.ARunnable import ARunnable
        from bundle.input.automation.InputAutomationBundleActivatorListenerInterface import InputAutomationBundleActivatorListenerInterface
        from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo
        from org.allbinary.string.CommonStrings import CommonStrings
        LogConfigTypeFactory.getInstance()
        appUrlGlobals: AppUrlGlobals = AppUrlGlobals()
        appUrlGlobals.setWebappPath("G:/mnt/bc/mydev/work_automation/automation/run/")
        URLGLOBALS.init(appUrlGlobals)
        WebappClassLoaderInfo.setLoader(__import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.getSystemClassLoader())
        class _JavaListenerN76836(ARunnable):
            
            

            def run(self) -> None:
                from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.string.CommonStrings import CommonStrings
                logUtil: LogUtil = LogUtil.getInstance()
                commonStrings: CommonStrings = CommonStrings.getInstance()
                try:
                    logUtil.putF("Running", self, commonStrings.RUN)
                    InputAutomationJFrame.INPUTAUTOMATION_JFRAME = InputAutomationJFrame()
                    InputRobotFactory.getInstance().addListener(InputAutomationJFrame.getInstance())
                    if inputAutomationBundleActivatorListenerInterface is not None:
                        inputAutomationBundleActivatorListenerInterface.registerAsService()
                        inputAutomationBundleActivatorListenerInterface.useServices()
                    InputAutomationJFrame.INPUTAUTOMATION_JFRAME.setVisible(True)
                except Exception as e:
                    logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
        EventQueue.invokeLater(_JavaListenerN76836()
            )
    

    # throws Exception
    @staticmethod
    def main(args: list[str]) -> None:
        InputAutomationJFrame.create(None)
    

    def getAutomationModuleConfigurationJPanel(self) -> JPanel:
        return self.automationModuleConfigurationJPanel
    

    def setAutomationModuleConfigurationJPanel(self, automationModuleConfigurationJPanel: JPanel) -> None:
        self.automationModuleConfigurationJPanel = automationModuleConfigurationJPanel
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def onAdd_j1_1(self, inputAutomationRobotChangeEvent: InputAutomationRobotChangeEvent) -> None:
        from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotChangeEvent import InputAutomationRobotChangeEvent
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onAdd")
            InputRobotFactory.getInstance().add(inputAutomationRobotChangeEvent.getInputAutomationRobotInterfaceWrapper().getInputRobotInterface())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onAdd", e)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def onRemove_j1_1(self, inputAutomationRobotChangeEvent: InputAutomationRobotChangeEvent) -> None:
        from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotChangeEvent import InputAutomationRobotChangeEvent
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onRemove")
            InputRobotFactory.getInstance().add(inputAutomationRobotChangeEvent.getInputAutomationRobotInterfaceWrapper().getInputRobotInterface())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onRemove", e)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def onAdd_j1_2(self, inputAutomationConfigurationChangeEvent: InputAutomationConfigurationModuleChangeEvent) -> None:
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onAdd")
            self.inputAutomationModuleConfigurations.add(inputAutomationConfigurationChangeEvent.getInputAutomationModuleConfiguration())
            self.init()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onAdd", e)

    def onAdd(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "InputAutomationRobotChangeEvent" for base in type(args[0]).__mro__)):
            return __class__.__dict__["onAdd_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["onAdd_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("onAdd_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().onAdd(*args)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def onRemove_j1_2(self, inputAutomationConfigurationChangeEvent: InputAutomationConfigurationModuleChangeEvent) -> None:
        from java.util.List import List
        from org.allbinary.input.automation.configuration.InputAutomationConfiguration import InputAutomationConfiguration
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationFactory import InputAutomationConfigurationFactory
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
        from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfigurations import InputAutomationModuleConfigurations
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onRemove")
            inputAutomationConfiguration: InputAutomationConfiguration = InputAutomationConfigurationFactory.getInstance().inputAutomationConfiguration
            inputAutomationModuleConfigurationList: List[InputAutomationModuleConfiguration] = inputAutomationConfiguration.getInputAutomationModuleConfigurationList()
            if inputAutomationModuleConfigurationList is None:
                logUtil: LogUtil = LogUtil.getInstance()
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.putF("inputAutomationModuleConfigurationList: " + str(inputAutomationModuleConfigurationList), self, commonStrings.INIT)
                raise Exception()
            inputAutomationModuleConfigurations: InputAutomationModuleConfigurations = InputAutomationModuleConfigurations(inputAutomationConfiguration.getInputAutomationModuleConfigurationList())
            inputAutomationModuleConfigurations.remove(inputAutomationConfigurationChangeEvent.getInputAutomationModuleConfiguration())
            self.init()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onRemove", e)

    def onRemove(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "InputAutomationRobotChangeEvent" for base in type(args[0]).__mro__)):
            return __class__.__dict__["onRemove_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["onRemove_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("onRemove_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().onRemove(*args)
# from org.allbinary.thread.ARunnable import ARunnable
# from java.net.URI import URI
# from java.net.URL import URL
# from java.awt.Desktop import Desktop
# from java.util.List import List
# from javax.swing.ImageIcon import ImageIcon
# from javax.swing.JDialog import JDialog
# from javax.help.HelpSet import HelpSet
# from javax.help.event.HelpSetEvent import HelpSetEvent
# from bundle.input.automation.InputAutomationBundleActivatorListenerInterface import InputAutomationBundleActivatorListenerInterface
# from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.gui.dialog.BasicTextJDialog import BasicTextJDialog
# from org.allbinary.gui.swing.workers.JListSwingWorker import JListSwingWorker
# from org.allbinary.input.automation.configuration.InputAutomationConfiguration import InputAutomationConfiguration
# from org.allbinary.input.automation.configuration.InputAutomationConfigurationFactory import InputAutomationConfigurationFactory
# from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
# from org.allbinary.input.automation.module.InputAutomationModuleFactoryFactory import InputAutomationModuleFactoryFactory
# from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
# from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
# from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfigurations import InputAutomationModuleConfigurations
# from org.allbinary.input.automation.osgi.DesktopBundle import DesktopBundle
# from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
# from org.allbinary.input.automation.robot.osgi.InputAutomationRobotChangeEvent import InputAutomationRobotChangeEvent
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.java.help.JavaHelpUtil import JavaHelpUtil
# from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo
# from org.allbinary.logic.system.security.licensing.InputAutomationClientInformationFactory import InputAutomationClientInformationFactory
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.thread.RunnableInterface import RunnableInterface
# from java.awt.Dimension import Dimension
# from java.awt.EventQueue import EventQueue
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from java.awt.event.FocusAdapter import FocusAdapter
# from java.awt.event.FocusEvent import FocusEvent
# from java.awt.event.WindowEvent import WindowEvent
# from java.awt.event.WindowFocusListener import WindowFocusListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JCheckBoxMenuItem import JCheckBoxMenuItem
# from javax.swing.JLabel import JLabel
# from javax.swing.JList import JList
# from javax.swing.JMenu import JMenu
# from javax.swing.JMenuBar import JMenuBar
# from javax.swing.JMenuItem import JMenuItem
# from javax.swing.JPanel import JPanel
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.JTabbedPane import JTabbedPane
# from javax.swing.WindowConstants import WindowConstants
# from javax.swing.event.ListSelectionEvent import ListSelectionEvent
# from javax.swing.event.ListSelectionListener import ListSelectionListener


