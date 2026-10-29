# Generated Code Do Not Modify
# package org.apache.xmlrpc

from __future__ import annotations



class XmlRpcException(Exception):
    

    def __init__(self, code: int, message: str) -> None:
        super().__init__(message)


