from .typing import TupleVec
from .vector import Vector


class MaterialPoint:
    """2D material point"""

    position: Vector
    velocity: Vector
    acceleration: Vector
    mass: float

    def __init__(
        self,
        position: Vector | TupleVec,
        velocity: Vector | TupleVec,
        acceleration: Vector | TupleVec,
        mass: float,
    ):
        if isinstance(position, tuple):
            position = Vector(*position)
        if isinstance(velocity, tuple):
            velocity = Vector(*velocity)
        if isinstance(acceleration, tuple):
            acceleration = Vector(*acceleration)

        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

        self.mass = mass

    def apply_force(self, force: Vector) -> None:
        self.acceleration += force / self.mass

    def update(self, dt: float) -> None:
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

    @property
    def momentum(self) -> Vector:
        return self.velocity * self.mass

    @property
    def kinetic(self) -> float:
        return 0.5 * self.mass * self.velocity.length**2
