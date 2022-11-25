# pylint: disable=import-error
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from fastapi_pagination import Page, paginate, add_pagination, Params
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from typing import Optional
from db import SessionLocal, Plan
from schema import planner, sortOption, filterOption


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
    response_model=Page[planner],
    status_code=status.HTTP_200_OK,
)
async def get_user(params: Params = Depends(), db: Session = Depends(get_db)):

    """
    ## get plan data with pagenation based on pagenumber and max-page size
    This requires the following
    ```
            page number:int
            max-page-size:int
    ```
    """
    return paginate(db.query(Plan).all(), params)


add_pagination(router)


# get planning data with search
# filter based on isUnassigned including paginantion
@router.get("/filter", response_model=Page[planner], status_code=status.HTTP_200_OK)
async def filter_user_Unassignment(
    filter_query: Optional[filterOption],
    params: Params = Depends(),
    db: Session = Depends(get_db),
):

    """
    ## get plan data filtered by user unassignment status including pagenation based on pagenumber and max-page size
    This requires the following
    ```
            unassignment-status:select-option (bool)
            page number:int
            max-page-size:int
    ```
    """
    if not filter_query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="input filter query"
        )
    if filter_query is filterOption.false:
        items = db.query(Plan).filter(Plan.isUnassigned.is_(False)).all()
        return paginate(items, params)
    if filter_query is filterOption.true:
        items = db.query(Plan).filter(Plan.isUnassigned.is_(True)).all()
        return paginate(items, params)


add_pagination(router)


# get planning data with sorting
# sort in ascending or descending order based on totalHours including paginantion
@router.get("/sort", response_model=Page[planner], status_code=status.HTTP_200_OK)
async def sort_user_totalHours(
    sort_query: Optional[sortOption],
    params: Params = Depends(),
    db: Session = Depends(get_db),
):

    """
    ## get plan data sorted by user totalHours in descending or ascending order including pagenation based on pagenumber and max-page size
    This requires the following
    ```
            totalHours:select-option
            page number:int
            max-page-size:int
    ```
    """
    if not sort_query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="input sort query"
        )
    if sort_query is sortOption.asc:
        items = db.query(Plan).order_by(asc(Plan.totalHours)).all()
    if sort_query is sortOption.desc:
        items = db.query(Plan).order_by(desc(Plan.totalHours)).all()
    if sort_query is sortOption.NONE:
        items = db.query(Plan).filter(Plan.totalHours).all()
    return paginate(items, params)


add_pagination(router)
