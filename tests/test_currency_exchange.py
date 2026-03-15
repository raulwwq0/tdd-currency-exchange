"""
Test suite for CurrencyExchange class

Follow TDD principles:
1. Write a failing test (Red)
2. Write minimal code to pass (Green)
3. Refactor and improve (Refactor)

Example test structure for workshop participants:
"""

from src.currency_exchange import CurrencyExchange


class TestCurrencyExchange:
    """Test suite for CurrencyExchange class."""

    def test_currency_exchange_can_be_instantiated(self):
        """Test that we can create a CurrencyExchange instance."""
        exchange = CurrencyExchange()
        assert exchange is not None

    # TODO: Add more tests following TDD approach
    # Example ideas:
    # - test_convert_same_currency
    # - test_convert_usd_to_eur
    # - test_convert_with_invalid_currency
    # - test_get_exchange_rate
    # - test_set_exchange_rate
