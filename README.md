# Currency Exchange TDD Workshop

This is a hands-on Test-Driven Development (TDD) workshop using Python and pytest.

## Setup

### 1. Create virtual environment and install dependencies

```bash
make setup
```

### 2. Activate the virtual environment

```bash
source .venv/bin/activate
```

## Running Tests

### Run all tests

```bash
make test
```

### Run tests in watch mode (auto-rerun on file changes)

```bash
make test-watch
```

### Run tests with coverage report

```bash
make coverage
```

## Code Quality

### Lint code with ruff

```bash
make lint
```

### Auto-fix linting issues

```bash
make lint-fix
```

### Format code with ruff

```bash
make format
```

### Check formatting without changes

```bash
make format-check
```

### Type check with pyright

```bash
make typecheck
```

### Run all checks (lint + format-check + typecheck)

```bash
make check
```

## Workshop Structure

- `src/` - Source code directory
- `tests/` - Test files directory

## TDD Workflow

1. **Red**: Write a failing test
2. **Green**: Write the minimum code to make the test pass
3. **Refactor**: Improve the code while keeping tests green

## Available Make Commands

Run `make help` to see all available commands.

## Workshop Exercise: Currency Exchange

Build a currency exchange system following TDD principles. Start with simple conversions and gradually add more features.

### Suggested Test Cases (in order of complexity)

Follow the TDD cycle for each test case below:

#### 1. Test Convert Same Currency

**Goal**: Convert an amount when both currencies are the same.

**Example**: Converting 100 USD to USD should return 100 USD.

**Learning**: This is the simplest case - helps establish the basic `convert()` method signature.

#### 2. Test Set Exchange Rate

**Goal**: Allow setting an exchange rate between two currencies.

**Example**: Set the exchange rate from USD to EUR at 0.85.

**Learning**: Introduces the concept of storing exchange rates in the system.

#### 3. Test Get Exchange Rate

**Goal**: Retrieve a previously set exchange rate.

**Example**: After setting USD to EUR at 0.85, getting the rate should return 0.85.

**Learning**: Validates that exchange rates are stored correctly.

#### 4. Test Convert USD to EUR

**Goal**: Convert an amount from one currency to another using the exchange rate.

**Example**: Converting 100 USD to EUR with rate 0.85 should return 85 EUR.

**Learning**: Implements the core conversion logic using stored rates.

#### 5. Test Convert with Invalid Currency

**Goal**: Handle conversions when exchange rate is not available.

**Example**: Attempting to convert JPY to GBP without setting a rate should raise an exception.

**Learning**: Introduces error handling and edge cases.

### TDD Tips

- Write only ONE test at a time
- Run the test and watch it fail (Red)
- Write the minimal code to make it pass (Green)
- Refactor if needed, keeping tests green
- Commit after each green test
- Move to the next test only when current test is passing

---

## Workshop Exercise: Rate Provider

### Overview

`src/rate_provider.py` contains two classes that form the foundation of a pluggable rate-fetching system:

| Class                | Purpose                                                                    |
| -------------------- | -------------------------------------------------------------------------- |
| `RateProvider`       | Abstract base class — defines the contract every provider must fulfil      |
| `StaticRateProvider` | Concrete stub backed by an in-memory dict — **your implementation target** |

### The `RateProvider` contract

```python
class RateProvider(ABC):
    @abstractmethod
    def get_rate(self, from_currency: str, to_currency: str) -> float:
        """Return the exchange rate from from_currency to to_currency."""
```

Any object that inherits from `RateProvider` and implements `get_rate` can be used as a drop-in rate source.

### Step 1 — Implement `StaticRateProvider.get_rate`

Open `src/rate_provider.py` and replace the `NotImplementedError` stub with real logic:

```python
def get_rate(self, from_currency: str, to_currency: str) -> float:
    pair = (from_currency.upper(), to_currency.upper())
    if pair not in self._rates:
        raise ValueError(f"No rate available for {from_currency} -> {to_currency}")
    return self._rates[pair]
```

Follow TDD: write a failing test first, then add the code above, then refactor.

### Step 2 — Integrate `RateProvider` with `CurrencyExchange`

Update `CurrencyExchange` to accept an optional provider at construction time:

```python
from src.rate_provider import RateProvider

class CurrencyExchange:
    def __init__(self, rate_provider: RateProvider | None = None):
        self._rate_provider = rate_provider

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency == to_currency:
            return amount
        rate = self._rate_provider.get_rate(from_currency, to_currency)
        return amount * rate
```

The provider is injected via the constructor — `CurrencyExchange` never needs to know where the rates come from.

### Step 3 — Write integration tests

Integration tests verify that `CurrencyExchange` and a `RateProvider` work correctly **together**.
Open `tests/test_integration.py` — a fixture is already provided. Add tests inside `TestCurrencyExchangeWithRateProvider` following the TDD cycle.

### Suggested provider test cases (unit level)

Drive these with TDD before writing the integration tests above:

1. **`test_get_rate_returns_correct_value`** — provider returns the rate set at construction.
2. **`test_get_rate_unknown_pair_raises_value_error`** — provider raises `ValueError` for unsupported pairs.
3. **`test_get_rate_is_case_insensitive`** — `"usd"` and `"USD"` resolve to the same rate.
4. **`test_empty_provider_raises_value_error`** — a provider initialised with no rates raises for any pair.
