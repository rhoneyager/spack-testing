# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class EnginesEnv(BundlePackage):
    """Interface for Observation Data Access development environment.."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')

    depends_on('jedi-cmake')
    depends_on('jedi-sdk-base')

    # Set to make cmake run better
    depends_on('cmake', type=('build', 'run'))
    depends_on('ecbuild', type=('build', 'run'))
    depends_on('eigen', type=('build', 'run'))
    depends_on('gsl-lite', type=('build', 'run'))

    variant('python', default=True)
    depends_on('python@3.7:', when='+python')
    depends_on('py-pybind11', when='+python')
    depends_on('py-numpy', when='+python')

    def cmake_args(self):
        res = [] 
        return res

