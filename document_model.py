from typing import Optional
from fastapi_camelcase import CamelModel

class dmd(CamelModel):
    APIGUID: Optional[str] = None
    FileMetaDataGUID: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DateUploaded: Optional[str] = None
    DateModified: Optional[str] = None
    Revision: Optional[str] = None
    IsCurrent: Optional[bool] = None
    IsDeleted: Optional[bool] = None
    FileGuid: Optional[str] = None
    InputFormatGuid: Optional[str] = None
    FileHash: Optional[str] = None
    FileCacheExpiration: Optional[str] = None

class df(CamelModel):
    fileGuid: Optional[str] = None
    fileContents: Optional[str] = None

class api(CamelModel):
    APIDGUID: Optional[str] = None
    API: Optional[str] = None
    OwnerEmailAddress: Optional[str] = None
    DateExpires: Optional[str] = None
    PermissionCreate: Optional[bool] = None
    PermissionGlobalAdmin: Optional[bool] = None
    IsDisabled: Optional[bool] = None
    IsDeleted: Optional[bool] = None

class ifm(CamelModel):
    InputFormatGuid: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    FileExtension: Optional[str] = None
    FileMIMEType: Optional[str] = None

class ofm(CamelModel):
    OutputFormatGuid: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    FunctionName: Optional[str] = None
    FileExtension: Optional[str] = None
    FileMIMEType: Optional[str] = None

class sr(CamelModel):
    SearchGuid: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
