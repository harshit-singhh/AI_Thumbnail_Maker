import asyncio
import logging

from sqlmodel import Session , select

from database import engine
from models import Job , Thumbnail
from services.openai_service import generate_thumbnail
from services.imagekit_service import upload_file

logger = logging.getLogger(__name__)

STLES = {  }
 