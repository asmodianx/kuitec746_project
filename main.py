import uuid

from fastapi import FastAPI, HTTPException
from typing import List

from document_model import df, dmd, ifm, ofm, api, sr
from document_repository import (get_all_df, get_all_dmd, get_df, get_dmd, create_df, create_dmd, update_df, update_dmd,
                                 delete_df, delete_dmd, purge_dmd, get_all_ifm, get_ifm, create_ifm, update_ifm,
                                 delete_ifm, get_all_ofm, get_ofm, create_ofm, update_ofm, delete_ofm, get_all_api,
                                 get_api, create_api, update_api, delete_api, purge_api, get_all_sr, get_sr, create_sr,
                                 update_sr, delete_sr)
app = FastAPI()

#TODO: df and dmd - the insert statements for DMD needs to check to see if the file guid and ifm guid exists before inserting
#todo: create sql to return GUID exists for all tables then run it for updates inserts

# === get all record 
@app.get("/df")
def api_get_all_df() -> List[df]:
    return get_all_df()

@app.get("/dmd")
def api_get_all_dmd() -> List[dmd]:
    return get_all_dmd()

@app.get("/ifm")
def api_get_all_ifm() -> List[ifm]:
    return get_all_ifm()

@app.get("/ofm")
def api_get_all_ofm() -> List[ofm]:
    return get_all_ifm()

@app.get("/api")
def api_get_all_api() -> List[api]:
    return get_all_api()

@app.get("/sr")
def api_get_all_sr() -> List[sr]:
    return get_all_sr()

# === get one record
@app.get("/df/{did}")
def api_get_df(did: str) -> df:
    did = uuid.UUID(FileMetaDataGUID)
    df = get_user(did)
    return df

@app.get("/dmd/{did}")
def api_get_dmd(did: str) -> dmd:
    did = uuid.UUID(did)
    dmd = get_user(did)
    return dmd

@app.get("/ifm/{did}")
def api_get_ifm(did: str) -> ifm:
    did = uuid.UUID(did)
    ifm = get_ifm(did)
    return ifm

@app.get("/ofm/{did}")
def api_get_ofm(FileMetaDataGUID: str) -> Format:
    did = uuid.UUID(did)
    ofm = get_ofm(did)
    return ofm

@app.get("/api/{did}")
def api_get_api(did: str) -> api:
    did = uuid.UUID(did)
    api = get_ofm(api)
    return api
@app.get("/sr/{did}")
def api_get_sr(did: str) -> sr:
    did = uuid.UUID(did)
    sr = get_ofm(sr)
    return sr

#=== create record
@app.post("/df")
def api_create_df(df: df) -> List[df]:
    return create_user(user)

@app.post("/dmd")
def api_create_dmd(dmd: dmd) -> List[dmd]:
    return create_dmd()

@app.post("/ifm")
def api_create_ifm() -> List[ifm]:
    return create_ifm()

@app.post("/ofm")
def api_create_ofm() -> List[ofm]:
    return create_ofm()

@app.post("/api")
def api_create_api() -> List[api]:
    return create_api()

@app.post("/sr")
def api_create_sr() -> List[sr]:
    return create_sr()

# update record

@app.put("/df/{did}")
def api_update_df(did: str,  df:df) -> df:
    if did != df.fileGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_df(did, df)

@app.put("/dmd/{did}")
def api_update_dmd(did: str,  dmd:dmd) -> dmd:
    if did != dmd.fileGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_dmd(did, dmd)

@app.put("/ifm/{did}")
def api_update_ifm(did: str,  ifm:ifm) -> ifm:
    if did != ifm.fileGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_ifm(did, ifm)

@app.put("/ofm/{did}")
def api_update_ofm(did: str,  ofm:ofm) -> ofm:
    if did != ofm.fileGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_df(did, df)

@app.put("/api/{did}")
def api_update_df(did: str,  api:api) -> api:
    if did != df.fileGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_df(did, api)

@app.put("/sr/{did}")
def api_update_sr(did: str,  sr:sr) -> sr:
    if did != df.fileGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_sr(did, sr)

# delete record

@app.delete("/df/{did}")
def api_delete_df(did: str):
    did = uuid.UUID(did)
    delete_user(did)

@app.delete("/dmd/{did}")
def api_delete_dmd(did: str):
    did = uuid.UUID(did)
    delete_user(did)

@app.delete("/ifm/{did}")
def api_delete_ifm(did: str):
    did = uuid.UUID(did)
    delete_user(did)

@app.delete("/ofm/{did}")
def api_delete_ofm(did: str):
    did = uuid.UUID(did)
    delete_user(did)

@app.delete("/api/{did}")
def api_delete_api(did: str):
    did = uuid.UUID(did)
    delete_user(did)

@app.delete("/sr/{did}")
def api_delete_sr(did: str):
    did = uuid.UUID(did)
    delete_user(did)
