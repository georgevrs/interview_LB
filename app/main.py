from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models import Company, SessionLocal  # Import your models and session

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/company/{gemh_number}")
def read_company(gemh_number: str, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.gemh_number == gemh_number).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

