from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
import models

# Create all tables in database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="PeriodicUniverse API", version="1.0.0")

# Allow Next.js frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://periodic-universe.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "PeriodicUniverse API is running"}

@app.get("/api/v1/elements")
def get_elements(db: Session = Depends(get_db)):
    elements = db.query(models.ElementModel).order_by(
        models.ElementModel.atomic_number
    ).all()
    return elements

@app.get("/api/v1/elements/{atomic_number}")
def get_element(atomic_number: int, db: Session = Depends(get_db)):
    element = db.query(models.ElementModel).filter(
        models.ElementModel.atomic_number == atomic_number
    ).first()
    if not element:
        raise HTTPException(status_code=404, detail="Element not found")
    return element

@app.get("/api/v1/elements/{atomic_number}/properties")
def get_element_properties(atomic_number: int, db: Session = Depends(get_db)):
    props = db.query(models.ElementPropertyModel).filter(
        models.ElementPropertyModel.atomic_number == atomic_number
    ).first()
    if not props:
        raise HTTPException(status_code=404, detail="Properties not found")
    return props

@app.get("/api/v1/trends/{property_name}")
def get_trend(property_name: str, db: Session = Depends(get_db)):
    allowed = [
        "electronegativity", "atomic_radius", "ionization_energy",
        "melting_point", "boiling_point", "density"
    ]
    if property_name not in allowed:
        raise HTTPException(status_code=400, detail="Invalid property name")
    
    results = db.query(
        models.ElementModel.atomic_number,
        models.ElementModel.symbol,
        models.ElementModel.name,
        getattr(models.ElementPropertyModel, property_name)
    ).join(
        models.ElementPropertyModel,
        models.ElementModel.atomic_number == models.ElementPropertyModel.atomic_number
    ).order_by(models.ElementModel.atomic_number).all()
    
    return [
        {
            "atomicNumber": r[0],
            "symbol": r[1],
            "name": r[2],
            "value": r[3]
        }
        for r in results
    ]


@app.get("/api/v1/elements/{atomic_number}/compounds")
def get_element_compounds(atomic_number: int, db: Session = Depends(get_db)):
    from sqlalchemy import text
    result = db.execute(
        text("SELECT * FROM compounds WHERE primary_element_atomic_number = :z ORDER BY compound_class, formula"),
        {"z": atomic_number}
    ).fetchall()
    return [dict(row._mapping) for row in result]