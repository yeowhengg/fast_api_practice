from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(root_path='/api/v1/')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def first_api(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}

@app.get("/get_artifact_by_name/", response_model=schemas.GenshinItem)
def get_artifact_by_name(artifact_name:str, db: Session = Depends(get_db)):
    artifact_exist = crud.get_artifact(db, artifact_name)
    if artifact_exist is None:
        raise HTTPException(status_code=404, detail="Artifact not found!")
    return artifact_exist

@app.post("/add_artifact/", response_model=schemas.GenshinItem)
def add_artifact(artifact: schemas.AddArtifects, db: Session = Depends(get_db)):
    artifact_exists = crud.get_artifact(db, artifact.name)
    if artifact_exists:
        raise HTTPException(status_code=409, detail="Artifact already exist!")
    return crud.insert_item(db, artifact)

@app.put("/increase_artifact_level/", response_model=schemas.GenshinItem)
def update_artifact_level(item_to_update: schemas.UpdateItem, db: Session = Depends(get_db)):
    artifact_exists = crud.get_artifact(db, item_to_update.name)
    if not artifact_exists:
        return {}

    return crud.update_item(db, item_to_update)

@app.get("/get_all_artifacts")
def get_all_artifacts(db: Session = Depends(get_db)):
    all_artifacts = crud.get_items(db)
    if not all_artifacts:
        return {"all_artifacts": []}
    return all_artifacts

@app.get("/get_artifact_by_level")
def get_artifact_by_level(level: int, db: Session = Depends(get_db)):
    returned_artifacts = crud.get_artifact_by_level(level, db)
    if returned_artifacts is None:
        return {"all_artifacts":[]}
        
    return returned_artifacts

@app.post("/delete_artifact_by_name", response_model=schemas.GenshinItem)
def delete_artifact_by_name(name: str, db: Session = Depends(get_db)):
    artifact_exists = crud.get_artifact(db, name)
    if artifact_exists is None:
        raise HTTPException(status_code=404, detail="Artifact not found")
    deleted_artifact = crud.delete_artifact_by_name(name, db)

    return deleted_artifact
    


