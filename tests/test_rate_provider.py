"""
Test suite for StaticRateProvider class

Follow TDD principles:
1. Write a failing test (Red)
2. Write minimal code to pass (Green)
3. Refactor and improve (Refactor)

Example test structure for workshop participants:
"""

from src.rate_provider import StaticRateProvider


class TestStaticRateProvider:
    """Test suite for StaticRateProvider class."""

    def test_static_rate_provider_can_be_instantiated(self):
        """Test that we can create a StaticRateProvider instance."""
        provider = StaticRateProvider()
        assert provider is not None

    # TODO: Add more tests following TDD approach
    # Example ideas:
    # - test_get_rate_returns_correct_value
    # - test_get_rate_unknown_pair_raises_value_error
    # - test_get_rate_is_case_insensitive
    # - test_empty_provider_raises_value_error
    # - test_get_rate_same_currency_returns_one
