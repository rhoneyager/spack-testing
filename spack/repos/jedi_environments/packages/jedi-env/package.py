# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
import sys

from spack import *

class JediEnv(BundlePackage):
    """JEDI development environment.."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')

    depends_on('cmake')
    depends_on('ecbuild')
    depends_on('jedi-cmake')
    depends_on('jedi-sdk-base')

    depends_on('eckit')
    depends_on('fckit')
    depends_on('atlas')
    depends_on('oops')
    depends_on('hdf5')
    depends_on('netcdf-c@:4.7.4')
    depends_on('gsl-lite')
    depends_on('git', type='run')
    depends_on('git-lfs', type='run')

    variant('bufr', default=False)
    depends_on('bufr', when='+bufr')

    variant('odc', default=False)
    depends_on('odc', when='+odc')

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

