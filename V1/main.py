from classes.stellarObject import StellarObject


sun = StellarObject(name="Sun")
earth = StellarObject(name="Earth", orbits=sun)
moon = StellarObject(name="Moon", orbits=earth)


# Display structure
print(sun)
print("Orbiters of Sun:", sun.orbiters)
print("Orbiters of Earth:", earth.orbiters)