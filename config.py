"""Configuration helpers for the Module 11 laboratory."""

from __future__ import annotations

import os


def get_api_key() -> str:
    return os.getenv("MEDILINK_API_KEY", "local-demo-key")


def get_request_timeout() -> int:
    raw = os.getenv("REQUEST_TIMEOUT", "5")
    try:
        value = int(raw)
    except ValueError:
        raise ValueError("REQUEST_TIMEOUT must be an integer")
    if value <= 0:
        raise ValueError("REQUEST_TIMEOUT must be greater than zero")
    return value
