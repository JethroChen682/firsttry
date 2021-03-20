import torch

import os
import sys

out = sys.stdout
sys.stdout = open("help.txt", "w")
help(torch)
sys.stdout.close()
sys.stdout = out