import uuid
from typing import List

from document_model import df, dmd, ifm, ofm, api, sr
from db_connection import DBConnection

# Documents
#GET_ALL_FILE_BY_API = 'select A."API",A."APIGUID",A."OwnerEmailAddress",B."Name",B."Description",B."DateModified",B."DateUploaded",B."Revision",B."Name",B."IsCurrent",D."FileMIMEType",D."FileExtension",C."fileGuid" from kershner."API" A, kershner."FileMetadata" B,kershner."InputFile" C,kershner."InputFileFormat" D WHERE A."APIGUID" = %s AND A."APIGUID" = B."APIGUID" AND B."FileGuid" = C."fileGuid" AND  B."InputFormatGuid" = D."InputFormatGuid" AND A."IsDeleted" = false AND A."IsDisabled" = false AND A."DateExpires"::date > current_date AND B."IsCurrent" = true AND B."IsDeleted" = false;'
#INSERT_FMD = 'INSERT INTO kershner."FileMetadata"("APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration") SELECT %s as "APIGUID", %s as "FileMetaDataGUID", %s as "Name", %s as "Description", CURRENT_DATE as "DateUploaded", CURRENT_DATE as "DateModified", '1' as "Revision", true as "IsCurrent", false as "IsDeleted", "fileGuid" as "fileGuid", %s as "InputFormatGuid", md5("fileContents")::text as fileHash, %s as "FileCacheExpiration" FROM kershner."InputFile" WHERE "fileGuid" = %s;'
#INSERT_FILE = 'INSERT INTO kershner."InputFile"("fileGuid", "fileContents") values(%s,%s);'
#GET_FILE_BY_ID = 'select A."API",A."OwnerEmailAddress",B."FileMetaDataGUID",B."Name",B."Description",B."DateModified",B."DateUploaded",B."Revision",B."Name",B."IsCurrent",D."FileMIMEType",D."FileExtension",C."fileContents" from kershner."API" A,kershner."FileMetadata" B,kershner."InputFile" C,kershner."InputFileFormat" D WHERE A."APIGUID" = %s AND B."FileMetaDataGUID" = %s A."APIGUID" = B."APIGUID" AND B."FileGuid" = C."fileGuid" AND B."InputFormatGuid" = D."InputFormatGuid" AND A."IsDeleted" = false AND A."IsDisabled" = false AND A."DateExpires"::date > current_date AND B."IsCurrent" = true AND B."IsDeleted" = false;'
#UPDATE_FILE= "UPDATE users set first_name = %s, last_name=%s WHERE user_id = %s"
#DELETE_FILE = "DELETE FROM users where user_id=%s"

# Document file DF
SELECT_ALL_FILES = 'SELECT "fileGuid", "fileContents" FROM kershner."InputFile";'
SELECT_FILE = 'SELECT "fileGuid", "fileContents" FROM kershner."InputFile" WHERE "fileGuid" = %s;'
INSERT_FILE = 'INSERT INFO kershner."InputFile" values(%s,%s);'
UPDATE_FILE = 'UPDATE kershner."InputFile" "fileContents" = %s WHERE "fileGuid" = %s;'
DELETE_FILE = 'DELETE FROM kershner."InputFile" WHERE "fileGuid" = %s;'

# DOCUMENT META DATA DMD
SELECT_ALL_MD = 'SELECT "APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration" FROM kershner."FileMetadata";'
SELECT_MD = 'SELECT "APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration" FROM kershner."FileMetadata" WHERE "FileMetaDataGUID"=%s;'
INSERT_MD = 'INSERT INTO kershner."FileMetadata" values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
UPDATE_MD = 'UPDATE kershner."FileMetadata" SET "APIGUID" = %s, "Name" = %s, "Description" = %s, "DateUploaded" = %s, "DateModified" = %s, "Revision", "IsCurrent" = %s, "IsDeleted" = %s, "FileGuid" = %s, "InputFormatGuid" = %s, "FileHash" = %s, "FileCacheExpiration" = %s WHERE "FileMetaDataGUID";'
DELETE_MD = 'UPDATE kershner."FileMetadata" SET "IsDeleted" = true where "FileMetaDataGUID"=%s;'
PURGE_MD = 'DELETE FROM kershner."FileMetadata" where "FileMetaDataGUID"=%s;'

