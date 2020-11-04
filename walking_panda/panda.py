from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, panda_scale=False, env_scale=False,
                 rotate_left=False, sound_off=False):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Re-parent the model to render.
        self.scene.reparentTo(self.render)

        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spin_camera_task procedure to the task manager.
        if not no_rotate:
            self.taskMgr.add(self.spin_camera_task, "SpinCameraTask")

        # Add the left_spin_camera_task procedure to the task manager
        # if --rotate-left command line control is used.
        if rotate_left:
            self.taskMgr.add(self.left_spin_camera_task, "LeftSpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        # Rescale panda if --scale command line control is used.
        if panda_scale:
            self.pandaActor.setScale(1, 1, 1)

        # Rescale environment if --env-scale command line control is used.
        if env_scale:
            self.scene.setScale(1, 1, 1)

        # Load and play panda sound effects.
        sound = self.loader.loadSfx("jungle_sounds.ogg")
        sound.setLoop(True)
        sound.play()

        # Toggle sound off if --sound-off command line control is used.
        if sound_off:
            sound.stop()

    # Define a procedure to move the camera.
    def spin_camera_task(self, task):
        angle_degrees = task.time * 6.0
        angle_radians = angle_degrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angle_radians), -20.0 * cos(angle_radians), 3)
        self.camera.setHpr(angle_degrees, 0, 0)
        return Task.cont

    # Define a procedure to change camera's rotation's direction
    # for --rotate-left command line control.
    def left_spin_camera_task(self, task):
        left_degrees = task.time * -6.0
        left_radians = left_degrees * (pi / 180.0)
        self.camera.setPos(20 * sin(left_radians), -20.0 * cos(left_radians), 3)
        self.camera.setHpr(left_degrees, 0, 0)
        return Task.cont
