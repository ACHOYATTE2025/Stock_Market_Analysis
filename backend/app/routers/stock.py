from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from app.services.stock_service import get_stock_data, get_stock_analysis

router = APIRouter()
security = HTTPBearer()

@router.get("/{ticker}", dependencies=[Depends(security)])
def stock(ticker: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return get_stock_data(ticker)

@router.get("/{ticker}/analysis", dependencies=[Depends(security)])
def stock_analysis(ticker: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return get_stock_analysis(ticker)