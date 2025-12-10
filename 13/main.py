from fastapi import APIRouter, status, Response

router = APIRouter()

@router.post("/", status.HTTP)