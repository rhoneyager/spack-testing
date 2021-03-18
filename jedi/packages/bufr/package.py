# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Bufr(CMakePackage):
    """Package to read/write BUFR data."""

    homepage = "https://software.ecmwf.int/wiki/display/odc"
    git = "https://github.com/NOAA-EMC/NCEPLIBS-bufr.git"
    url = "https://github.com/NOAA-EMC/NCEPLIBS-bufr/archive/bufr_v11.4.0.tar.gz"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master')
    version('develop', branch='develop')
    version('11.4.0', commit='eaa10dda59ad166aeef6b8d59be929ef621856fb', preferred=True)

    variant('docs', default=False)
    depends_on('doxygen', when='+doxygen')
    variant('python', default=False)
    depends_on('python', when='+python')

    variant('shared', default=True)

    def cmake_args(self):
        res = [
                self.define_from_variant('ENABLE_DOCS', 'docs'),
                self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
                self.define_from_variant('ENABLE_PYTHON', 'python')
                ] 
        return res

