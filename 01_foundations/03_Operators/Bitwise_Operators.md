# Bitwise Operators in Python

Bitwise operators perform operations directly on the **binary (bit-level)** representation of integers. They compare or manipulate individual bits and are commonly used in low-level programming, performance optimization, embedded systems, networking, operating systems, and cybersecurity.

> **Note:** Before using bitwise operators, it is helpful to understand how decimal numbers are represented in binary.

## Bitwise Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&` | Bitwise AND | `5 & 3` |
| `\|` | Bitwise OR | `5 \| 3` |
| `^` | Bitwise XOR | `5 ^ 3` |
| `~` | Bitwise NOT (One's Complement) | `~5` |
| `<<` | Left Shift | `5 << 1` |
| `>>` | Right Shift | `5 >> 1` |

## Binary Representation

```text
Decimal  Binary

5        0101
3        0011
```

---

## 1. Bitwise AND (`&`)

Returns `1` only if **both bits are 1**.

```python
print(5 & 3)
```

```text
Binary

0101
0011
----
0001

Result: 1
```

---

## 2. Bitwise OR (`|`)

Returns `1` if **at least one bit is 1**.

```python
print(5 | 3)
```

```text
Binary

0101
0011
----
0111

Result: 7
```

---

## 3. Bitwise XOR (`^`)

Returns `1` only if **the bits are different**.

```python
print(5 ^ 3)
```

```text
Binary

0101
0011
----
0110

Result: 6
```

---

## 4. Bitwise NOT (`~`)

Flips every bit (0 becomes 1 and 1 becomes 0).

```python
print(~5)
```

```text
Result: -6
```

> Python uses **two's complement** representation for signed integers, which is why `~5` evaluates to `-6`.

---

## 5. Left Shift (`<<`)

Shifts all bits to the left by the specified number of positions.

```python
print(5 << 1)
```

```text
0101

↓

1010

Result: 10
```

Each left shift by one position is equivalent to multiplying by **2**.

---

## 6. Right Shift (`>>`)

Shifts all bits to the right by the specified number of positions.

```python
print(5 >> 1)
```

```text
0101

↓

0010

Result: 2
```

Each right shift by one position is approximately equivalent to integer division by **2**.

---

## Complete Example

```python
a = 5
b = 3

print("AND       :", a & b)
print("OR        :", a | b)
print("XOR       :", a ^ b)
print("NOT       :", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
```

### Output

```text
AND        : 1
OR         : 7
XOR        : 6
NOT        : -6
Left Shift : 10
Right Shift: 2
```

## Key Points

- Bitwise operators work only with integer values.
- They perform operations on individual binary bits.
- `&` returns `1` only when both bits are `1`.
- `|` returns `1` if at least one bit is `1`.
- `^` returns `1` when the bits are different.
- `~` inverts all bits using two's complement representation.
- `<<` shifts bits left (approximately multiplying by 2 for each shift).
- `>>` shifts bits right (approximately dividing by 2 for each shift).

## Real-World Uses

- Setting, clearing, and toggling permission flags.
- Network programming and subnet mask calculations.
- Cryptography and cybersecurity.
- Embedded systems and hardware programming.
- Performance optimization using bit manipulation.
- Solving coding interview and competitive programming problems.