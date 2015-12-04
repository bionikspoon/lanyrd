#!/usr/bin/env python
# coding=utf-8

"""
test_lanyrd
----------------------------------

Tests for `lanyrd` module.
"""
import pytest


@pytest.fixture
def lanyrd():
    from lanyrd.lanyrd import Lanyrd

    mock_lanyrd = Lanyrd()
    return mock_lanyrd


def test_lanyrd_properly_mocked(lanyrd):
    assert str(lanyrd) == "Success"
