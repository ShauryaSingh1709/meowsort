from typing import Iterable, List, TypeVar

from .algorithms import bubble_sort, quick_sort
from .exceptions import InvalidInputError

T = TypeVar("T")


def sort_array(data: Iterable[T]) -> List[T]:
    if data is None:
        raise InvalidInputError("Input cannot be None")

    if not isinstance(data, Iterable):
        raise InvalidInputError("Input must be iterable")

    try:
        arr = list(data)
    except TypeError as exc:
        raise InvalidInputError("Input cannot be converted to a list") from exc

    if len(arr) == 0:
        return []

    try:
        if len(arr) < 32:
            return bubble_sort(arr)
        return quick_sort(arr)
    except TypeError as exc:
        raise InvalidInputError(
            "Elements in the iterable must be comparable"
        ) from exc