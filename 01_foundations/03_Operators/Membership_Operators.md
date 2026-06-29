# Membership Operators in Python

Membership operators are used to check whether a value or element exists in a sequence or collection. They search for an item in objects such as strings, lists, tuples, sets, and dictionaries, and always return either `True` or `False`.

## Membership Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `in` | Returns `True` if the element exists in the collection | `'a' in "apple"` | `True` |
| `not in` | Returns `True` if the element does not exist in the collection | `'z' not in "apple"` | `True` |

## Example

```python
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

print("Orange" not in fruits)
print("Banana" not in fruits)
```

### Output

```text
True
False
True
False
```

## Membership Operators with Strings

```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)
```

### Output

```text
True
False
True
```

## Membership Operators with Dictionaries

> By default, membership operators check **keys**, not values.

```python
student = {
    "name": "Abhishek",
    "age": 21,
    "course": "B.Tech"
}

print("name" in student)
print("Abhishek" in student)

print("Abhishek" in student.values())
```

### Output

```text
True
False
True
```

## Key Points

- `in` checks whether an element exists in a collection.
- `not in` checks whether an element does **not** exist in a collection.
- Membership operators return only `True` or `False`.
- They work with strings, lists, tuples, sets, dictionaries, and other iterable objects.
- In dictionaries, `in` checks **keys** by default. Use `.values()` to search values.

## Real-World Uses

- Checking whether a username exists in a database.
- Verifying if a word is present in a sentence.
- Searching for products in an inventory list.
- Validating permissions or roles in an application.
- Filtering and validating user input.