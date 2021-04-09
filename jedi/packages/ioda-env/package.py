# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class IodaEnv(BundlePackage):
    """Interface for Observation Data Access development environment.."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')

    depends_on('cmake')
    depends_on('ecbuild')
    depends_on('jedi-cmake')
    depends_on('eckit')
    depends_on('fckit')
    depends_on('atlas')
    depends_on('jedi-sdk-base')
    depends_on('oops')
    depends_on('hdf5')
    depends_on('netcdf-c')
    depends_on('gsl-lite')

    variant('bufr', default=False)
    depends_on('bufr', when='+bufr')

    variant('odc', default=False)
    depends_on('odc', when='+odc')

    def cmake_args(self):
        res = [] 
        return res

