from environs import Env

env = Env()
env.read_env()

MONGO_DB_USER=env.str('MONGO_DB_USER')
MONGO_DB_PASSWORD=env.str('MONGO_DB_PASSWORD')
