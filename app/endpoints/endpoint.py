from fastapi import APIRouter, status, Depends
from fastapi_pagination import Page, LimitOffsetPage, paginate, add_pagination
from sqlalchemy.orm import Session
from db import SessionLocal, Plan
from schema import planner


# create endpoint router instance
router = APIRouter(prefix="/planner", tags=["Planner"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get planning data with paginetion
# @router.get("/", response_model=Page[planner], status_code=status.HTTP_200_OK)
@router.get(
    "/limit-offset",
    response_model=LimitOffsetPage[planner],
    status_code=status.HTTP_200_OK,
)
async def get_user(db: Session = Depends(get_db)):
    return paginate(db.query(Plan).all())


add_pagination(router)


# get planning data with filtering
