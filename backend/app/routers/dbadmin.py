from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from ..db import engine, get_session
from ..deps import get_current_superuser

router = APIRouter()

class SQLQuery(BaseModel):
    sql: str

@router.get("/tables")
def list_tables(current=Depends(get_current_superuser)):
    with engine.connect() as conn:
        res = conn.execute(text("SHOW TABLES"))
        return [row[0] for row in res.fetchall()]

@router.post("/query")
def run_query(q: SQLQuery, current=Depends(get_current_superuser)):
    sql = q.sql.strip()
    if not sql.lower().startswith("select"):
        raise HTTPException(status_code=400, detail="Only SELECT queries are allowed")
    with engine.connect() as conn:
        res = conn.execute(text(sql))
        cols = res.keys()
        rows = [dict(zip(cols, r)) for r in res.fetchall()]
        return {"columns": cols, "rows": rows}
