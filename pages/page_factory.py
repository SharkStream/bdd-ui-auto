from typing import Dict, Type

from .base_page import BasePage
from .input_page import InputPage
from .login_page import LoginPage
from .secure_page import SecurePage


class PageFactory:
    _page_map: Dict[str, Type[BasePage]] = {
        'base': BasePage,
        'login': LoginPage,
        'secure': SecurePage,
        'input': InputPage,
    }

    @classmethod
    def get_page(cls, page_name: str, context) -> BasePage:
        if page_name not in cls._page_map:
            raise ValueError(f"Unknown page: {page_name}. Available: {list(cls._page_map.keys())}")
        return cls._page_map[page_name](context.page, context)
