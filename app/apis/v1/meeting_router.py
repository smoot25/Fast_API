from fastapi import APIRouter
from app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(
    prefix="/v1/edgedb/meetings", tags=["Meeting"], redirect_slashes=False
)
mysql_router = APIRouter(
    prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False
)


@edgedb_router.post("", description="meeting 생성")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post("", description="meeting 생성")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
