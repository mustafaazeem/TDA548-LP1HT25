class Kepler:
    def __init__(self):
        self.obs = {}

    def observe(self, planet_name, angle, time):
        self.obs.setdefault(planet_name, [])
        # self.obs[planet_name].append((angle, time))
        temp_list = self.obs[planet_name]
        temp_list.append((angle, time))

        print(self.obs)

def main():
    solar_system = Kepler()
    solar_system.observe('mars', 2.3, 0)
    solar_system.observe('mars', 2.5, 23)

    solar_system.observe('jupiter', 3.6, 45)

    # solar_system.

main()