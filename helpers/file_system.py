import os
from helpers.constants import SCREENSHOTS_DIR, REPORTS, WORKER_DIR, ALLURE_RESULTS_DIR
from utils.logger import log_info_emoji

_shown_messages: set = set()


def create_reports_structure():
    """
    Create the necessary directory structure for reports if they do not exist.
    """
    directories = [REPORTS, SCREENSHOTS_DIR, WORKER_DIR, ALLURE_RESULTS_DIR]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    if "reports_structure" not in _shown_messages:
        log_info_emoji("📁", "Reports directory structure created")
        _shown_messages.add("reports_structure")
