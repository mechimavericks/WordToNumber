# Word to Number Converter

A Python library to convert word representations of numbers to their numerical values. The library supports multiple number systems:

- American number system (million, billion)
- Indian and Nepali number system (lakh, crore)

## Installation

```
pip install WordToNumber
```

## Usage

```python
from word_to_number import word_to_num

# American system
print(word_to_num('two million five hundred thousand'))  # 2500000

# Indian system
print(word_to_num('two crore fifty lakh'))  # 25000000

# Extended system with arba
print(word_to_num('one arba two crore'))  # 1020000000

# With decimals
print(word_to_num('one hundred point five'))  # 100.5
```

## Features

- Supports American number system: thousand, million, billion
- Supports Indian number system: thousand, lakh/lac, crore
- Supports extended number system with arba
- Handles decimal numbers
- Validates correct ordering of number words
- Prevents mixing of different number systems
- Processes hyphenated words and extra spaces

## Error Handling

The library provides clear error messages for:
- Incorrect word order
- Missing intermediary units
- Mixing different number systems
- Invalid input types
- Redundant number words

## License

MIT

Inspire from : https://github.com/akshaynagpal/w2n
