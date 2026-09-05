import pytest

from app.store import store


@pytest.fixture(autouse=True)
def reset_store() -> None:
    store.reset()
