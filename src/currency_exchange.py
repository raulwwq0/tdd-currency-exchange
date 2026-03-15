"""
Currency Exchange class

This module will contain the currency exchange logic.
Start by writing tests first!
"""

from typing import Optional

from src.rate_provider import RateProvider


class CurrencyExchange:
    """Handle currency conversion operations."""

    def __init__(self, rate_provider: Optional[RateProvider] = None):
        """Initialize the currency exchange."""
        self._rate_provider = rate_provider
