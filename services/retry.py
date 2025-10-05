import time, requests
from typing import Optional

class HttpFailure(Exception): ...
def _retryable(status: int) -> bool:
    return status in (408, 425, 429, 500, 502, 503, 504)

def retry_request(method: str, url: str, *, max_tries: int = 3, backoff_base: float = 0.98, **kwargs) -> requests.Response:
    last_exc: Optional[Exception] = None
    for attempt in range(1, max_tries + 1):
        try:
            resp = requests.request(method, url, timeout=kwargs.pop("timeout", 15), **kwargs)
            if resp.status_code < 400:
                return resp
            if not _retryable(resp.status_code) or attempt == max_tries:
                raise HttpFailure(f"{method} {url} failed: {resp.status_code} {resp.text[:500]}")
        except Exception as exc:
            last_exc = exc
            if attempt == max_tries:
                raise
        time.sleep(backoff_base * (2 ** (attempt - 1)))
    raise HttpFailure(f"unreachable: {last_exc}")

