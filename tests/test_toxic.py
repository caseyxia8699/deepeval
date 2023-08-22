"""Tests for toxic
"""


import pytest
from deepeval.metrics.toxic_classifier import NonToxicMetric, assert_non_toxic
from .utils import assert_viable_score

generated_text = "Winners of the FIFA world cup were the French national football team"


@pytest.mark.asyncio
async def test_non_toxic():
    assert_non_toxic(
        text="Who won the FIFA World Cup in 2018?",
    )


@pytest.mark.asyncio
async def test_non_toxic_2():
    with pytest.raises(AssertionError):
        assert_non_toxic(
            text="You are stupid!",
        )


@pytest.mark.asyncio
async def test_overall_score_metric():
    metric = NonToxicMetric()
    score = metric.measure(text=generated_text)
    assert metric.is_successful(), "Overall score metric not working"
    assert_viable_score(score)
