import os
import json
from systems.solar_system import SolarSystem
from entities.planet import Planet
from entities.wormhole import Wormhole

class GalaxyMap:
    def __init__(self):
        self.systems = {}              # Key: system name, Value: SolarSystem object
        self.current_system = None     # The active system the player is in

    def add_system(self, name, system):
        self.systems[name] = system
        if self.current_system is None:
            self.current_system = system  # Set first added system as default

    def get_system(self, name):
        return self.systems.get(name)

    def switch_system(self, name):
        if name in self.systems:
            print(f"Switching to {name}")
            self.current_system = self.systems[name]
        else:
            print(f"System '{name}' not found!")

    def update(self, spaceship):
        if self.current_system:
            self.current_system.update(spaceship)

    def draw(self, screen):
        if self.current_system:
            self.current_system.draw(screen)

    def get_current_system_name(self):
        for name, system in self.systems.items():
            if system == self.current_system:
                return name
        return "Unknown"

    def load_from_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                full_path = os.path.join(folder_path, filename)
                with open(full_path, "r") as f:
                    data = json.load(f)

                name = data.get("name", os.path.splitext(filename)[0])
                center = tuple(data.get("center", [800, 450]))  # default center

                solar_system = SolarSystem(name=name, center=center)

                for p in data.get("planets", []):
                    planet = Planet(
                        orbit_center=center,
                        name=p.get("name", "Planet"),
                        image_index=p.get("image_index", 0),
                        radius=p.get("radius", 50),
                        orbit_radius=p.get("orbit_radius", 200),
                        orbit_angle=p.get("orbit_angle", 0),
                        orbit_angular_speed=p.get("orbit_angular_speed", 0.01),
                        rotation_speed=p.get("rotation_speed", 0.1),
                    )
                    solar_system.add_planet(planet)

                for w in data.get("wormholes", []):
                    wormhole = Wormhole(
                        x=w["x"],
                        y=w["y"],
                        destination=w["destination"]
                    )
                    solar_system.add_wormhole(wormhole)

                self.add_system(name, solar_system)