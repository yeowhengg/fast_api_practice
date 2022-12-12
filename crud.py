from sqlalchemy.orm import Session

from . import models, schemas

import json

def get_artifact(db: Session, artifact_name: str):
    return db.query(models.Genshin_Item).filter(models.Genshin_Item.name == artifact_name).first()

def insert_item(db: Session, new_artifact:schemas.GenshinItem):
    insertted_artifact = models.Genshin_Item(**new_artifact.dict())
    db.add(insertted_artifact)
    db.commit()
    db.refresh(insertted_artifact)
    return insertted_artifact

def update_item(db: Session, update_artifact: schemas.UpdateItem):
    item_to_update = db.query(models.Genshin_Item).filter(models.Genshin_Item.name == update_artifact.name).first()
    item_to_update.level += update_artifact.level
    
    db.commit()
    db.refresh(item_to_update)
    return item_to_update

def get_items(db: Session):
    all_items = db.query(models.Genshin_Item).all()
    response = {"all_artifacts":[{}]}
    for i in all_items:
        key = i.__dict__
        response['all_artifacts'][0][key['name']] = {"id":key['id'], "name":key['name'], "element":key['element'], "level":key['level']}
    return response

def get_artifact_by_level(artifact_level: int, db: Session):
    response = {"all_artifacts":[{}]}
    returned_items = db.query(models.Genshin_Item).filter(models.Genshin_Item.level == artifact_level).all()
    
    for i in returned_items:
        key = i.__dict__
        response['all_artifacts'][0][key['name']] = {"id":key['id'], "name":key['name'], "element":key['element'], "level":key['level']}
    return response

def delete_artifact_by_name(artifact_name: str, db: Session):
    artifact_to_delete = db.query(models.Genshin_Item).filter(models.Genshin_Item.name == artifact_name).first()
    db.delete(artifact_to_delete)
    db.commit()
    
    return artifact_to_delete




    
    
    
    
