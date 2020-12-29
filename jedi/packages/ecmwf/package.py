# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *


class Ecmwf(BundlePackage):
    """Base packages for ecmwf. ecbuild, eckit, fckit, atlas."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')

    depends_on('ecbuild')
    depends_on('eckit~mkl~git~flex~curl~bzip2~bison~lz4')

