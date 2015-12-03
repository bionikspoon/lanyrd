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
    from lanyrd.lanyrd import lanyrd

    mock_lanyrd = lanyrd()
    return mock_lanyrd


def test_lanyrd_properly_mocked(lanyrd):
    assert str(lanyrd) == "Success"
