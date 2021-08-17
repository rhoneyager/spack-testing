# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nccmp(CMakePackage):
    """Compare NetCDF Files"""
    homepage = "https://gitlab.com/remikz/nccmp"
    git = "https://gitlab.com/remikz/nccmp.git"
    url = "https://gitlab.com/remikz/nccmp/-/archive/1.8.8.0/nccmp-1.8.8.0.zip"

    version('1.9.0.1', commit='e10f944b336f727c2d5a841e38e8efa634a22318')
    version('1.8.9.0', commit='8a7ec138b614727915c9e4ab188f74a1466366b8', preferred=True)
    version('1.8.8.0', commit='18d03b25e2d0b3c289f430931fb6838f23ebb1d9')

    depends_on('netcdf-c')

    def cmake_args(self):
        res = [
                self.define('CMAKE_C_FLAGS', '-fcommon'),
                self.define('CMAKE_EXE_LINKER_FLAGS', '-fcommon')
                ]
        return res

