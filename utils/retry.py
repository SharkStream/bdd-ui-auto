import time
import functools
from typing import Callable, TypeVar, Any
from utils.logger import log_warning

T = TypeVar("T")


def retry_on_failure(
    max_retries: int = 3,
    base_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (Exception,),
) -> Callable:
    """Decorator for retrying flaky operations with exponential backoff."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        delay = base_delay * (backoff_factor ** attempt)
                        log_warning(
                            f"Attempt {attempt + 1}/{max_retries + 1} for "
                            f"{func.__name__} failed: {e}. Retrying in {delay:.1f}s..."
                        )
                        time.sleep(delay)
            raise last_exception  # type: ignore[misc]

        return wrapper

    return decorator
