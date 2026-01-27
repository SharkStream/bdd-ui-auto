import os.path
from utils.common import read_json_file, wrap_namespace

PRO_DIR = os.getcwd()

RESOURCES = os.path.join(PRO_DIR, 'resources')
CONFIG_YAML = os.path.join(RESOURCES, 'config.yaml')

REPORTS = os.path.join(PRO_DIR, 'reports')
SCREENSHOTS_DIR = os.path.join(REPORTS, 'screenshots')
WORKER_DIR = os.path.join(REPORTS, 'workers')
ALLURE_RESULTS_DIR = os.path.join(REPORTS, 'allure-results')

# Tracing
TRACES_DIR = os.path.join(REPORTS, "traces")
TRACES_VIDEOS_DIR = os.path.join(TRACES_DIR, "videos")

# Env Config
ENV_CONFIG_JSON = wrap_namespace(read_json_file(os.path.join(RESOURCES, "generic", 'env.json')))
ENDPOINTS_CONFIG_JSON = wrap_namespace(read_json_file(os.path.join(RESOURCES, "generic", 'endpoints.json')))
USERS_CONFIG_JSON = wrap_namespace(read_json_file(os.path.join(RESOURCES, "generic", 'login.json')))