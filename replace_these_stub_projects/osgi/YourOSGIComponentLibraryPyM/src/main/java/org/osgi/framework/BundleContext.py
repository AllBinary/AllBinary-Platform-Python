# Generated Code Do Not Modify
# package org.osgi.framework

from __future__ import annotations



# Java interface
class BundleContext:
    

    def getBundles(self) -> list[Bundle]:
        raise NotImplementedError()
    

    # throws BundleException
    def installBundle(self, location: str) -> Bundle:
        raise NotImplementedError()
    

    def registerService(self, clazz: str, service: object, properties: Dictionary) -> ServiceRegistration:
        raise NotImplementedError()
    

    def getService(self, reference: ServiceReference) -> object:
        raise NotImplementedError()
    

    # throws InvalidSyntaxException
    def getServiceReferences(self, clazz: str, filter: str) -> list[ServiceReference]:
        raise NotImplementedError()
    

    def getServiceReference(self, clazz: str) -> ServiceReference:
        raise NotImplementedError()
# from java.util.Dictionary import Dictionary


