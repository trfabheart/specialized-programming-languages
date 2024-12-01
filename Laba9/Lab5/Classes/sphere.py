import math
from Classes.shape3d import Shape3D

class Sphere(Shape3D):
    def __init__(self, size):
        super().__init__(size)

    def project_to_2d(self):
        projection_height = self.size * 2
        projection_width = self.size * 2
        projection = [[" " for _ in range(projection_width * 2)] for _ in range(projection_height)]
        segments = 12
        for i in range(segments):
            for j in range(segments):
                theta = 2 * math.pi * i / segments
                phi = math.pi * j / segments
                x = int(self.size * math.sin(phi) * math.cos(theta))
                y = int(self.size * math.sin(phi) * math.sin(theta))
                z = int(self.size * math.cos(phi))
                rotated_x, rotated_y, rotated_z = self.apply_rotation(x, y, z)
                self.plot_point(rotated_x + self.size, rotated_y + self.size, projection)

        return projection