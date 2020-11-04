from . import panda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")

    # `python walking_panda.py --no-rotate` stops the rotation.
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    # `python walking_panda.py --rotate-left` changes the rotation's direction from default right to left.
    parser.add_argument("--rotate-left", help="Change Rotation Direction",
                        action="store_true", default=0)
    # `python walking_panda.py --panda-scale=?` changes panda's scale to a float number specified instead of ?.
    parser.add_argument("--panda-scale", help="Change Panda Scale",
                        type=float, default=0.005)
    # `python walking_panda.py --env-scale=?` changes the environment's scale to a float number specified instead of ?.
    parser.add_argument("--env-scale", help="Change Environment Scale",
                        type=float, default=0.25)
    # `python walking_panda.py --sound-off` toggles default sound off.
    parser.add_argument("--sound-off", help="Toggle Sound Off",
                        action="store_true", default=0)

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
