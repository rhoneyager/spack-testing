# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Fckit(CMakePackage):
    """A Fortran toolkit for interoperating Fortran with C/C++."""

    homepage = "https://software.ecmwf.int/wiki/display/fckit"
    git = "https://github.com/ecmwf/fckit.git"
    url = "https://github.com/ecmwf/fckit/archive/0.9.0.tar.gz"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master')
    version('develop', branch='develop')
    version('0.9.0', commit='9cd993a524264e079ae260dbc89faea599e270fc')
    version('0.8.0', commit='4cd749f1eeac64eece00adb50abd072ea14fa2b1')
    version('0.7.0', commit='5a9ad884c087ae4c188a5937acf078514519778f')

    #depends_on('cmake @3.10:', type=('build', 'run', 'link'))
    depends_on('ecbuild', type=('build'))

    variant('eckit', default=True)
    depends_on('eckit', when='+eckit')

    def cmake_args(self):
        res = [
                self.define_from_variant('ENABLE_ECKIT', 'eckit')
                ] 
        res.append('-DCMAKE_MODULE_PATH=' + self.spec['ecbuild'].prefix + '/share/ecbuild/cmake')
        return res

