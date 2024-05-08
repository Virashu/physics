from __future__ import annotations


class Vector:
    """2D vector"""

    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vector:
        return Vector(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other)

    __rtruediv__ = __truediv__

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    @property
    def tuple(self) -> tuple[float, float]:
        return (self.x, self.y)

    @property
    def length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self) -> Vector:
        if self.length == 0:
            return self
        return self / self.length
