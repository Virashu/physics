from __future__ import annotations

from .material_point import MaterialPoint
from .typing import TupleVec
from .utils import rect_intersect
from .vector import Vector


class SolidBody(MaterialPoint):
    """2D solid body"""

    size: Vector

    def __init__(
        self,
        size: Vector | TupleVec,
        position: Vector | TupleVec,
        velocity: Vector | TupleVec = (0, 0),
        acceleration: Vector | TupleVec = (0, 0),
        mass: float = 0,
        *,
        anchored: bool = False,
    ):
        super().__init__(
            position,
            velocity,
            acceleration,
            mass,
        )

        if isinstance(size, tuple):
            size = Vector(*size)
        self.size = size
        self.anchored = anchored

        if not anchored and mass == 0:
            raise AttributeError

    def collide(self, other: SolidBody):
        if not rect_intersect(
            (
                self.position.x,
                self.position.y,
                self.position.x + self.size.x,
                self.position.y + self.size.y,
            ),
            (
                other.position.x,
                other.position.y,
                other.position.x + other.size.x,
                other.position.y + other.size.y,
            ),
        ):
            return

        v1 = self.velocity
        v2 = other.velocity

        m1 = self.mass
        m2 = other.mass

        new_v = (m1 * v1 + m2 * v2) / (m1 + m2)

        self.velocity = new_v
        other.velocity = new_v

    def collide_bounce(self, other: SolidBody) -> None:
        if not rect_intersect(
            (
                self.position.x,
                self.position.y,
                self.position.x + self.size.x,
                self.position.y + self.size.y,
            ),
            (
                other.position.x,
                other.position.y,
                other.position.x + other.size.x,
                other.position.y + other.size.y,
            ),
        ):
            return

        if self.anchored or other.anchored:
            other.velocity = other.velocity * -1
            self.velocity = self.velocity * -1

            return

        self_kinetic = self.kinetic
        other_kinetic = self.kinetic

        common_kinetic = self_kinetic + other_kinetic

        # self_k = self.mass / (self.mass + other.mass)
        # other_k = other.mass / (self.mass + other.mass)

        # self_kinetic_new = common_kinetic * self_k
        # other_kinetic_new = common_kinetic * other_k

        avg_kinetic = common_kinetic / 2

        self_kinetic_new = other_kinetic_new = avg_kinetic

        collision_vector = (other.velocity + self.velocity).normalize() * -1

        self.velocity = collision_vector * (self_kinetic_new / self.mass) ** 0.5
        other.velocity = -1 * collision_vector * (other_kinetic_new / other.mass) ** 0.5
