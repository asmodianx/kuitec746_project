from typing import Optional
from fastapi_camelcase import CamelModel

class dmd(CamelModel):
    apiGuid: Optional[str] = None
    fileMetaDataGUID: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dateUploaded: Optional[str] = None
    dateModified: Optional[str] = None
    revision: Optional[str] = None
    isCurrent: Optional[bool] = None
    isDeleted: Optional[bool] = None
    fileGuid: Optional[str] = None
    inputFormatGuid: Optional[str] = None
    fileHash: Optional[str] = None
    fileCacheExpiration: Optional[str] = None

class df(CamelModel):
    fileGuid: Optional[str] = None
    fileContents: Optional[str] = None

class api(CamelModel):
    apiGuid: Optional[str] = None
    api: Optional[str] = None
    ownerEmailAddress: Optional[str] = None
    dateExpires: Optional[str] = None
    permissionCreate: Optional[bool] = None
    permissionGlobalAdmin: Optional[bool] = None
    isDisabled: Optional[bool] = None
    isDeleted: Optional[bool] = None

class ifm(CamelModel):
    inputFormatGuid: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    fileExtension: Optional[str] = None
    fileMIMEType: Optional[str] = None

class ofm(CamelModel):
    outputFormatGuid: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    functionName: Optional[str] = None
    fileExtension: Optional[str] = None
    fileMIMEType: Optional[str] = None

class sr(CamelModel):
    searchGuid: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
