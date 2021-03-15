# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class JediCmake(CMakePackage):
    """CMake/ecbuild toolchains to facilitate portability on different systems."""

    homepage = "https://github.com/JCSDA-internal/jedi-cmake"
    git = "git@github.com:JCSDA-internal/jedi-cmake.git"
    url = "https://github.com/JCSDA-internal/jedi-cmake/archive/1.0.0.zip"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master')
    version('develop', branch='develop')
    version('fixtest', branch='feature/export_functions', preferred=True)
    version('1.0.0', commit='3f59be473037bd3d21df90c7a3f200d8012f679e')

    depends_on('cmake @3.10:', type=('build', 'run'))
    #depends_on('ecbuild', type=('build'))

