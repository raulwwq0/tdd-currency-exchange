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

    def test_convert_usd_to_eur(self, exchange):
        """Should convert USD to EUR using the injected provider rate."""
        result = exchange.convert(100, "USD", "EUR")
        assert result == pytest.approx(92.0)

    def test_convert_eur_to_usd(self, exchange):
        """Should convert EUR to USD using the injected provider rate."""
        result = exchange.convert(50, "EUR", "USD")
        assert result == pytest.approx(54.5)

    def test_convert_same_currency_ignores_provider(self, exchange):
        """Same-currency conversion should return the original amount."""
        result = exchange.convert(200, "USD", "USD")
        assert result == 200

    def test_convert_unsupported_pair_raises_value_error(self, exchange):
        """Provider raises ValueError for a pair not in the rates table."""
        with pytest.raises(ValueError):
            exchange.convert(100, "JPY", "GBP")
