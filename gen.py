import os
import yaml


BOXES = 'boxes.yaml'
CONFIG = 'config.yaml'
BASE = 'Dockerfile'
SCRIPT = 'setup.sh'
PREINSTALL = 'preinstall.sh'
INSTALL = 'install.sh'
BUILD = 'build.sh'
PUSH = 'push.sh'
PATH = './boxes'

with open(CONFIG, 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

with open(INSTALL, 'r') as f:
    install_sh = f.read()

ID = config['docker']['id']
REPO = config['docker']['repo']

AUTOGEN_SCRIPT =\
"""#!/bin/sh\n
# This file is generated automatically.
"""

def main():
    with open(BASE, 'r') as f:
        f.readline()
        base = f.read()
    with open(BOXES, 'r') as f:
        yml = yaml.load(f, Loader=yaml.FullLoader)
    for box_name, box in yml['boxes'].items():
        dir_p = os.path.join(PATH, box_name)
        setup = os.path.join(dir_p, SCRIPT)
        preinstall = os.path.join(dir_p, PREINSTALL)
        install = os.path.join(dir_p, INSTALL)
        build = os.path.join(dir_p, BUILD)
        push = os.path.join(dir_p, PUSH)
        dockerfile = os.path.join(dir_p, 'Dockerfile')
        if not os.path.exists(dir_p):
            os.mkdir(dir_p)
        if not os.path.exists(setup):
            with open(setup, 'w') as f:
                f.write(AUTOGEN_SCRIPT)
        if not os.path.exists(preinstall):
            with open(preinstall, 'w') as f:
                f.write(AUTOGEN_SCRIPT)
        if not os.path.exists(install):
            with open(install, 'w') as f:
                f.write(install_sh)

        with open(dockerfile, 'w') as f:
            f.write(f"FROM {box['image']}\n")
            f.write(base)

        with open(build, 'w') as f:
            f.write(f"""#!/bin/sh
            docker build . -t {ID}/{REPO}:{box['tag']}
            """)

        with open(push, 'w') as f:
            f.write(f"""#!/bin/sh
            docker push {ID}/{REPO}:{box['tag']}
            """)
main()
