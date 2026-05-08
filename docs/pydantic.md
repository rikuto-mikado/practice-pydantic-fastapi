# Pydantic Overview

A summary of Pydantic features used in this project.

---

## 1. BaseModel

```python
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    age: int
```

- Inheriting from `BaseModel` enables automatic type checking and validation
- Passing a value with the wrong type raises a `ValidationError`
- When used with FastAPI, the request body is automatically parsed and converted into this model

---

## 2. Field — Fine-grained validation constraints

```python
from pydantic import Field

username: str = Field(..., min_length=3, max_length=50)
age: int = Field(None, ge=0, le=120)
limit: int = Field(10, ge=1, le=100)
order_by: str = Field("created_at", pattern="^(created_at|updated_at)$")
```

| Argument | Meaning |
|---|---|
| `...` | Required field |
| `None` or a value | Default value (optional) |
| `min_length` / `max_length` | String length constraint |
| `ge` / `le` | Numeric range (greater than or equal / less than or equal) |
| `gt` / `lt` | Numeric range (strictly greater / strictly less) |
| `pattern` | Regex-based validation |

---

## 3. EmailStr — Email address validation

```python
from pydantic import EmailStr

email: EmailStr
```

- Using `EmailStr` instead of `str` automatically validates the email format
- `taro@example.com` passes; `not-an-email` raises a `ValidationError`

---

## 4. Field(exclude=True) — Exclude fields from response

```python
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str = Field(exclude=True)
```

- `exclude=True` removes the field from `model_dump()` and serialization output
- Combined with FastAPI's `response_model`, sensitive data like password hashes can be kept out of the response

Actual response:
```json
{
  "id": 1,
  "username": "taro123",
  "email": "taro@example.com"
}
```
`hashed_password` is not included.

---

## 5. model_dump() — Convert model to dictionary

```python
filters.model_dump()
```

- Converts model fields into a `dict`
- Fields with `exclude=True` are also excluded here
- Used in `GET /items` to return the `FilterParams` contents directly as a response

---

## 6. Config / from_attributes

```python
class UserResponse(BaseModel):
    class Config:
        from_attributes = True
```

- `from_attributes = True` allows model instantiation from ORM objects (e.g. SQLAlchemy) in addition to dicts
- Intended for use with `UserResponse.model_validate(orm_object)`
- Not actively used yet since data is currently created from dicts, but required when integrating with a database

---

## 7. Depends() — Group query parameters into a model

```python
# schemas/params.py
class FilterParams(BaseModel):
    limit: int = Field(10, ge=1, le=100)
    offset: int = Field(0, ge=0)
    order_by: str = Field("created_at", pattern="^(created_at|updated_at)$")

# main.py
@app.get("/items")
def list_items(filters: FilterParams = Depends()):
    return {"filters": filters.model_dump()}
```

- `Depends()` allows query parameters to be grouped and received as a Pydantic model
- Parameters are passed via query string: `GET /items?limit=20&offset=0&order_by=updated_at`
- Field constraints are enforced as usual

---

## Validation Error Example

Sending a request that violates a constraint returns a 422:

```json
// username is 2 characters (violates min_length=3)
{
  "username": "ab",
  "email": "taro@example.com"
}
```

Response:
```json
{
  "detail": [
    {
      "loc": ["body", "username"],
      "msg": "String should have at least 3 characters",
      "type": "string_too_short"
    }
  ]
}
```
