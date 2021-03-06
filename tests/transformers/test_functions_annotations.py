import pytest
from py_backwards.transformers.functions_annotations import FunctionsAnnotationsTransformer


@pytest.mark.parametrize('before, after', [
    ('def fn(x: T) -> List[T]:\n    return [x]',
     'def fn(x):\n    return [x]'),
    ('def fn(x: int) -> float:\n    return 1.5',
     'def fn(x):\n    return 1.5')])
def test_transform(transform, before, after):
    assert transform(FunctionsAnnotationsTransformer, before) == after


@pytest.mark.parametrize('code, result', [
    ('def fn(x: T) -> List[T]:\n    return [x]; fn(10)', [10]),
    ('def fn(x: int) -> float:\n    return 1.5; fn(10)', 1.5)])
def test_run(run_transformed, code, result):
    assert run_transformed(FunctionsAnnotationsTransformer, code) == result
