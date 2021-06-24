# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Oops(CMakePackage):
    """Object Oriented Prediction System"""

    homepage = "https://github.com/JCSDA-internal/oops"
    git = "git@github.com:JCSDA-internal/oops.git"
    url = "https://github.com/JCSDA-internal/oops/archive/1.0.0.zip"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master', no_cache=True, url="https://github.com/JCSDA/oops.git")
    version('develop', branch='develop', preferred=True, no_cache=True)
    version('1.1.0', url="https://github.com/JCSDA/oops/archive/refs/tags/1.1.0.tar.gz", sha256='f3ef7d33b57246127bb9bfe63d99923b811247c72e085fabb90a7cfbc84d2ec5')
    version('1.0.0', url=",https://github.com/JCSDA/oops/archive/refs/tags/1.0.0.tar.gz", sha256='24559483938e3dcde2a55aad6d53f6cbacb057d4fc13bc88731ff040b98d2757')

    #depends_on('cmake @3.10:', type=('build', 'run', 'link'))
    depends_on('ecbuild', type=('build'))
    depends_on('eckit')
    depends_on('fckit')
    depends_on('atlas')
    depends_on('jedi-sdk-base')

    def cmake_args(self):
        res = [] 
        res.append('-DCMAKE_MODULE_PATH=' + self.spec['ecbuild'].prefix + '/share/ecbuild/cmake')
        return res

