import uuid
from typing import List

from document_model import df, dmd, ifm, ofm, api, sr
from db_connection import DBConnection

# Documents
#GET_ALL_FILE_BY_API = 'select A."API",A."APIGUID",A."OwnerEmailAddress",B."Name",B."Description",B."DateModified",B."DateUploaded",B."Revision",B."Name",B."IsCurrent",D."FileMIMEType",D."FileExtension",C."fileGuid" from "kershner"."API" A, "kershner"."FileMetadata" B,"kershner"."InputFile" C,"kershner"."InputFileFormat" D WHERE A."APIGUID" = %s AND A."APIGUID" = B."APIGUID" AND B."FileGuid" = C."fileGuid" AND  B."InputFormatGuid" = D."InputFormatGuid" AND A."IsDeleted" = false AND A."IsDisabled" = false AND A."DateExpires"::date > current_date AND B."IsCurrent" = true AND B."IsDeleted" = false;'
#INSERT_FMD = 'INSERT INTO kershner."FileMetadata"("APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration") SELECT %s as "APIGUID", %s as "FileMetaDataGUID", %s as "Name", %s as "Description", CURRENT_DATE as "DateUploaded", CURRENT_DATE as "DateModified", '1' as "Revision", true as "IsCurrent", false as "IsDeleted", "fileGuid" as "fileGuid", %s as "InputFormatGuid", md5("fileContents")::text as fileHash, %s as "FileCacheExpiration" FROM kershner."InputFile" WHERE "fileGuid" = %s;'
#INSERT_FILE = 'INSERT INTO kershner."InputFile"("fileGuid", "fileContents") values(%s,%s);'
#GET_FILE_BY_ID = 'select A."API",A."OwnerEmailAddress",B."FileMetaDataGUID",B."Name",B."Description",B."DateModified",B."DateUploaded",B."Revision",B."Name",B."IsCurrent",D."FileMIMEType",D."FileExtension",C."fileContents" from "kershner"."API" A,"kershner"."FileMetadata" B,"kershner"."InputFile" C,"kershner"."InputFileFormat" D WHERE A."APIGUID" = %s AND B."FileMetaDataGUID" = %s A."APIGUID" = B."APIGUID" AND B."FileGuid" = C."fileGuid" AND B."InputFormatGuid" = D."InputFormatGuid" AND A."IsDeleted" = false AND A."IsDisabled" = false AND A."DateExpires"::date > current_date AND B."IsCurrent" = true AND B."IsDeleted" = false;'

# Document file DF
SELECT_ALL_FILES = 'SELECT "fileGuid", "fileContents" FROM "kershner"."InputFile";'
SELECT_FILE = 'SELECT "fileGuid", "fileContents" FROM "kershner"."InputFile" WHERE "fileGuid" = %s;'
INSERT_FILE = 'INSERT INFO "kershner"."InputFile" "fileGuid", "fileContents" values(%s,%s);'
UPDATE_FILE = 'UPDATE "kershner"."InputFile" "fileContents" = %s WHERE "fileGuid" = %s;'
DELETE_FILE = 'DELETE * FROM "kershner"."InputFile" WHERE "fileGuid" = %s;'

# DOCUMENT META DATA DMD
SELECT_ALL_MD = 'SELECT "APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration" FROM "kershner"."FileMetadata";'
SELECT_MD = 'SELECT "APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration" FROM "kershner"."FileMetadata" WHERE "FileMetaDataGUID"=%s;'
INSERT_MD = 'INSERT INTO "kershner"."FileMetadata" "APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration" values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
UPDATE_MD = 'UPDATE "kershner"."FileMetadata" SET "APIGUID" = %s, "Name" = %s, "Description" = %s, "DateUploaded" = %s, "DateModified" = %s, "Revision", "IsCurrent" = %s, "IsDeleted" = %s, "FileGuid" = %s, "InputFormatGuid" = %s, "FileHash" = %s, "FileCacheExpiration" = %s WHERE "FileMetaDataGUID";'
DELETE_MD = 'UPDATE "kershner"."FileMetadata" SET "IsDeleted" = true where "FileMetaDataGUID"=%s;'
PURGE_MD = 'DELETE * FROM "kershner"."FileMetadata" where "FileMetaDataGUID"=%s;'

