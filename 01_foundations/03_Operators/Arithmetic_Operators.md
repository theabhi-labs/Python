# Arithmetic Operators in Python

Arithmetic operators are used to perform mathematical calculations on numeric values. They allow you to add, subtract, multiply, divide, find remainders, calculate powers, and perform floor division. These operators are commonly used in mathematical expressions, algorithms, data processing, and everyday programming tasks.

## Arithmetic Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division (Returns float) | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation (Power) | `2 ** 3` | `8` |

## Example

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
```

### Output

```text
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000
```

## Key Points

- `+` is used to add two values.
- `-` subtracts one value from another.
- `*` multiplies two numbers.
- `/` always returns a floating-point (`float`) result.
- `//` returns only the integer part of the division.
- `%` returns the remainder after division.
- `**` raises a number to the power of another number.

## Real-World Uses

- Performing mathematical calculations.
- Calculating discounts, taxes, and percentages.
- Finding even or odd numbers using the modulus operator (`%`).
- Computing powers and scientific calculations.
- Determining page numbers or chunk sizes using floor division (`//`).