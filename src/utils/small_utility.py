import os
import os.path

from dotenv import load_dotenv


# TODO: Impl proper error handling
def get_env_token(req_token):
    # Check if .env file is present & at least one environment variable is set.
    if load_dotenv() is False:
        print(".env file is not present, shutting down...")
        exit(1)

    # Check if specified .env token is present in .env file
    token = os.getenv(req_token)
    if token is None:
        print("Couldnt find requested token in .env, shutting down...")
        exit(1)

    return token
