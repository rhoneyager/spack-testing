# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Ioda(CMakePackage):
    """Interface for Observation Data Access."""

    homepage = "https://github.com/JCSDA-internal/ioda"
    git = "git@github.com:JCSDA-internal/ioda.git"
    url = "https://github.com/JCSDA-internal/ioda/archive/1.0.0.zip"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master')
    version('ioda-v2', branch='feature/ioda-v2')
    version('jedicmake', branch='bugfix/jedicmake', preferred=True)
    version('develop', branch='develop')
    version('1.0.0', commit='3cbf1449f6a2caac946232d91d473a70585054c7')

    depends_on('ecbuild', type=('build'))
    depends_on('jedi-cmake', type=('build'))
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

