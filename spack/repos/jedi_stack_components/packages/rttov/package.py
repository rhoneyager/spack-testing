# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Rttov(CMakePackage):
    """RTTOV package from EUMETSAT"""

    homepage = "https://nwp-saf.eumetsat.int/site/software/rttov/"
    git = "https://github.com/JCSDA-internal/rttov.git"
    url = "https://github.com/JCSDA-internal/rttov/archive/1.11.6.tar.gz"

    maintainers = ['rhoneyager', 'mmiesch']

    version('develop', branch='develop', preferred=True, no_cache=True)
    version('master', branch='master', no_cache=True)

    depends_on('ecbuild', type=('build'))

    depends_on('hdf5@1.12.0+hl+fortran+szip') # 1.12 needed for jedi. Make optional? C interface only. MPI.


