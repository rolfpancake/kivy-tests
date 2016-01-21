# Checks your environment
# Is everything installed correctly?

# OS version
import os
import platform
print('Hello from', os.name.upper(), platform.system(), platform.release())

# Python version
import sys
print('Hello from Python', sys.version)

# Kivy version
import kivy
print('Hello from Kivy', kivy.__version__)

# Pygame version
# import pygame
# print("Hello from Pygame", pygame.version.ver)
