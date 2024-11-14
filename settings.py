import os

MAIN_URL = os.environ.get("EMNIFY_SDK_API_ENDPOINT_URL", "https://cdn.emnify.net/api")
TOKEN = os.environ.get("EMNIFY_SDK_APPLICATION_TOKEN", os.environ.get("APP_TOKEN"))
