# Test suite

The default test run is offline:

```bash
poetry run pytest
```

Disabling plugin autoload keeps the suite isolated from unrelated pytest
plugins installed globally on a developer machine. It is configured for the
project in `pyproject.toml`.

Read-only checks against the live Robonomics Polkadot RPC endpoint must be
marked with `@pytest.mark.integration` and enabled explicitly:

```bash
poetry run pytest --run-integration -m integration
```

Tests that submit extrinsics must target an explicitly configured local node,
use `@pytest.mark.e2e`, and be enabled explicitly:

```bash
poetry run pytest --run-e2e -m e2e
```

Keep tests in these groups:

- `unit/`: pure logic and mocked wrapper behavior.
- `contract/`: offline runtime metadata fixtures and SCALE contract checks.
- `integration/`: read-only live Polkadot RPC smoke tests.
- `e2e/`: local-node write workflows.
- `fixtures/`: runtime metadata and stable test payloads.