# input format IFM
SELECT_ALL_IF = 'SELECT "InputFormatGuid", "Name", "Description", "FileExtension", "FileMIMEType" FROM "kershner"."InputFileFormat";'
SELECT_IF = 'SELECT "InputFormatGuid", "Name", "Description", "FileExtension", "FileMIMEType" FROM "kershner"."InputFileFormat" WHERE InputFormatGuid=%s;'
INSERT_IF = 'INSERT INTO "kershner"."InputFileFormat" "InputFormatGuid", "Name", "Description", "FileExtension", "FileMIMEType" VALUES(GEN_RANDOM_UUID(),%s,%s,%s,%s);'
UPDATE_IF = 'UPDATE "kershner"."InputFileFormat" SET "Name"=%s, "Description"=%s, "FileExtension"=%s, "FileMIMEType" = %s WHERE InputFormatGuid=%s;'
DELETE_IF = 'DELETE FROM "kershner"."InputFileFormat" WHERE InputFormatGuid=%s;'

# output format OFM
SELECT_ALL_OF = 'SELECT "OutputFormatGuid", "Name", "Description", "FunctionName", "FileExtension", "FileMIMEType" FROM "kershner"."DataOutputFormat";'
SELECT_OF = 'SELECT "OutputFormatGuid", "Name", "Description", "FunctionName", "FileExtension", "FileMIMEType" FROM "kershner"."DataOutputFormat" WHERE "OutputFormatGuid"=%s;'
INSERT_OF = 'INSERT INTO "kershner"."DataOutputFormat" "OutputFormatGuid", "Name", "Description", "FunctionName", "FileExtension", "FileMIMEType" VALUES(GEN_RANDOM_UUID(),%s,%s,%s,%s,%s);'
UPDATE_OF = 'UPDATE "kershner"."DataOutputFormat" SET "Name" = %s, "Description" = %s, "FunctionName" = %s, "FileExtension" = %s, "FileMIMEType" = %s WHERE "OutputFormatGuid"=%s;'
DELETE_OF = 'DELETE * FROM "kershner"."DataOutputFormat" WHERE "OutputFormatGuid"=%s;'

# API API
SELECT_ALL_API = 'SELECT "APIGUID", "API", "OwnerEmailAddress", "DateExpires", "PermissionCreate", "PermissionGlobalAdmin", "IsDisabled", "IsDeleted" FROM "kershner"."API";'
SELECT_API = 'SELECT "APIGUID", "API", "OwnerEmailAddress", "DateExpires", "PermissionCreate", "PermissionGlobalAdmin", "IsDisabled", "IsDeleted" FROM "kershner"."API" WHERE APIGUID=%s;'
INSERT_API = 'INSERT INTO "kershner"."API" "APIGUID", "API", "OwnerEmailAddress", "DateExpires", "PermissionCreate", "PermissionGlobalAdmin", "IsDisabled", "IsDeleted" VALUES (GENERATE_RANDOM_UUID(),%s,%s,%s,%s,%s,false,false);'
UPDATE_API = 'UPDATE "kershner"."API" SET "API" = %s, "OwnerEmailAddress" = %s, "DateExpires" = %s, "PermissionCreate" = %s, "PermissionGlobalAdmin" = %s, "IsDisabled" = %s, "IsDeleted" = %s WHERE "APIGUID" = %s;'
DELETE_API = 'UPDATE "kershner"."API" SET IsDisabled = true,IsDeleted = true WHERE "APIGUID" = %s;'
PURGE_API = 'DELETE * FROM "kershner"."API" WHERE "APIGUID" = %s;'

# search SR
SELECT_ALL_SEARCH = 'SELECT "SearchGUID", "Name", "Description" FROM "kershner"."Search";'
SELECT_SEARCH = 'SELECT "SearchGUID", "Name", "Description" FROM "kershner"."Search" where "SearchGUID" = %s;'
INSERT_SEARCH = 'INSERT INTO "kershner"."Search" "SearchGUID", "Name", "Description" VALUES(GENERATE_RANDOM_UUID(),%s,%s);'
UPDATE_SEARCH = 'UPDATE "SearchGUID", "Name", "Description" FROM "kershner"."Search";'
DELETE_SEARCH = 'DELETE * FROM "kershner"."Search" WHERE "SearchGUID" = %s;'

#fixme: ubdates get two dids, by default it uses the one imbedded in the data object but for some reason im pulling the did in seperatly... 

def get_all_df() -> List[df]:
    df_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_FILES)
#"fileGuid", "fileContents"
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
    #"APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration"
    for row in cur:
        dmd_list.append(
            dmd(
                APIGUID=str(row[0]),
                FileMetaDataGUID=str(row[1]),
                Name=str(row[2]),
                Description=str(row[3]),
                DateUploaded=str(row[4]),
                DateModified=str(row[5]),
                Revision=str(row[6]),
                IsCurrent=bool(row[7]),
                IsDeleted=bool(row[8]),
                FileGuid=str(row[9]),
                InputFormatGuid=str(row[10]),
                FileHash=str(row[11]),
                FileCacheExpiration=str(row[12])
            )
        )
    return dmd_list

