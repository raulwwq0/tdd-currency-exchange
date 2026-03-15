"""
Integration tests — CurrencyExchange + RateProvider working together.

Follow TDD principles:
1. Write a failing test (Red)
2. Write minimal code to pass (Green)
3. Refactor and improve (Refactor)

Example test structure for workshop participants:
"""

import pytest

from src.currency_exchange import CurrencyExchange
from src.rate_provider import StaticRateProvider


@pytest.fixture
def exchange():
    """A CurrencyExchange wired with a StaticRateProvider."""
    rates = {
        ("USD", "EUR"): 0.92,
        ("EUR", "USD"): 1.09,
        ("GBP", "USD"): 1.27,
    }
    provider = StaticRateProvider(rates)
    return CurrencyExchange(rate_provider=provider)


class TestCurrencyExchangeWithRateProvider:
    """Integration test suite for CurrencyExchange + RateProvider."""

    # TODO: Add more tests following TDD approach
    # Example ideas:
    # - test_convert_usd_to_eur
    # - test_convert_eur_to_usd
    # - test_convert_same_currency_ignores_provider
    # - test_convert_unsupported_pair_raises_value_error
