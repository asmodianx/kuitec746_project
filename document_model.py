from typing import Optional
#from fastapi_camelcase import CamelModel
#CamelModel
class dmd():
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

class df():
    fileGuid: Optional[str] = None
    fileContents: Optional[str] = None

class api():
    APIGUID: Optional[str] = None
    API: Optional[str] = None
    OwnerEmailAddress: Optional[str] = None
    DateExpires: Optional[str] = None
    PermissionCreate: Optional[bool] = None
    PermissionGlobalAdmin: Optional[bool] = None
    IsDisabled: Optional[bool] = None
    IsDeleted: Optional[bool] = None

class ifm():
    InputFormatGuid: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    FileExtension: Optional[str] = None
    FileMIMEType: Optional[str] = None

class ofm():
    OutputFormatGuid: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    FunctionName: Optional[str] = None
    FileExtension: Optional[str] = None
    FileMIMEType: Optional[str] = None

class sr():
    SearchGuid: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
