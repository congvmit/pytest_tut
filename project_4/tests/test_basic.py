import sys

sys.path.append("..")

import asyncio

import pytest
import pytest_asyncio
from basic import add, sub


@pytest.mark.asyncio
async def test_add():
    assert await add(1, 2) == 3


@pytest.mark.asyncio
async def test_sub():
    assert await sub(3, 4) == -1
