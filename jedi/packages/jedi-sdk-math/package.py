# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *


class JediSdkMath(BundlePackage):
    """Optional math packages for jedi."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager']

    version('main', branch='main')

    depends_on('armadillo')
    depends_on('arrayfire')
    depends_on('blaze')
    depends_on('dlib')
    #itpp?
    #boost ublas?


