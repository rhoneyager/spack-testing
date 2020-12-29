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
    url = "https://github.com/JCSDA-internal/oops/archive/1.0.0.zip"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master')
    version('develop', branch='develop', preferred=True)
    version('1.0.0', commit='3cbf1449f6a2caac946232d91d473a70585054c7')

    #depends_on('cmake @3.10:', type=('build', 'run', 'link'))
    depends_on('ecbuild', type=('build'))
    depends_on('eckit')
    depends_on('fckit')
    depends_on('atlas')
    depends_on('jedi_base')
    depends_on('oops')
    depends_on('hdf5')
    depends_on('netcdf-c')
    depends_on('gsl-lite')

    def cmake_args(self):
        res = [] 
        res.append('-DCMAKE_MODULE_PATH=' + self.spec['ecbuild'].prefix + '/share/ecbuild/cmake')
        #res.append('-DCMAKE_MODULE_PATH='+os.environ['CMAKE_MODULE_PATH'])
        return res

