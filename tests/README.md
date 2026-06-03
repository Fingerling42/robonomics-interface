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

## Runtime metadata fixtures

Contract tests under `tests/contract/` run against every fixture matching:

```bash
tests/fixtures/metadata/robonomics_spec_*.json
```

Export the currently live runtime metadata with:

```bash
poetry run python tools/export_robonomics_metadata_fixture.py
```

Export an expected runtime version, failing if the connected block has a
different `specVersion`:

```bash
poetry run python tools/export_robonomics_metadata_fixture.py --spec-version 42
```

When the live runtime has moved on, pass a historical block:

```bash
poetry run python tools/export_robonomics_metadata_fixture.py --spec-version 42 --block-hash 0x...
```

To validate a freshly exported fixture without copying it into the repository:

```bash
poetry run python tools/export_robonomics_metadata_fixture.py --output-dir /tmp/robonomics-metadata
ROBONOMICS_METADATA_FIXTURE_DIR=/tmp/robonomics-metadata poetry run pytest tests/contract
```
