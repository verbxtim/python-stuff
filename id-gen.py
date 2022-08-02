# random id generator
# not sure if i made this or someone else did
import random

print("%04x:%04x:%04x:%04x" % (
random.randint(0, 60000),
random.randint(0, 60000),
random.randint(0, 60000),
random.randint(0, 60000),
))
