
import pytest
from process import process


@pytest.mark.statement_coverage
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),
    ],
)
def test_statement_coverage(values, expected):
    assert process(values) == expected


@pytest.mark.branch_coverage
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, -1], ["positivo", "par"]),
    ],
)
def test_branch_coverage(values, expected):
    assert process(values) == expected
