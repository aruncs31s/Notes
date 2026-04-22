---
id: 12-Testing-Patterns
tags:
  - python
  - testing
  - assertions
dg-publish: true
---

# Testing Patterns

Common assertions used in pytest tests.

## Assert Equality

```python
assert result == expected
```

## Assert Truthy/Falsy

```python
assert result
assert not result
```

## Assert in Collection

```python
assert item in list
assert key in dict
```

## Assert Type

```python
assert isinstance(result, list)
```

## Assert Exception

```python
with pytest.raises(ValueError):
    function_that_raises()
```

---

**See Also:** [[00-Setup]] - Getting started with pytest