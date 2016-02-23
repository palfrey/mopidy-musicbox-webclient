from __future__ import unicode_literals

import re

from setuptools import find_packages, setup
import distutils.command.install_lib
import os

def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']

class conf_install_lib(distutils.command.install_lib.install_lib):
  def run(self):
    distutils.command.install_lib.install_lib.run(self)
    for fn in self.get_outputs():
      if fn.endswith("ext.conf"):
        mode = 0644
        distutils.log.info("changing mode of %s to %o", fn, mode)
        os.chmod(fn, mode)

setup(
    name='Mopidy-MusicBox-Webclient',
    version=get_version('mopidy_musicbox_webclient/__init__.py'),
    url='https://github.com/woutervanwijk/mopidy-musicbox-webclient',
    license='Apache License, Version 2.0',
    author='Wouter van Wijk',
    author_email='woutervanwijk@gmail.com',
    description='Mopidy MusicBox web extension',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.1.0',
    ],
    cmdclass={'install_lib': conf_install_lib},
    entry_points={
        'mopidy.ext': [
            'musicbox_webclient = mopidy_musicbox_webclient:MusicBoxExtension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
