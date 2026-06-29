# Logical Operators in Python

Logical operators are used to combine two or more conditions or Boolean expressions. They evaluate the logical relationship between conditions and always return either `True` or `False`. Logical operators are commonly used in decision-making, conditional statements, loops, and authentication logic.

## Logical Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns `True` if **both** conditions are `True` | `10 > 5 and 20 > 10` | `True` |
| `or` | Returns `True` if **at least one** condition is `True` | `10 > 15 or 20 > 10` | `True` |
| `not` | Reverses the Boolean value | `not(10 > 5)` | `False` |

## Example

```python
a = 10
b = 20

print("and :", a < b and b > 15)
print("or  :", a > b or b > 15)
print("not :", not(a < b))
```

### Output

```text
and : True
or  : True
not : False
```

## Key Points

- `and` returns `True` only if **all** conditions are `True`.
- `or` returns `True` if **at least one** condition is `True`.
- `not` changes `True` to `False` and `False` to `True`.
- Logical operators are frequently used with comparison operators to build complex conditions.

## Real-World Uses

- Validating username **and** password during login.
- Checking if a user is an admin **or** a moderator.
- Verifying whether a student has passed all required subjects.
- Controlling access based on multiple permissions.
- Filtering data using multiple conditions.