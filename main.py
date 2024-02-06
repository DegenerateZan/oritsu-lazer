from api.router import init_routes
import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()
init_routes(app)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
# 	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
# 	logging.error(f"{request}: {exc_str}")
# 	content = {'status_code': 10422, 'message': exc_str, 'data': None}
# 	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)