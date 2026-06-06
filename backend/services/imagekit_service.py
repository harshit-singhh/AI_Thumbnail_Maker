
from imagekitio import ImageKit
from config import IMAGEKIT_PRIVATE_KEY, IMAGEKIT_URL_ENDPOINT

imagekit = ImageKit(private_key = IMAGEKIT_PRIVATE_KEY)

def upload_file(file_bytes:bytes , file_name:str , folder:str , content_type:str = "image/png") -> str:

    """Upload file to imagekit and return the CDN URL"""

    result = imagekit.files.upload(
        file = (file_bytes , file_name , content_type ),
        file_name = file_name,
        folder = folder,
        is_private_file = False,
        use_unique_file_name= True,
     )
    
    return result.url


def get_variants(base_url : str) -> dict:
    """Return 3 sizes variants URLs using imagekit transformations."""