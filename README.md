# 🔢 Word to Number Converter (Multisystem: American, Indian & Nepali)

A simple yet powerful Python package to convert number words into numeric form. Inspired by [w2n by Akshay Nagpal](https://github.com/akshaynagpal/w2n), but extended to support **Indian** and **Nepali** numbering systems such as `lakh`, `crore`, `arba`, and decimals.

---

## ✨ Features

- ✅ Converts words like `five hundred twenty five` into `525`
- ✅ Supports **American system**: `million`, `billion`, `trillion`
- ✅ Supports **Indian/Nepali system**: `lakh`, `crore`, `arba`
- ✅ Handles **decimal points**: `point four five` → `0.45`
- ✅ Easy to integrate into Python applications

---

## 📦 Installation

Install using pip:

```bash
pip install WordToNumber
```
**OR**

Just copy the `WordToNumber.py` file into your project from the Source Code.

---

## 🚀 Usage

```python
from WordToNumber import word_to_num

# American system
print(word_to_num('two million five hundred thousand'))  # 2500000

# Indian system
print(word_to_num('two crore fifty lakh'))  # 25000000

# Extended Nepali system with arba
print(word_to_num('one arba two crore'))  # 1020000000

# Decimal numbers
print(word_to_num('one hundred point five'))  # 100.5
```

---

## 🧠 Supported Vocabulary

### 🔢 Basic Numbers:
- `zero` to `nineteen`
- `twenty`, `thirty`, ..., `ninety`

### 🧱 Place Values:

#### American:
- `hundred`, `thousand`, `million`, `billion`, `trillion`

#### Indian/Nepali:
- `hundred`, `thousand`
- `lakh`, `lac`, `lakhs`
- `crore`, `arba`

#### Decimal:
- `point`

---
<!-- 
## ❗ Error Handling

This package throws meaningful errors for:

- ❌ Mixing different systems (e.g., `two million five crore`)
- ❌ Invalid words or syntax (e.g., `fivety`, `hundred crore lakh`)
- ❌ Repeated place values (`two million one million`)

--- -->

## 🧪 Function Overview

### `word_to_num(number_sentence)`
- Main function to convert a sentence into a number.
- Returns `int` or `float`.

---

## 📄 Example Conversions

| Input                             | Output       |
|----------------------------------|--------------|
| `ten thousand`                   | `10000`      |
| `two crore fifty lakh`           | `25000000`   |
| `one arba two crore`             | `1020000000` |
| `one hundred point five`         | `100.5`      |
| `seventy five lakh twenty one`   | `7500021`    |
| `twelve point zero six seven`    | `12.067`     |

---

## 💡 Inspired By

> [akshaynagpal/w2n](https://github.com/akshaynagpal/w2n) — A minimalistic library for word to number conversion in Python.

This project builds on top of that idea by supporting **regional systems** like Indian and Nepali with added robustness and flexibility.

---

## 🤝 Contributing

We welcome contributions! If you'd like to contribute to this Flutter Package Project, please check out our [Contribution Guidelines](Contribution.md).

---


## 🤗 Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this app.

---

## 🪪 LICENSE
This project is licensed under the MIT [License](LICENSE).


## Author

[Santosh Bhandari](mailto:info@bhandari-santosh.com.np)

---
