# Identity Operators in Python

Identity operators are used to check whether two variables refer to the **same object in memory**, not whether they have the same value. They compare the identity (memory reference) of objects and always return either `True` or `False`.

> **Note:** Identity operators compare **object identity**, whereas comparison operators (`==`) compare **object values**.

## Identity Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `is` | Returns `True` if both variables refer to the same object | `a is b` | `True` or `False` |
| `is not` | Returns `True` if both variables refer to different objects | `a is not b` | `True` or `False` |

## Example

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b      :", a is b)
print("a == b      :", a == b)

print("a is c      :", a is c)
print("a == c      :", a == c)

print("a is not c  :", a is not c)
```

### Output

```text
a is b      : True
a == b      : True
a is c      : False
a == c      : True
a is not c  : True
```

## Key Points

- `is` checks whether two variables point to the **same object** in memory.
- `is not` checks whether two variables point to **different objects**.
- `==` compares **values**, while `is` compares **memory references**.
- Identity operators are commonly used to compare objects with `None`.

## Real-World Uses

- Checking whether a variable is `None`.
- Determining if two variables reference the same object.
- Debugging object references in memory.
- Working with mutable objects like lists, dictionaries, and custom classes.
- Optimizing programs where object identity is important.

## `is` vs `==`

| Operator | Checks |
|----------|--------|
| `==` | Whether the **values** of two objects are equal |
| `is` | Whether both variables refer to the **same object** in memory |

### Example

```python
x = [10, 20]
y = [10, 20]
z = x

print(x == y)   # True (same values)
print(x is y)   # False (different objects)

print(x == z)   # True
print(x is z)   # True (same object)
```