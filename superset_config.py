CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": "localhost",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 1,
    "CACHE_REDIS_URL": "redis://localhost:6379/1",
}
FILTER_STATE_CACHE_CONFIG = {**CACHE_CONFIG, "CACHE_KEY_PREFIX": "superset_filter_"}
EXPLORE_FORM_DATA_CACHE_CONFIG = {**CACHE_CONFIG, "CACHE_KEY_PREFIX": "superset_explore_form_"}
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset:superset@localhost:5432/superset"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "blabla1212"
ENABLE_PROXY_FIX = True