import os
import yaml


ID = 'moratorium08'
CONFIG = 'boxes.yaml'
BASE = 'Dockerfile'
SCRIPT = 'setup.sh'
BUILD = 'build.sh'
PATH = './boxes'

AUTOGEN_SETUP =\
"""#!/bin/sh\n
# This file is generated automatically.
"""

def main():
    with open(BASE, 'r') as f:
        f.readline()
        base = f.read()
    with open(CONFIG, 'r') as f:
        yml = yaml.load(f, Loader=yaml.FullLoader)
    for box_name, box in yml['boxes'].items():
        dir_p = os.path.join(PATH, box_name)
        setup = os.path.join(dir_p, SCRIPT)
        build = os.path.join(dir_p, BUILD)
        dockerfile = os.path.join(dir_p, 'Dockerfile')
        if not os.path.exists(dir_p):
            os.mkdir(dir_p)
        if not os.path.exists(setup):
            with open(setup, 'w') as f:
                f.write(AUTOGEN_SETUP)

        with open(dockerfile, 'w') as f:
            f.write(f"FROM {box['image']}\n")
            f.write(base)

        with open(build, 'w') as f:
            f.write(f"""#!/bin/sh
            docker build . -t {ID}/lib:{box['tag']}
            """)
main()
