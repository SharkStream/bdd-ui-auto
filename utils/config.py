import os
import yaml
from helpers.constants import CONFIG_YAML


def load_config():
    if os.path.exists(CONFIG_YAML):
        with open(CONFIG_YAML, 'r') as f:
            return yaml.safe_load(f)
    return {}
