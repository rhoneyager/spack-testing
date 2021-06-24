# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Ufo(CMakePackage):
    """Unified Forward Operator."""

    homepage = "https://github.com/JCSDA-internal/ufo"
    git = "git@github.com:JCSDA-internal/ufo.git"
    url = "https://github.com/JCSDA-internal/ufo/archive/1.0.0.zip"

    maintainers = ['rhoneyager']

    version('master', branch='master', no_cache=True)
    version('develop', branch='develop', preferred=True, no_cache=True)
    version('1.1.0', commit='2af9b91433553ca473c72fcd131400a01c3aabdb')
    version('1.0.0', commit='68dab85486f5d79991956076ac6b962bc1a0c5bd')

    # Optional: CRTM, RTTOV, GSW, ROPP-UFO, GEOS-AERO
    depends_on('ecbuild', type=('build'))
    depends_on('jedi-cmake')
    depends_on('jedi-sdk-base')
    depends_on('oops')
    depends_on('oops@1.0.0', when='@1.0.0')
    depends_on('oops@1.1.0', when='@1.1.0')
    depends_on('ioda')
    depends_on('ioda@1.0.0', when='@1.0.0')
    depends_on('ioda@2.0.0', when='@1.1.0')

    def cmake_args(self):
        res = [] 
        res.append('-DCMAKE_MODULE_PATH=' + self.spec['ecbuild'].prefix + '/share/ecbuild/cmake')
        return res

