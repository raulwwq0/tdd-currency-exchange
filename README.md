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
