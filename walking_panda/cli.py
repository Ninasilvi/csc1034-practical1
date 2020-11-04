from . import panda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--rotate-left", help="Change Rotation Direction",
                        action="store_true", default=0)
    parser.add_argument("--panda-scale", help="Set Panda Scale To 1",
                        action="store_true", default=0)
    parser.add_argument("--env-scale", help="Set Environment Scale To 1",
                        action="store_true", default=0)
    parser.add_argument("--sound-off", help="Toggle Sound Off",
                        action="store_true", default=0)

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
