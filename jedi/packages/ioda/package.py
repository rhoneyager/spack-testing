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

    version('master', branch='master', no_cache=True)
    version('develop', branch='develop', no_cache=True, preferred=True)
    version('2.0.0', url="https://github.com/JCSDA/ioda/archive/refs/tags/2.0.0.tar.gz", sha256='bdea62c573930223a6f5e080cef960343d220dbcc126b4e55639c63a1219e5a2')
    version('1.0.0', url="https://github.com/JCSDA/ioda/archive/refs/tags/1.0.0.tar.gz", sha256='7e1bedaf1c8100b2f2f53c9bf733f2861369ab9421172d6528ca763c989a75f6')

    depends_on('ecbuild', type=('build'))
    depends_on('jedi-cmake', type=('build'))
    depends_on('eckit')
    depends_on('fckit')
    depends_on('atlas')
    depends_on('jedi-sdk-base')
    depends_on('oops@1.0.0', when='@1.0.0')
    depends_on('oops@1.1.0', when='@2.0.0')
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

