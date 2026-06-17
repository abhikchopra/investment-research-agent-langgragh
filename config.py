import os

from dotenv import load_dotenv

import vertexai

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION
)