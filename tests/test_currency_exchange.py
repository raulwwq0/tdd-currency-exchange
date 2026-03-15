"""
Test suite for CurrencyExchange class

Follow TDD principles:
1. Write a failing test (Red)
2. Write minimal code to pass (Green)
3. Refactor and improve (Refactor)

Example test structure for workshop participants:
"""

import pytest
from src.currency_exchange import CurrencyExchange


class TestCurrencyExchange:
    """Test suite for CurrencyExchange class."""

    def test_currency_exchange_can_be_instantiated(self):
        """Test that we can create a CurrencyExchange instance."""
        exchange = CurrencyExchange()
        assert exchange is not None

    def test_convert_same_currency(self):
        """Test converting an amount when both currencies are the same."""
        exchange = CurrencyExchange()
        result = exchange.convert(100, "USD", "USD")
        assert result == 100

    def test_set_exchange_rate(self):
        """Test setting an exchange rate between two currencies."""
        exchange = CurrencyExchange()
        exchange.set_exchange_rate("USD", "EUR", 0.85)
        # If no exception is raised, the test passes

    def test_get_exchange_rate(self):
        """Test retrieving a previously set exchange rate."""
        exchange = CurrencyExchange()
        exchange.set_exchange_rate("USD", "EUR", 0.85)
        rate = exchange.get_exchange_rate("USD", "EUR")
        assert rate == 0.85

    def test_convert_usd_to_eur(self):
        """Test converting USD to EUR using the exchange rate."""
        exchange = CurrencyExchange()
        exchange.set_exchange_rate("USD", "EUR", 0.85)
        result = exchange.convert(100, "USD", "EUR")
        assert result == 85.0

    def test_convert_with_invalid_currency(self):
        """Test that converting without a set exchange rate raises an exception."""
        exchange = CurrencyExchange()
        with pytest.raises(ValueError, match="Exchange rate not found"):
            exchange.convert(100, "JPY", "GBP")
