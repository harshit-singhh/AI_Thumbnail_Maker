
import base64
from openai import AsyncOpenAI
from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key = OPENAI_API_KEY)

def generate_thumbnail(prompt :str , style_prompt:str , headshot_url : str ) -> bytes:
      """Use the Response API with gpt-image-2 as a built-in image_generation tool. 
      Pass the headshot URL directly as an input_image.
      
      Returns raw PNG bytes"""

      

