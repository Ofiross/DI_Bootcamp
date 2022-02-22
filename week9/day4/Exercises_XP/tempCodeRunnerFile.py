
    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)
