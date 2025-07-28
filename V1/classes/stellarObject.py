import numpy as np

class StellarObject:
    def __init__(self, name, position=None, velocity=None, acceleration=None, orbits=None):
        """
        Initialize a StellarObject.

        :param name: Unique name or identifier for the object
        :param position: 3D position vector (numpy array)
        :param velocity: 3D velocity vector (numpy array)
        :param acceleration: 3D acceleration vector (numpy array)
        :param orbits: StellarObject this object orbits, or None
        """
        self.name = name
        self.position = np.array(position if position is not None else [0.0, 0.0, 0.0], dtype=float)
        self.velocity = np.array(velocity if velocity is not None else [0.0, 0.0, 0.0], dtype=float)
        self.acceleration = np.array(acceleration if acceleration is not None else [0.0, 0.0, 0.0], dtype=float)
        
        self.orbits = orbits  # The StellarObject this object orbits
        self.orbiters = []    # List of StellarObjects that orbit this one

        if orbits is not None:
            orbits.add_orbiter(self)
            
        self.isOrbiting = False
        
            
    @classmethod
    def empty(cls):
        """Alternative constructor that creates a default StellarObject with no parameters."""
        return cls(name="Unnamed")

    def add_orbiter(self, obj):
        """Add a StellarObject to this object's orbiters list."""
        if obj not in self.orbiters:
            self.orbiters.append(obj)

    def __repr__(self):
        return f"StellarObject(name='{self.name}', position={self.position.tolist()})"
