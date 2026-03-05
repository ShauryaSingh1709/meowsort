# MeowSort 😺

![PyPI](https://img.shields.io/pypi/v/meowsort)
![Python](https://img.shields.io/pypi/pyversions/meowsort)
![License](https://img.shields.io/github/license/ShauryaSingh1709/meowsort)
![Downloads](https://img.shields.io/pypi/dm/meowsort)

A lightweight Python sorting utility that automatically selects the best algorithm for your dataset.

The goal of this library is to provide a minimal, easy-to-use sorting tool for developers and students.

---

## Links

📦 PyPI: https://pypi.org/project/meowsort/  
💻 GitHub: https://github.com/ShauryaSingh1709/meowsort  

---
## Features

* Simple and clean API
* Automatic algorithm selection
* Supports any comparable Python data type
* Lightweight with no external dependencies
* Safe error handling

---

## Installation

Install directly from PyPI:

```bash
pip install meowsort
```
[![Install](https://img.shields.io/badge/install-pip%20install%20meowsort-blue)](https://pypi.org/project/meowsort/)

Verify installation:

```bash
pip show meowsort
```

---

## Quick Start

```python
from meowsort import sort_array

data = [5, 3, 9, 1]

sorted_data = sort_array(data)

print(sorted_data)
```

Output:

```
[1, 3, 5, 9]
```

---

## Sorting Different Data Types

The library works with any comparable data type.

### Numbers

```python
from meowsort import sort_array

numbers = [8, 2, 6, 1]

print(sort_array(numbers))
```

Output

```
[1, 2, 6, 8]
```

### Strings

```python
from meowsort import sort_array

words = ["banana", "apple", "orange"]

print(sort_array(words))
```

Output

```
['apple', 'banana', 'orange']
```

---

## Error Handling

The library validates input and raises clear exceptions if invalid data is provided.

Example:

```python
from meowsort import sort_array

sort_array(None)
```

Raises:

```
InvalidInputError
```

---

## Algorithms Used

MeowSort currently includes:

* Bubble Sort — optimized for small datasets
* Quick Sort — used for larger datasets

The algorithm is selected automatically based on the size of the input.

---

## Requirements

* Python 3.8 or newer

---

## Project Structure

```
meowsort
│
├── meowsort
│   ├── __init__.py
│   ├── sorter.py
│   ├── algorithms.py
│   └── exceptions.py
│
├── tests
│   └── test_basic.py
│
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Author

**Shaurya Singh**

---

## License

This project is released under the MIT License.
