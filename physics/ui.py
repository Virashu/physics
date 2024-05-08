import vgame
from . import SolidBody


class UI(vgame.Scene):
    def load(self):
        # middle = (self.width / 2, self.height / 2)
        self.body_1 = SolidBody(
            (20, 20),
            (20, self.height - 20),
            (100, 0),
            (0, 0),
            1,
        )
        self.body_2 = SolidBody(
            (20, 20),
            (self.width / 2, self.height - 20),
            (0, 0),
            (0, 0),
            5,
        )
        self.left_wall = SolidBody((10, self.height), (0, 0), anchored=True)
        self.right_wall = SolidBody(
            (10, self.height), (self.width - 10, 0), anchored=True
        )

    def update(self):
        self.body_1.update(0.01)
        self.body_2.update(0.01)

        self.body_1.collide_bounce(self.body_2)

        self.body_1.collide_bounce(self.left_wall)
        self.body_2.collide_bounce(self.left_wall)

        self.body_1.collide_bounce(self.right_wall)
        self.body_2.collide_bounce(self.right_wall)

    def draw(self):
        self.graphics.rectangle(self.body_1.position.tuple, self.body_1.size.tuple)
        self.graphics.rectangle(
            self.body_2.position.tuple, self.body_2.size.tuple, (0, 0, 255)
        )
        self.graphics.rectangle(
            self.left_wall.position.tuple, self.left_wall.size.tuple
        )
        self.graphics.rectangle(
            self.right_wall.position.tuple, self.right_wall.size.tuple
        )

        self.graphics.text(str(self.body_1.kinetic), (10, 0))
        self.graphics.text(str(self.body_2.kinetic), (10, 40))
        self.graphics.text(str(self.body_1.kinetic + self.body_2.kinetic), (10, 80))


def run():
    ui = UI()

    runner = vgame.Runner()

    runner.run(ui)
