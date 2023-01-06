from setuptools import setup, find_packages, Command

import os

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

# Further down when you call setup()
setup(
    name = "pocprod_taina",
    packages = find_packages(),
    cmdclass = {
        'clean': CleanCommand,
    }
)