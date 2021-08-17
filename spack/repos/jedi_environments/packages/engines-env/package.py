# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
import sys

from spack import *

class EnginesEnv(BundlePackage):
    """Interface for Observation Data Access development environment.."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')

    depends_on('jedi-cmake')
    depends_on('jedi-sdk-base')

    variant('python', default=True)
    if sys.platform == 'darwin':
        depends_on('python@3.7:%apple-clang', when='+python')
        depends_on('py-pybind11%apple-clang', when='+python')
        depends_on('py-numpy%apple-clang', when='+python')
    else:
        depends_on('python@3.7:', when='+python')
        depends_on('py-pybind11', when='+python')
        depends_on('py-numpy', when='+python')

    def cmake_args(self):
        res = [] 
        return res