def get_df(did: uuid) -> List[df]:
    df_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_FILE, did)
#"fileGuid", "fileContents"
    for row in cur:
        df_list.append(
            df(
                fileGuid=str(row[0]),
                fileContents=str(row[1])
            )
        )
    return df_list

def get_dmd(did: uuid) -> List[dmd]:
    dmd_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_MD, did)
    #"APIGUID", "FileMetaDataGUID", "Name", "Description", "DateUploaded", "DateModified", "Revision", "IsCurrent", "IsDeleted", "FileGuid", "InputFormatGuid", "FileHash", "FileCacheExpiration"
    for row in cur:
        dmd_list.append(
            dmd(
                APIGUID=str(row[0]),
                FileMetaDataGUID=str(row[1]),
                Name=str(row[2]),
                Description=str(row[3]),
                DateUploaded=str(row[4]),
                DateModified=str(row[5]),
                Revision=str(row[6]),
                IsCurrent=bool(row[7]),
                IsDeleted=bool(row[8]),
                FileGuid=str(row[9]),
                InputFormatGuid=str(row[10]),
                FileHash=str(row[11]),
                FileCacheExpiration=str(row[12])
            )
        )
    return dmd_list

def create_df(df: df) -> df:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.uuid4()
    df.fileGuid = did
    cur.execute(INSERT_FILE, (
        df.fileGuid,
        df.fileContents
        )
    )
    db.connection.commit()
    return get_df(did)

def create_dmd(dmd: dmd) -> dmd:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.uuid4()
    dmd.FileMetaDataGUID = did
    cur.execute(INSERT_MD, (
        dmd.APIGUID,
        dmd.FileMetaDataGUID,
        dmd.Name,
        dmd.Description,
        dmd.DateUploaded,
        dmd.DateModified,
        dmd.Revision,
        dmd.IsCurrent,
        dmd.IsDeleted,
        dmd.FileGuid,
        dmd.InputFormatGuid,
        dmd.FileHash,
        dmd.FileCacheExpiration
       )
    )
    db.connection.commit()
    return get_dmd(did)

def update_df(df: df) -> df:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(df.fileGuid)
    cur.execute(UPDATE_FILE, (did, df.fileContents))
    db.connection.commit()
    return get_df(did)

def update_dmd(dmd: dmd) -> dmd:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(dmd.FileMetaDataGUID)
    cur.execute(UPDATE_MD, (did, dmd.fileContents))
    db.connection.commit()
    return get_dmd(did)

def delete_df(did: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_FILE, [did])
    db.connection.commit()
    return
    
def delete_dmd(did: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_MD, [did])
    db.connection.commit()
    return

def purge_dmd(did: uuid):
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
    #"InputFormatGuid", "Name", "Description", "FileExtension", "FileMIMEType"
    for row in cur:
        ifm_list.append(
            ifm(
                InputFormatGuid=str(row[0]),
                Name=str(row[1]),
                Description=str(row[2]),
                FileExtension=str(row[3]),
                FileMIMEType=str(row[4])
            )
        )
    return ifm_list

def get_ifm(did: uuid) -> List[ifm]:
    ifm_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_IF, did)
    for row in cur:
        ifm_list.append(
            ifm(
                InputFormatGuid=str(row[0]),
                Name=str(row[1]),
                Description=str(row[2]),
                FileExtension=str(row[3]),
                FileMIMEType=str(row[4])
                )
        )
    return ifm_list

def create_ifm(ifm: ifm) -> ifm:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.uuid4()
    ifm.InputFormatGuid = did
    cur.execute(INSERT_IF, (
    ifm.InputFormatGuid, 
        ifm.Name,
        ifm.Description,
        ifm.FileExtension,
        ifm.FileMIMEType
        )
    )
    db.connection.commit()
    return get_ifm(did)

def update_ifm(ifm: ifm) -> ifm:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(ifm.InputFormatGuid)
    cur.execute(UPDATE_IF, (did, ifm.Name, ifm.Description, ifm.FileExtension, ifm.FileMIMEType))
    db.connection.commit()
    return get_ifm(did)

def delete_ifm(did: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_IF, [did])
    db.connection.commit()
    return
    
#==== output format
#"OutputFormatGuid", "Name", "Description", "FunctionName", "FileExtension", "FileMIMEType" 
def get_all_ofm() -> List[ofm]:
    ofm_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_OF)

    for row in cur:
        ofm_list.append(
            ofm(
                OutputFormatGuid=str(row[0]),
                Name=str(row[1]),
                Description=str(row[2]), 
                FunctionName=str(row[3]),
                FileExtension=str(row[4]),
                FileMIMEType=str(row[5])
            )
        )
    return ofm_list
