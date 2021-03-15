# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *


class JediSdkExtras(BundlePackage):
    """Extra packages for jedi."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager']

    version('main', branch='main')

    depends_on('cppgsl')
    depends_on('doxygen')
    depends_on('ecflow')
    depends_on('environment-modules')
    depends_on('esmf')
    depends_on('fftw')
    depends_on('flann')

