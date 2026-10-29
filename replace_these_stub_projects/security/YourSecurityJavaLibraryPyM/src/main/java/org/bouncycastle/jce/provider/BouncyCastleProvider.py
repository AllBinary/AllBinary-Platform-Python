# Generated Code Do Not Modify
# package org.bouncycastle.jce.provider

from __future__ import annotations

# from java.security.Provider import Provider


class BouncyCastleProvider(Provider):
    info: str = "BouncyCastle Security Provider v1.41"
    PROVIDER_NAME: str = "BC"
    

    def __init__(self) -> None:
        super().__init__(BouncyCastleProvider.PROVIDER_NAME, 1.41, BouncyCastleProvider.info)
    

    def setParameter(self, parameterName: str, parameter: object) -> None:
        pass


