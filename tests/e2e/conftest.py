import os

import pytest
from substrateinterface import SubstrateInterface

from robonomicsinterface.classes.account import Account
from robonomicsinterface.constants import TYPE_REGISTRY
from helpers import is_local_dev_chain

DEFAULT_E2E_RPC_URL = "ws://127.0.0.1:9944"


@pytest.fixture(scope="session")
def e2e_rpc_url():
    return os.environ.get("ROBONOMICS_E2E_RPC_URL", DEFAULT_E2E_RPC_URL)


@pytest.fixture(scope="session")
def e2e_substrate(e2e_rpc_url):
    try:
        interface = SubstrateInterface(
            url=e2e_rpc_url,
            ss58_format=32,
            type_registry_preset="substrate-node-template",
            type_registry=TYPE_REGISTRY,
        )
        interface.init_runtime()
    except Exception as exc:
        pytest.skip(
            f"Local Robonomics e2e node is not available at {e2e_rpc_url}: {exc}"
        )

    if not is_local_dev_chain(interface.chain):
        pytest.skip(
            f"Refusing to run write e2e tests against non-dev chain: {interface.chain}"
        )

    yield interface
    interface.close()


@pytest.fixture
def e2e_alice(e2e_rpc_url):
    return Account(
        seed=os.environ.get("ROBONOMICS_E2E_ALICE_SEED", "//Alice"),
        remote_ws=e2e_rpc_url,
    )


@pytest.fixture
def e2e_bob(e2e_rpc_url):
    return Account(
        seed=os.environ.get("ROBONOMICS_E2E_BOB_SEED", "//Bob"),
        remote_ws=e2e_rpc_url,
    )
