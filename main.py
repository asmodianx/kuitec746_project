import uuid

from typing import List
from fastapi import FastAPI, HTTPException


from document_model import df, dmd, ifm, ofm, api, sr
from document_repository import (get_all_df, get_all_dmd, get_df, get_dmd, create_df, 
    create_dmd, update_df, update_dmd, delete_df, delete_dmd, get_all_ifm, 
    get_ifm, create_ifm, update_ifm, delete_ifm, get_all_ofm, get_ofm, create_ofm, 
    update_ofm, delete_ofm, get_all_api, get_api, create_api, update_api, delete_api, 
    get_all_sr, get_sr, create_sr,update_sr, delete_sr)

app = FastAPI()

#TODO: df and dmd - the insert statements for DMD needs to check to see if the 
#file guid and ifm guid exists before inserting

#todo: create sql to return GUID exists for all tables then run it for updates inserts

#fixme: im getting in nulls for some of the fields


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
    return get_all_ofm()

@app.get("/api")
def api_get_all_api() -> List[api]:
    return get_all_api()

@app.get("/sr")
def api_get_all_sr() -> List[sr]:
    return get_all_sr()

# === get one record
@app.get("/df/{did1}")
def api_get_df(did1: str) -> df:
    did = uuid.UUID(did1)
    return get_df(did)

@app.get("/dmd/{did1}")
def api_get_dmd(did1: str) -> dmd:
    did = uuid.UUID(did1)
    return get_dmd(did)

@app.get("/ifm/{did1}")
def api_get_ifm(did1: str) -> ifm:
    did = uuid.UUID(did1)
    return get_ifm(did)

@app.get("/ofm/{did1}")
def api_get_ofm(did1: str) -> ofm:
    did = uuid.UUID(did1)
    return get_ofm(did)

@app.get("/api/{did1}")
def api_get_api(did1: str) -> api:
    did = uuid.UUID(did1)
    return get_api(did)
@app.get("/sr/{did1}")
def api_get_sr(did1: str) -> sr:
    did = uuid.UUID(did1)
    return get_sr(did)

#=== create record
@app.post("/df")
def api_create_df(df_post :df) -> List[df]:
    return create_df(df_post)

@app.post("/dmd")
def api_create_dmd(dmd_post :dmd) -> List[dmd]:
    return create_dmd(dmd_post)

@app.post("/ifm")
def api_create_ifm(ifm_post :ifm) -> List[ifm]:
    return create_ifm(ifm_post)

@app.post("/ofm")
def api_create_ofm(ofm_post :ofm) -> List[ofm]:
    return create_ofm(ofm_post)

@app.post("/api")
def api_create_api(api_post :api) -> List[api]:
    return create_api(api_post)

@app.post("/sr")
def api_create_sr(sr_post :sr) -> List[sr]:
    return create_sr(sr_post)

# update record

@app.put("/df/{did}")
def api_update_df(did: str,  df_put:df) -> df:
    if did != df_put.fileGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_df(df_put)

@app.put("/dmd/{did}")
def api_update_dmd(did: str,  dmd_put:dmd) -> dmd:
    if did != dmd_put.fileMetaDataGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_dmd(dmd_put)

@app.put("/ifm/{did}")
def api_update_ifm(did: str,  ifm_put:ifm) -> ifm:
    if did != ifm_put.inputFormatGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_ifm(ifm_put)

@app.put("/ofm/{did}")
def api_update_ofm(did: str,  ofm_put:ofm) -> ofm:
    if did != ofm_put.outputFormatGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_ofm(ofm_put)

@app.put("/api/{did}")
def api_update_api(did: str,  api_put:api) -> api:
    if did != api_put.apiGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_api(api_put)

@app.put("/sr/{did}")
def api_update_sr(did: str,  sr_put:sr) -> sr:
    if did != sr_put.searchGuid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_sr(sr_put)

# delete record

@app.delete("/df/{did1}")
def api_delete_df(did1: str):
    did = uuid.UUID(did1)
    delete_df(did)

@app.delete("/dmd/{did1}")
def api_delete_dmd(did1: str):
    did = uuid.UUID(did1)
    delete_dmd(did)

@app.delete("/ifm/{did1}")
def api_delete_ifm(did1: str):
    did = uuid.UUID(did1)
    delete_ifm(did)

@app.delete("/ofm/{did1}")
def api_delete_ofm(did1: str):
    did = uuid.UUID(did1)
    delete_ofm(did)

@app.delete("/api/{did1}")
def api_delete_api(did1: str):
    did = uuid.UUID(did1)
    delete_api(did)

@app.delete("/sr/{did1}")
def api_delete_sr(did1: str):
    did = uuid.UUID(did1)
    delete_sr(did)
