from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routers import auth, stock
from app.config.settings import get_jwt_settings
from fastapi_jwt_auth import AuthJWT
from fastapi.middleware.cors import CORSMiddleware

security = HTTPBearer()

app = FastAPI(
    title="Stock Market Analysis API",
    swagger_ui_init_oauth={},
    components={"securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer"}}}
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@AuthJWT.load_config
def get_config():
    return get_jwt_settings()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(stock.router, prefix="/stock", tags=["stock"])