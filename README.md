# ...

A module i made to better understand physics

---

Environment

- Variables
  - Gravity
  - Temperature

Bodies

- Variables
  - Acceleration
  - Mass
  - Velocity
  - Position
  - Force
  - Size
- Actions
  - Move
  - Collide
  - Change state

## Diagram

```mermaid
classDiagram

materialPoint <-- solidBody

class materialPoint {
  position
  velocity
  acceleration
  mass
  force

  move()
}

class solidBody {
  size
  material
  shape

  collision()
}

```
