from sqlalchemy import Column, Integer, String, Float, Boolean, ARRAY, Text
from database import Base

class ElementModel(Base):
    __tablename__ = "elements"

    id = Column(Integer, primary_key=True, index=True)
    atomic_number = Column(Integer, unique=True, nullable=False)
    symbol = Column(String(3), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    category = Column(String(30))
    period = Column(Integer)
    group_number = Column(Integer, nullable=True)
    block = Column(String(1))
    atomic_mass = Column(Float)
    standard_state = Column(String(10))
    xpos = Column(Integer)
    ypos = Column(Integer)
    bohr_shells = Column(ARRAY(Integer))

class ElementPropertyModel(Base):
    __tablename__ = "element_properties"

    id = Column(Integer, primary_key=True, index=True)
    atomic_number = Column(Integer, unique=True, nullable=False)
    electronic_config = Column(String(100))
    electronegativity = Column(Float, nullable=True)
    atomic_radius = Column(Float, nullable=True)
    ionization_energy = Column(Float, nullable=True)
    melting_point = Column(Float, nullable=True)
    boiling_point = Column(Float, nullable=True)
    density = Column(Float, nullable=True)
    oxidation_states = Column(ARRAY(Integer))
    all_ionization_energies = Column(ARRAY(Float))