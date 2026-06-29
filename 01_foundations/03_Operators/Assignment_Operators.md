# Assignment Operators in Python

Assignment operators are used to assign values to variables. They not only assign a value but can also perform an operation and update the variable in a single statement. Assignment operators make code shorter, cleaner, and easier to read.

## Assignment Operators

| Operator | Description | Example | Equivalent To |
|----------|-------------|---------|---------------|
| `=` | Assign value | `x = 10` | `x = 10` |
| `+=` | Add and assign | `x += 5` | `x = x + 5` |
| `-=` | Subtract and assign | `x -= 5` | `x = x - 5` |
| `*=` | Multiply and assign | `x *= 5` | `x = x * 5` |
| `/=` | Divide and assign | `x /= 5` | `x = x / 5` |
| `//=` | Floor divide and assign | `x //= 5` | `x = x // 5` |
| `%=` | Modulus and assign | `x %= 5` | `x = x % 5` |
| `**=` | Exponentiate and assign | `x **= 2` | `x = x ** 2` |
| `&=` | Bitwise AND and assign | `x &= y` | `x = x & y` |
| `|=` | Bitwise OR and assign | `x |= y` | `x = x \| y` |
| `^=` | Bitwise XOR and assign | `x ^= y` | `x = x ^ y` |
| `>>=` | Right shift and assign | `x >>= 2` | `x = x >> 2` |
| `<<=` | Left shift and assign | `x <<= 2` | `x = x << 2` |

## Example

```python
x = 10

x += 5
print("After += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

x /= 4
print("After /= :", x)

x //= 2
print("After //= :", x)

x %= 3
print("After %= :", x)

x **= 2
print("After **= :", x)
```

### Output

```text
After += : 15
After -= : 12
After *= : 24
After /= : 6.0
After //= : 3.0
After %= : 0.0
After **= : 0.0
```

## Key Points

- `=` is used to assign a value to a variable.
- Compound assignment operators (`+=`, `-=`, `*=`, etc.) perform an operation and update the variable in a single statement.
- They make code more concise and readable.
- Bitwise assignment operators are commonly used in low-level programming and optimization.

## Real-World Uses

- Updating a user's account balance.
- Increasing or decreasing a counter in loops.
- Tracking scores in games.
- Updating inventory quantities.
- Performing efficient mathematical calculations without writing repetitive code.