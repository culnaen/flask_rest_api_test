import os

from envparse import env

env_path = f"{os.getcwd()}/.env.example"
env.read_envfile(path=env_path)

PATH_TO_DB = env.str("PATH_TO_DB")
