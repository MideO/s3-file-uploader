from unittest.mock import MagicMock, patch

import pytest

from s3fileuploader.src.utils.lock import Lock, LockAlreadyAcquiredError

pytest.locks = {}


def insert_lock_side_effect(name, value, **kwargs):
    pytest.locks[name] = value


def delete_lock_side_effect(name):
    del pytest.locks[name]


@pytest.fixture(autouse=True)
def clear_lock():
    pytest.locks = {}


def test_lock_created_with_context_manager():
    redis = MagicMock()
    a_lock = "lock"
    redis.set.side_effect = insert_lock_side_effect
    redis.delete.side_effect = delete_lock_side_effect
    redis.get.side_effect = lambda _: None

    with Lock(a_lock, redis):
        assert a_lock in pytest.locks
    assert a_lock not in pytest.locks


def test_lock_cannot_be_created_when_lock_exist():
    a_lock = "lock"

    redis = MagicMock()
    redis.set.side_effect = insert_lock_side_effect
    redis.delete.side_effect = delete_lock_side_effect
    redis.get.side_effect = lambda x: pytest.locks.get(x)

    with pytest.raises(LockAlreadyAcquiredError) as ex:
        with Lock(a_lock, redis):
            with Lock(a_lock, redis):
                raise AssertionError("lock incorrectly acquired")

    assert f"lock: {a_lock} already exist" in str(ex.value)
