CSC1034: Practical 1
====================
Portfolio 1
===========

This package is build as a part of the CSC1034: Portfolio-1.

Type `python walking_panda.py` to see a *__3D panda__* animation.

<br />

__Command Line Control__

There are 5 different command line control options implemented into this program:

* `--no-rotate` to suppress camera's rotation (by default the rotation is on);

* `--rotate-left` to change camera's rotation's direction (by default it rotates to the right);

* `--panda-scale=?` to change the panda's scale to an input value replacing the `?` (by default it's 0.005);

* `--env-scale=?` to change the environment's scale to an input value replacing the `?` (by default it's 0.25);

* `--sound-off` to toggle sound effects off (by default they are on).

<br />

__Additional Notes__

There are a couple things to note about the project:

* When rotation is disabled, the camera position changes automatically, so the view is zoomed in.

* When either the panda's or the environment's scale is changed, it does not change the scale of the other (independent), 
does not change the position of the model and does not change camera's position (models may be seen from a peculiar point of view).

* The sound effects are naturally really quiet, so use headphones with maximum volume for the best immersive jungle
experience.
