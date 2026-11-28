# Generated Code Do Not Modify
# package org.apache.xmlrpc

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads


@java_inherited_overloads
class XmlRpcException(Exception):
    

    def __init__(self, code: int, message: str) -> None:
        super().__init__(message)


