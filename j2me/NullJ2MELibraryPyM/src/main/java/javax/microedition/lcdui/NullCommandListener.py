# Generated Code Do Not Modify
# package javax.microedition.lcdui

from __future__ import annotations

from javax.microedition.lcdui.CommandListener import CommandListener


class NullCommandListener(CommandListener):
    NULL_COMMAND_LISTENER: NullCommandListener = None
    

    def commandAction(self, c: Command, d: Displayable) -> None:
        pass


NullCommandListener.NULL_COMMAND_LISTENER = NullCommandListener()

