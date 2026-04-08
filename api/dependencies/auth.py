from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.security_service import SecurityService

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = SecurityService.decode_jwt_token(token)
        return payload
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