# input format IFM
SELECT_ALL_IF = 'SELECT "InputFormatGuid", "Name", "Description", "FileExtension", "FileMIMEType" FROM kershner."InputFileFormat";'
SELECT_IF = 'SELECT "InputFormatGuid", "Name", "Description", "FileExtension", "FileMIMEType" FROM kershner."InputFileFormat" WHERE "InputFormatGuid"=%s;'
INSERT_IF = 'INSERT INTO kershner."InputFileFormat" VALUES(%s,%s,%s,%s,%s);'
UPDATE_IF = 'UPDATE kershner."InputFileFormat" SET "Name"=%s, "Description"=%s, "FileExtension"=%s, "FileMIMEType" = %s WHERE InputFormatGuid=%s;'
DELETE_IF = 'DELETE FROM kershner."InputFileFormat" WHERE InputFormatGuid=%s;'

# output format OFM
SELECT_ALL_OF = 'SELECT "OutputFormatGuid", "Name", "Description", "FunctionName", "FileExtension", "FileMIMEType" FROM kershner."DataOutputFormat";'
SELECT_OF = 'SELECT "OutputFormatGuid", "Name", "Description", "FunctionName", "FileExtension", "FileMIMEType" FROM kershner."DataOutputFormat" WHERE "OutputFormatGuid"=%s;'
INSERT_OF = 'INSERT INTO kershner."DataOutputFormat" VALUES(%s,%s,%s,%s,%s,%s);'
UPDATE_OF = 'UPDATE kershner."DataOutputFormat" SET "Name" = %s, "Description" = %s, "FunctionName" = %s, "FileExtension" = %s, "FileMIMEType" = %s WHERE "OutputFormatGuid"=%s;'
DELETE_OF = 'DELETE FROM kershner."DataOutputFormat" WHERE "OutputFormatGuid"=%s;'

# API API
SELECT_ALL_API = 'SELECT "APIGUID", "API", "OwnerEmailAddress", "DateExpires", "PermissionCreate", "PermissionGlobalAdmin", "IsDisabled", "IsDeleted" FROM kershner."API";'
SELECT_API = 'SELECT "APIGUID", "API", "OwnerEmailAddress", "DateExpires", "PermissionCreate", "PermissionGlobalAdmin", "IsDisabled", "IsDeleted" FROM kershner."API" WHERE "APIGUID"=%s;'
INSERT_API = 'INSERT INTO kershner."API" VALUES (%s,%s,%s,%s,%s,%s,false,false);'
UPDATE_API = 'UPDATE kershner."API" SET "API" = %s, "OwnerEmailAddress" = %s, "DateExpires" = %s, "PermissionCreate" = %s, "PermissionGlobalAdmin" = %s, "IsDisabled" = %s, "IsDeleted" = %s WHERE "APIGUID" = %s;'
DELETE_API = 'UPDATE kershner."API" SET IsDisabled = true,IsDeleted = true WHERE "APIGUID" = %s;'
PURGE_API = 'DELETE FROM kershner."API" WHERE "APIGUID" = %s;'

# search SR
SELECT_ALL_SEARCH = 'SELECT "SearchGUID", "Name", "Description" FROM kershner."Search";'
SELECT_SEARCH = 'SELECT "SearchGUID", "Name", "Description" FROM kershner."Search" where "SearchGUID" = %s;'
INSERT_SEARCH = 'INSERT INTO kershner."Search" VALUES(%s,%s,%s);'
UPDATE_SEARCH = 'UPDATE kershner."Search" set "Name"=%s, "Description"=%s where "SearchGUID"=%s;'
DELETE_SEARCH = 'DELETE FROM kershner."Search" WHERE "SearchGUID" = %s;'

def get_all_df() -> List[df]:
    df_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_FILES)
    for row in cur:
        df_list.append(
            df(
                fileGuid=str(row[0]),
                fileContents=str(row[1])
            )
        )
    return df_list

def get_all_dmd() -> List[dmd]:
    dmd_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_MD)
    for row in cur:
        dmd_list.append(
            dmd(
                apiGuid=str(row[0]),
                fileMetaDataGUID=str(row[1]),
                name=str(row[2]),
                description=str(row[3]),
                dateUploaded=str(row[4]),
                dateModified=str(row[5]),
                revision=str(row[6]),
                isCurrent=bool(row[7]),
                isDeleted=bool(row[8]),
                fileGuid=str(row[9]),
                inputFormatGuid=str(row[10]),
                fileHash=str(row[11]),
                fileCacheExpiration=str(row[12])
            )
        )
    return dmd_list

