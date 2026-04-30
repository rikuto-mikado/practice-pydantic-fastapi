# Pydantic Field Guide

This document summarizes common parameters used in Pydantic's `Field` for validation and metadata.

## Required vs. Optional Fields

### `...` (Ellipsis)
The ellipsis `...` indicates that a field is **required**. Pydantic will raise a validation error if the field is missing from the input data.

```python
username: str = Field(..., min_length=3)  # Required
```

### `None` or Default Values
Providing `None` or a specific value makes the field **optional**.

```python
age: int = Field(None)  # Optional, defaults to None
status: str = Field("active")  # Optional, defaults to "active"
```

## Numerical Constraints

These parameters are used to restrict the range of numeric types (`int`, `float`).

| Parameter | Meaning | Comparison |
| :--- | :--- | :--- |
| `gt` | Greater Than | `> ` |
| `ge` | Greater than or Equal to | `>= ` |
| `lt` | Less Than | `< ` |
| `le` | Less than or Equal to | `<= ` |

**Example:**
```python
# Age must be between 0 and 120 (inclusive)
age: int = Field(..., ge=0, le=120)
```

## String Constraints

Parameters used to validate string lengths and patterns.

| Parameter | Meaning |
| :--- | :--- |
| `min_length` | Minimum number of characters |
| `max_length` | Maximum number of characters |
| `pattern` | Regular expression (regex) to match |

**Example:**
```python
# Username must be between 3 and 50 characters
username: str = Field(..., min_length=3, max_length=50)
```

## Metadata

| Parameter | Meaning |
| :--- | :--- |
| `title` | A human-readable title for the field |
| `description` | A detailed description of the field (used in OpenAPI/Swagger) |
| `examples` | List of example values |

**Example:**
```python
description: str = Field(
    None, 
    description="A brief bio of the user",
    examples=["I love coding in Python!"]
)
```
