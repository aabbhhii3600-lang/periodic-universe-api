import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

# Element data — matches your elements.ts exactly
ELEMENTS = [
    {"atomic_number": 1,  "symbol": "H",  "name": "Hydrogen",     "category": "nonmetal",              "period": 1, "group_number": 1,    "block": "s", "atomic_mass": 1.008,   "standard_state": "gas",     "xpos": 1,  "ypos": 1, "bohr_shells": [1]},
    {"atomic_number": 2,  "symbol": "He", "name": "Helium",        "category": "noble-gas",             "period": 1, "group_number": 18,   "block": "s", "atomic_mass": 4.003,   "standard_state": "gas",     "xpos": 18, "ypos": 1, "bohr_shells": [2]},
    {"atomic_number": 3,  "symbol": "Li", "name": "Lithium",       "category": "alkali-metal",          "period": 2, "group_number": 1,    "block": "s", "atomic_mass": 6.941,   "standard_state": "solid",   "xpos": 1,  "ypos": 2, "bohr_shells": [2,1]},
    {"atomic_number": 4,  "symbol": "Be", "name": "Beryllium",     "category": "alkaline-earth-metal",  "period": 2, "group_number": 2,    "block": "s", "atomic_mass": 9.012,   "standard_state": "solid",   "xpos": 2,  "ypos": 2, "bohr_shells": [2,2]},
    {"atomic_number": 5,  "symbol": "B",  "name": "Boron",         "category": "metalloid",             "period": 2, "group_number": 13,   "block": "p", "atomic_mass": 10.811,  "standard_state": "solid",   "xpos": 13, "ypos": 2, "bohr_shells": [2,3]},
    {"atomic_number": 6,  "symbol": "C",  "name": "Carbon",        "category": "nonmetal",              "period": 2, "group_number": 14,   "block": "p", "atomic_mass": 12.011,  "standard_state": "solid",   "xpos": 14, "ypos": 2, "bohr_shells": [2,4]},
    {"atomic_number": 7,  "symbol": "N",  "name": "Nitrogen",      "category": "nonmetal",              "period": 2, "group_number": 15,   "block": "p", "atomic_mass": 14.007,  "standard_state": "gas",     "xpos": 15, "ypos": 2, "bohr_shells": [2,5]},
    {"atomic_number": 8,  "symbol": "O",  "name": "Oxygen",        "category": "nonmetal",              "period": 2, "group_number": 16,   "block": "p", "atomic_mass": 15.999,  "standard_state": "gas",     "xpos": 16, "ypos": 2, "bohr_shells": [2,6]},
    {"atomic_number": 9,  "symbol": "F",  "name": "Fluorine",      "category": "halogen",               "period": 2, "group_number": 17,   "block": "p", "atomic_mass": 18.998,  "standard_state": "gas",     "xpos": 17, "ypos": 2, "bohr_shells": [2,7]},
    {"atomic_number": 10, "symbol": "Ne", "name": "Neon",          "category": "noble-gas",             "period": 2, "group_number": 18,   "block": "p", "atomic_mass": 20.180,  "standard_state": "gas",     "xpos": 18, "ypos": 2, "bohr_shells": [2,8]},
    {"atomic_number": 11, "symbol": "Na", "name": "Sodium",        "category": "alkali-metal",          "period": 3, "group_number": 1,    "block": "s", "atomic_mass": 22.990,  "standard_state": "solid",   "xpos": 1,  "ypos": 3, "bohr_shells": [2,8,1]},
    {"atomic_number": 12, "symbol": "Mg", "name": "Magnesium",     "category": "alkaline-earth-metal",  "period": 3, "group_number": 2,    "block": "s", "atomic_mass": 24.305,  "standard_state": "solid",   "xpos": 2,  "ypos": 3, "bohr_shells": [2,8,2]},
    {"atomic_number": 13, "symbol": "Al", "name": "Aluminum",      "category": "post-transition-metal", "period": 3, "group_number": 13,   "block": "p", "atomic_mass": 26.982,  "standard_state": "solid",   "xpos": 13, "ypos": 3, "bohr_shells": [2,8,3]},
    {"atomic_number": 14, "symbol": "Si", "name": "Silicon",       "category": "metalloid",             "period": 3, "group_number": 14,   "block": "p", "atomic_mass": 28.085,  "standard_state": "solid",   "xpos": 14, "ypos": 3, "bohr_shells": [2,8,4]},
    {"atomic_number": 15, "symbol": "P",  "name": "Phosphorus",    "category": "nonmetal",              "period": 3, "group_number": 15,   "block": "p", "atomic_mass": 30.974,  "standard_state": "solid",   "xpos": 15, "ypos": 3, "bohr_shells": [2,8,5]},
    {"atomic_number": 16, "symbol": "S",  "name": "Sulfur",        "category": "nonmetal",              "period": 3, "group_number": 16,   "block": "p", "atomic_mass": 32.065,  "standard_state": "solid",   "xpos": 16, "ypos": 3, "bohr_shells": [2,8,6]},
    {"atomic_number": 17, "symbol": "Cl", "name": "Chlorine",      "category": "halogen",               "period": 3, "group_number": 17,   "block": "p", "atomic_mass": 35.453,  "standard_state": "gas",     "xpos": 17, "ypos": 3, "bohr_shells": [2,8,7]},
    {"atomic_number": 18, "symbol": "Ar", "name": "Argon",         "category": "noble-gas",             "period": 3, "group_number": 18,   "block": "p", "atomic_mass": 39.948,  "standard_state": "gas",     "xpos": 18, "ypos": 3, "bohr_shells": [2,8,8]},
    {"atomic_number": 19, "symbol": "K",  "name": "Potassium",     "category": "alkali-metal",          "period": 4, "group_number": 1,    "block": "s", "atomic_mass": 39.098,  "standard_state": "solid",   "xpos": 1,  "ypos": 4, "bohr_shells": [2,8,8,1]},
    {"atomic_number": 20, "symbol": "Ca", "name": "Calcium",       "category": "alkaline-earth-metal",  "period": 4, "group_number": 2,    "block": "s", "atomic_mass": 40.078,  "standard_state": "solid",   "xpos": 2,  "ypos": 4, "bohr_shells": [2,8,8,2]},
    {"atomic_number": 26, "symbol": "Fe", "name": "Iron",          "category": "transition-metal",      "period": 4, "group_number": 8,    "block": "d", "atomic_mass": 55.845,  "standard_state": "solid",   "xpos": 8,  "ypos": 4, "bohr_shells": [2,8,14,2]},
    {"atomic_number": 29, "symbol": "Cu", "name": "Copper",        "category": "transition-metal",      "period": 4, "group_number": 11,   "block": "d", "atomic_mass": 63.546,  "standard_state": "solid",   "xpos": 11, "ypos": 4, "bohr_shells": [2,8,18,1]},
    {"atomic_number": 47, "symbol": "Ag", "name": "Silver",        "category": "transition-metal",      "period": 5, "group_number": 11,   "block": "d", "atomic_mass": 107.868, "standard_state": "solid",   "xpos": 11, "ypos": 5, "bohr_shells": [2,8,18,18,1]},
    {"atomic_number": 79, "symbol": "Au", "name": "Gold",          "category": "transition-metal",      "period": 6, "group_number": 11,   "block": "d", "atomic_mass": 196.967, "standard_state": "solid",   "xpos": 11, "ypos": 6, "bohr_shells": [2,8,18,32,18,1]},
    {"atomic_number": 92, "symbol": "U",  "name": "Uranium",       "category": "actinide",              "period": 7, "group_number": None, "block": "f", "atomic_mass": 238.029, "standard_state": "solid",   "xpos": 6,  "ypos": 9, "bohr_shells": [2,8,18,32,21,9,2]},
]

def seed():
    db = SessionLocal()
    try:
        existing = db.query(models.ElementModel).count()
        if existing > 0:
            print(f"Database already has {existing} elements. Skipping seed.")
            return

        for el in ELEMENTS:
            db_element = models.ElementModel(**el)
            db.add(db_element)

        db.commit()
        print(f"Successfully seeded {len(ELEMENTS)} elements.")
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed()