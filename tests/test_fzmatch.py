import pytest

from . import context
from sicsearch.fzmatch import fzmatch


def test_fuzzy_match():
    match, _ = fzmatch('abc', 'abc')
    assert match == 'abc'

    match, _ = fzmatch('quickfox', 'quick fox')
    assert match == 'quickfox'

    match, _ = fzmatch('the quick fox', 'fox')
    assert match == '          fox'

    match, _ = fzmatch('the quick fox', 'foxx')
    assert match is None

    match, _ = fzmatch('the quick fox', ' f o x')
    assert match == '          fox'

    match, _ = fzmatch('the quick fox', 'w')
    assert match is None

    match, _ = fzmatch('the quick fox', 'teqckox')
    assert match == 't e q  ck  ox'

    match, _ = fzmatch('quick fox', 'q fox')
    assert match == 'q     fox'

    match, _ = fzmatch('quick fox', 'q k')
    assert match == 'q   k    '

