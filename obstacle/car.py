import pyray as rl
import math


class Circle:
    def __init__(self, positions, speed):
        self.positions = positions
        self.speed = speed
        self.frames_per_segment = []
        self.current_segment = 0
        self.frame = 0
        self.current_position = positions[0]
        self.calculate_frames_per_segment()

    def calculate_frames_per_segment(self):
        for i in range(len(self.positions) - 1):
            p1 = self.positions[i]
            p2 = self.positions[i + 1]
            distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
            frames = max(1, int(distance / self.speed))
            self.frames_per_segment.append(frames)

    def update(self):
        if self.current_segment < len(self.frames_per_segment):
            if self.frame < self.frames_per_segment[self.current_segment]:
                p1 = self.positions[self.current_segment]
                p2 = self.positions[self.current_segment + 1]
                alpha = self.frame / self.frames_per_segment[self.current_segment]
                x = (1 - alpha) * p1[0] + alpha * p2[0]
                y = (1 - alpha) * p1[1] + alpha * p2[1]
                self.current_position = (x, y)
                self.frame += 1
            else:
                self.current_segment += 1
                self.frame = 0

    def draw(self):
        rl.draw_circle(int(self.current_position[0]), int(self.current_position[1]), 20, rl.DARKBLUE)