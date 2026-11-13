# Generated Code Do Not Modify
# package javax.microedition.lcdui

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from javax.microedition.lcdui.CommandListener import CommandListener


class NullCommandListener(CommandListener):
    NULL_COMMAND_LISTENER: NullCommandListener = None
    

    def commandAction(self, c: Command, d: Displayable) -> None:
        pass


def _NullCommandListener_NULL_COMMAND_LISTENER() -> object:
    return NullCommandListener()

lazy_static(NullCommandListener, "NULL_COMMAND_LISTENER", _NullCommandListener_NULL_COMMAND_LISTENER)

