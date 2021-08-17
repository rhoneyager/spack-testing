# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *

class Ecbuild(CMakePackage):
    """A CMake-based build system, consisting of a collection of CMake macros and functions that ease the managing of software build systems."""

    homepage = "https://software.ecmwf.int/wiki/display/ecbuild"
    git = "https://github.com/ecmwf/ecbuild.git"
    url = "https://github.com/ecmwf/ecbuild/archive/3.4.1.tar.gz"

    maintainers = ['rhoneyager', 'mmiesch']

    version('3.6.2', commit='28a007d15059be24fb65439adf7633ce8b65abe1')
    version('3.5.0', commit='70f224596cf0058567bed2021bec0481742f9f63')
    version('3.4.1', commit='d4347cf92466c742ef989444b2acbf7c867a338e')
    version('3.4.0', commit='d18a2dfa4a350881bfdded080880eaa47d2361f8')
    version('3.3.5', commit='b10ab33fff852411fe842c4178d35993223e116f')
    version('3.3.2', commit='362e3d93d331b62bf8b6cf515db253c9e9c50daa')
    version('3.3.1', commit='34f8362771aef4fc9debd886011fa188a120522a')
    version('3.3.0', commit='a981ba52b0765b8e4c7a28210fc804fb772030e9')
    version('3.2.0', commit='9dcf4c6f80c2cbd349f110af53c0256f1687d160')
    version('3.1.0', commit='457e7ea1c78dcfe0cef51e6ea886b7c53a0c94c3')

    #depends_on('cmake @3.10:', type=('build', 'run', 'link'))

