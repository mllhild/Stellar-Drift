class Orbit:
    def __init__(self, radius, angle, angular_speed, radial_speed, orbit_center):
        """
        Initialize an Orbit instance.

        :param radius: Current radius of the orbit
        :param angle: Current angular position in radians
        :param angular_speed: Angular speed in radians per time unit
        :param radial_speed: Radial speed (change of radius per time unit)
        :param orbit_center: The object this orbit revolves around
        """
        self.radius = float(radius)
        self.angle = float(angle)
        self.angular_speed = float(angular_speed)
        self.radial_speed = float(radial_speed)
        self.orbit_center = orbit_center

    def __repr__(self):
        return (f"Orbit(radius={self.radius}, angle={self.angle}, angular_speed={self.angular_speed}, "
                f"radial_speed={self.radial_speed}, orbit_center={repr(self.orbit_center)})")