def get_df(did: str) -> List[df]:
    df_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_FILE, [did])
#fileGuid, fileContents
    for row in cur:
        df_list=df(fileGuid=str(row[0]), fileContents=str(row[1]))
    return df_list

def get_dmd(did: uuid) -> List[dmd]:
    dmd_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_MD, [did])
    
    for row in cur:
        dmd_list = dmd(apiGuid = str(row[0]),fileMetaDataGUID = str(row[1]),name = str(row[2]),description = str(row[3]),dateUploaded = str(row[4]),dateModified = str(row[5]),revision = str(row[6]),isCurrent = bool(row[7]),isDeleted = bool(row[8]),fileGuid = str(row[9]),inputFormatGuid = str(row[10]),fileHash = str(row[11]),fileCacheExpiration = str(row[12]))
    return dmd_list

def create_df(df_create: df) -> df:
    db = DBConnection()
    cur = db.get_cursor()
    did = str(uuid.uuid4())
    cur.execute(INSERT_FILE, (did,df_create.fileContents))
    db.connection.commit()
    return get_df(did)

def create_dmd(dmd_create: dmd) -> dmd:
    db = DBConnection()
    cur = db.get_cursor()
    did = str(uuid.uuid4())
    cur.execute(INSERT_MD, (dmd_create.apiGuid,did,dmd_create.name,dmd_create.description,dmd_create.dateUploaded,dmd_create.dateModified,dmd_create.revision,dmd_create.isCurrent,dmd_create.isDeleted,dmd_create.fileGuid,dmd_create.inputFormatGuid,dmd_create.fileHash,dmd_create.fileCacheExpiration))
    db.connection.commit()
    return get_dmd(did)

def update_df(df_update: df) -> df:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(df_update.fileGuid)
    cur.execute(UPDATE_FILE, (did, df_update.fileContents))
    db.connection.commit()
    return get_df(did)

def update_dmd(dmd_update: dmd) -> dmd:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(dmd_update.fileMetaDataGUID)
    cur.execute(UPDATE_MD, (dmd_update.apiGuid, did, dmd_update.name, dmd_update.description, dmd_update.dateUploaded, dmd_update.dateModified, dmd_update.revision, dmd_update.isCurrent, dmd_update.isDeleted, dmd_update.fileGuid, dmd_update.inputFormatGuid, dmd_update.fileHash, dmd_update.fileCacheExpiration))
    db.connection.commit()
    return get_dmd(did)

def delete_df(did):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_FILE, [did])
    db.connection.commit()
    return
    
def delete_dmd(did: str):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_MD, [did])
    db.connection.commit()
    return

def purge_dmd(did: str):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(PURGE_MD, [did])
    db.connection.commit()
    return

#==== input format
def get_all_ifm() -> List[ifm]:
    ifm_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_IF)
    for row in cur:
        ifm_list.append(
            ifm(
                inputFormatGuid=str(row[0]),
                name=str(row[1]),
                description=str(row[2]),
                fileExtension=str(row[3]),
                fileMimeType=str(row[4])
            )
        )
    return ifm_list

def get_ifm(did: str) -> List[ifm]:
    ifm_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_IF, [did])
    for row in cur:
        ifm_list=ifm(inputFormatGuid=str(row[0]), name=str(row[1]),description=str(row[2]),fileExtension=str(row[3]),fileMimeType=str(row[4]))
    return ifm_list

def create_ifm(ifm_create: ifm) -> ifm:
    db = DBConnection()
    cur = db.get_cursor()
    did = str(uuid.uuid4())
    cur.execute(INSERT_IF, (did, ifm_create.name,ifm_create.description,ifm_create.fileExtension,ifm_create.fileMimeType))
    db.connection.commit()
    return get_ifm(did)

def update_ifm(ifm_update: ifm) -> ifm:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(ifm_update.inputFormatGuid)
    cur.execute(UPDATE_IF, (did, ifm_update.name, ifm_update.description, ifm_update.fileExtension, ifm_update.fileMimeType))
    db.connection.commit()
    return get_ifm(did)

def delete_ifm(did: str):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_IF, [did])
    db.connection.commit()
    return
    
#==== output format
def get_all_ofm() -> List[ofm]:
    ofm_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_OF)

    for row in cur:
        ofm_list.append(
            ofm(
                outputFormatGuid=str(row[0]),
                name=str(row[1]),
                description=str(row[2]), 
                functionName=str(row[3]),
                fileExtension=str(row[4]),
                fileMimeType=str(row[5])
            )
        )
    return ofm_list
