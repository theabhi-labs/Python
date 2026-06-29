# Comparison Operators in Python

Comparison operators are used to compare two values or expressions. They evaluate the relationship between the operands and always return a Boolean value: `True` or `False`. These operators are commonly used in conditional statements, loops, and decision-making logic.

## Comparison Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equal to | `10 == 10` | `True` |
| `!=` | Not equal to | `10 != 5` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal to | `10 >= 10` | `True` |
| `<=` | Less than or equal to | `10 <= 5` | `False` |

## Example

```python
a = 10
b = 20

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
```

### Output

```text
a == b : False
a != b : True
a > b  : False
a < b  : True
a >= b : False
a <= b : True
```

## Key Points

- Comparison operators always return either `True` or `False`.
- They are mainly used to make decisions in a program.
- These operators can compare numbers, strings, and other comparable objects.
- They are commonly used with `if`, `elif`, `else`, `while`, and other control flow statements.

## Real-World Uses

- Checking user login credentials.
- Verifying age eligibility.
- Comparing product prices.
- Validating input values.
- Making decisions in applications, such as granting or denying access based on conditions.