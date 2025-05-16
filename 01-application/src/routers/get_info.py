
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from models import HostInfo

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def index():
    info = HostInfo.from_env()

    return f"""
    <html>
        <head><title>Host Info</title></head>
        <body>
            <h2>Host Info</h2>
            <ul>
                <li><strong>Hostname:</strong> {info.hostname}</li>
                <li><strong>IP Address:</strong> {info.ip_address}</li>
                <li><strong>Author:</strong> {info.author}</li>
            </ul>
        </body>
    </html>
    """
