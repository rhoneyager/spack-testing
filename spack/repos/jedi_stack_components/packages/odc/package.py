# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Odc(CMakePackage):
    """Package to read/write ODB data."""

    homepage = "https://software.ecmwf.int/wiki/display/odc"
    git = "https://github.com/ecmwf/odc.git"
    url = "https://github.com/ecmwf/odc/archive/1.2.0.tar.gz"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master')
    version('develop', branch='develop')
    version('1.3.0', commit='b12994efb0be76a64147aa14b248ddd9ba98220a', preferred=True)
    version('1.2.0', commit='b6514e8847d09ee48fbd991dda8f23d0a0a1d21c')
    version('1.1.1', commit='31b7b8b7fddc03743ddd1566db478813c5099cdd')
    version('1.1.0', commit='bba1322f6d1976490337ee9564fbf9a392eb2528')
    version('1.0.3', commit='8a120ebc744778248dda0267094cbf9aaa9d7246')
    version('1.0.2', commit='6b75e9f666251fa4d98d6b791816cbabd9d29caa')

    #depends_on('cmake @3.10:', type=('build', 'run', 'link'))
    depends_on('ecbuild', type=('build'))
    depends_on('eckit')

    variant('fortran', default=True)

    def cmake_args(self):
        res = [
                self.define_from_variant('ENABLE_FORTRAN', 'fortran')
                ] 
        res.append('-DCMAKE_MODULE_PATH=' + self.spec['ecbuild'].prefix + '/share/ecbuild/cmake')
        return res