def get_ofm(did: uuid) -> List[ofm]:
    ofm_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_OF,[did])
    for row in cur:
        ofm_list=ofm(outputFormatGuid=str(row[0]),name=str(row[1]),description=str(row[2]),functionName=str(row[3]),fileExtension=str(row[4]),fileMimeType=str(row[5]))
    return ofm_list

def create_ofm(ofm_create: ofm) -> ofm:
    db = DBConnection()
    cur = db.get_cursor()
    did = str(uuid.uuid4())
    cur.execute(INSERT_OF, ( did, ofm_create.name,ofm_create.description, ofm_create.functionName, ofm_create.fileExtension, ofm_create.fileMimeType ))
    db.connection.commit()
    return get_ofm(did)

def update_ofm(ofm_update: ofm) -> ofm:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(ofm_update.outputFormatGuid)
    cur.execute(UPDATE_OF, (did, ofm_update.name, ofm_update.functionName, ofm_update.fileExtension, ofm_update.fileMimeType))
    db.connection.commit()
    return get_ofm(did)

def delete_ofm(did: str):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_OF, [did])
    db.connection.commit()
    return
    
#=== API
def get_all_api() -> List[api]:
    api_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_API)

    for row in cur:
        print(row)
        api_list.append(
            api(
                apiGuid = str(row[0]),
                api = str(row[1]),
                ownerEmailAddress = str(row[2]),
                dateExpires = str(row[3]),
                permissionCreate = bool(row[4]),
                permissionGlobalAdmin = bool(row[5]),
                isDisabled = bool(row[6]),
                isDeleted = bool(row[7])
            )
        )
        print(api_list)  
    return api_list    
def get_api(did: uuid) -> List[api]:
    api_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_API, [did])
    for row in cur:
        api_list=api(apiGuid=str(row[0]),api=str(row[1]),ownerEmailAddress=str(row[2]),dateExpires=str(row[3]),permissionCreate=bool(row[4]),permissionGlobalAdmin=bool(row[5]),isDisabled=bool(row[6]),isDeleted=bool(row[7]))
    return api_list

def create_api(api_create: api) -> api:
    db = DBConnection()
    cur = db.get_cursor()
    did = str(uuid.uuid4())
    cur.execute(INSERT_API, (did,api_create.api,api_create.ownerEmailAddress,api_create.dateExpires,api_create.permissionCreate,api_create.permissionGlobalAdmin,api_create.isDisabled,api_create.isDeleted))
    db.connection.commit()
    return get_api(did)

def update_api(api_update: api) -> api:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(api_update.apiGuid)
    cur.execute(UPDATE_API, (did, api_update.api, api_update.ownerEmailAddress, api_update.dateExpires, api_update.permissionCreate, api_update.permissionGlobalAdmin, api_update.isDisabled, api_update.isDeleted))
    db.connection.commit()
    return get_api(did)

def delete_api(did: str):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_API, [did])
    db.connection.commit()
    return    

def purge_api(did: str):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(PURGE_API, [did])
    db.connection.commit()
    return    

#==== search
def get_all_sr() -> List[sr]:
    sr_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_SEARCH)
    for row in cur:
        sr_list.append(
            sr(
                searchGuid=str(row[0]),
                name=str(row[1]),
                description=str(row[2])
            )
        )
    return sr_list

def get_sr(did: uuid) -> List[sr]:
    sr_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_SEARCH,[did])
    for row in cur:
        sr_list=sr(searchGuid=str(row[0]),name=str(row[1]),description=str(row[2]))
        return sr_list

def create_sr(sr_create: sr) -> sr:
    db = DBConnection()
    cur = db.get_cursor()
    did = str(uuid.uuid4())
    cur.execute(INSERT_SEARCH, (did, sr_create.name, sr_create.description ))
    db.connection.commit()
    return get_sr(did)

def update_sr(sr_update: sr) -> sr:
    db = DBConnection()
    cur = db.get_cursor()
    did =str( uuid.UUID(sr_update.searchGuid))
    cur.execute(UPDATE_SEARCH, (sr_update.name, sr_update.description, did))
    db.connection.commit()
    return get_sr(did)

def delete_sr(did: str):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_SEARCH, [did])
    db.connection.commit()
    return
