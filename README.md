# practice-pydantic-fastapi

A practice project for learning Pydantic and FastAPI basics.

## What this covers

- Request/response schema validation with Pydantic
- `Field` constraints (length, range, pattern)
- Excluding fields from responses with `Field(exclude=True)`
- Grouping query parameters into a Pydantic model using `Depends()`

## Run

```bash
uvicorn main:app --reload
```

API docs available at `http://127.0.0.1:8000/docs`

## Notes

See [docs/pydantic.md](docs/pydantic.md) for a detailed breakdown of Pydantic features used in this project.
