
** Make Migration **
```
alembic revision -m "migration_name"
```

** Migrate **
```
alembic upgrade head
```

** Run **
```
uvicorn app.main:app --reload
```