def get_ofm(did: uuid) -> List[ofm]:
    ofm_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_OF, did)
    for row in cur:
        ofm_list.append(
            ofm(
                OutputFormatGuid=str(row[0]),
                Name=str(row[1]),
                Description=str(row[2]),
                FunctionName=str(row[3]),
                FileExtension=str(row[4]),
                FileMIMEType=str(row[5])
            )
        )
    return ofm_list

def create_ofm(ofm: ofm) -> ofm:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.uuid4()
    ofm.OutputFormatGuid = did
    cur.execute(INSERT_OF, (
    ofm.OutputFormatGuid, 
        ofm.Name,
        ofm.FunctionName,
        ofm.FileExtension,
        ofm.FileMIMEType
        )
    )
    db.connection.commit()
    return get_ofm(did)

def update_ofm(ofm: ofm) -> ofm:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(ofm.OutputFormatGuid)
    cur.execute(UPDATE_OF, (did, ofm.Name, ofm.FunctionName, ofm.FileExtension, ofm.FileMIMEType))
    db.connection.commit()
    return get_ofm(did)

def delete_ofm(did: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_OF, [did])
    db.connection.commit()
    return
    
#=== API
#"APIGUID", "API", "OwnerEmailAddress", "DateExpires", "PermissionCreate", "PermissionGlobalAdmin", "IsDisabled", "IsDeleted"
def get_all_api() -> List[api]:
    api_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_ALL_API)
    for row in cur:
        api_list.append(
            api(
                APIGUID=str(row[0]),
                API=str(row[1]),
                OwnerEmailAddress=str(row[2]),
                DateExpires=str(row[3]),
                PermissionCreate=bool(row[4]),
                PermissionGlobalAdmin=bool(row[5]),
                IsDisabled=bool(row[6]),
                IsDeleted=bool(row[7])
                )
        )
    return api_list    
def get_api(did: uuid) -> List[api]:
    api_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_API, did)
    for row in cur:
        api_list.append(
            api(
                APIGUID=str(row[0]),
                API=str(row[1]),
                OwnerEmailAddress=str(row[2]), 
                DateExpires=str(row[3]), 
                PermissionCreate=bool(row[4]),
                PermissionGlobalAdmin=bool(row[5]),
                IsDisabled=bool(row[6]),
                IsDeleted=bool(row[7])
            )
        )
    return api_list

def create_api(api: api) -> api:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.uuid4()
    api.OutputFormatGuid = did
    cur.execute(INSERT_API, (
    api.APIGUID, 
        api.API,
        api.OwnerEmailAddress,
        api.DateExpires,
        api.PermissionCreate,
        api.PermissionGlobalAdmin,
        api.IsDisabled,
        api.IsDeleted
        )
    )
    db.connection.commit()
    return get_api(did)

def update_api(api: api) -> api:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(api.OutputFormatGuid)
    cur.execute(UPDATE_API, (did, api.API, api.OwnerEmailAddress, api.DateExpires, api.PermissionCreate, api.PermissionGlobalAdmin, api.IsDisabled, api.IsDeleted))
    db.connection.commit()
    return get_api(did)

def delete_api(did: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_API, [did])
    db.connection.commit()
    return    

def purge_api(did: uuid):
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
    #"SearchGUID", "Name", "Description"
    for row in cur:
        sr_list.append(
            sr(
                SearchGUID=str(row[0]),
                Name=str(row[1]),
                Description=str(row[2])
            )
        )
    return sr_list
def get_sr(did: uuid) -> List[sr]:
    sr_list = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(SELECT_SEARCH, did)
    for row in cur:
        sr_list.append(
            sr(
                SearchGUID=str(row[0]),
                Name=str(row[1]),
                Description=str(row[2])
            )
        )
    return sr_list

def create_sr(sr: sr) -> sr:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.uuid4()
    sr.OutputFormatGuid = did
    cur.execute(INSERT_SEARCH, (
        sr.SearchGUID,
        sr.Name,
        sr.Description
        )
    )
    db.connection.commit()
    return get_sr(did)

def update_sr(sr: sr) -> sr:
    db = DBConnection()
    cur = db.get_cursor()
    did = uuid.UUID(sr.OutputFormatGuid)
    cur.execute(UPDATE_SEARCH, (did, sr.Name, sr.Description))
    db.connection.commit()
    return get_sr(did)

def delete_sr(did: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE_SEARCH, [did])
    db.connection.commit()
    return
