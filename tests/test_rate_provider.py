"""
Test suite for StaticRateProvider class

Follow TDD principles:
1. Write a failing test (Red)
2. Write minimal code to pass (Green)
3. Refactor and improve (Refactor)

Example test structure for workshop participants:
"""

import pytest

from src.rate_provider import StaticRateProvider


@pytest.fixture
def provider():
    """A StaticRateProvider pre-loaded with a small rates table."""
    return StaticRateProvider(
        {
            ("USD", "EUR"): 0.92,
            ("EUR", "USD"): 1.09,
            ("GBP", "USD"): 1.27,
        }
    )


class TestStaticRateProvider:
    """Test suite for StaticRateProvider class."""

    def test_static_rate_provider_can_be_instantiated(self):
        """Test that we can create a StaticRateProvider instance."""
        provider = StaticRateProvider()
        assert provider is not None

    def test_get_rate_returns_correct_value(self, provider):
        """get_rate should return the rate set at construction."""
        assert provider.get_rate("USD", "EUR") == pytest.approx(0.92)

    def test_get_rate_unknown_pair_raises_value_error(self, provider):
        """get_rate should raise ValueError for a pair not in the table."""
        with pytest.raises(ValueError):
            provider.get_rate("JPY", "GBP")

    def test_get_rate_is_case_insensitive(self, provider):
        """Currency codes should be normalised before lookup."""
        assert provider.get_rate("usd", "eur") == pytest.approx(0.92)

    def test_empty_provider_raises_value_error(self):
        """A provider with no rates should raise ValueError for any pair."""
        empty = StaticRateProvider()
        with pytest.raises(ValueError):
            empty.get_rate("USD", "EUR")

    def test_get_rate_same_currency_returns_one(self):
        """Converting a currency to itself should always yield rate 1.0."""
        provider = StaticRateProvider()
        assert provider.get_rate("USD", "USD") == 1.0
