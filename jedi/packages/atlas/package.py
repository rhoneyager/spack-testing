# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Atlas(CMakePackage):
    """A library for numerical weather prediction and climate modelling."""

    homepage = "https://software.ecmwf.int/wiki/display/atlas"
    git = "https://github.com/ecmwf/atlas.git"
    url = "https://github.com/ecmwf/atlas/archive/0.22.1.tar.gz"

    maintainers = ['rhoneyager', 'mmiesch']

    version('master', branch='master')
    version('develop', branch='develop')
    version('0.23.0', commit='7e0a1251685e07a5dcccc84f4d9251d5a066e2ee')
    version('0.22.1', commit='e55e9c72883d24e3ed4d4eaaae330825a2d77dd3')
    version('0.22.0', commit='a70030278541d4c4e18ebf92b683951749d60049')
    version('0.21.0', commit='b7728bb798b9891ce62e1034fa21c0bc33a30cab')

    depends_on('ecbuild', type=('build'))
    depends_on('eckit')
    variant('fckit', default=True)
    depends_on('fckit', when='+fckit')
    #depends_on('python')

    #variant('transi', default=False)
    #depends_on('transi', when='+transi')
    #variant('cgal', default=False)
    #depends_on('cgal', when='+cgal')
    #variant('eigen3', default=False)
    #depends_on('eigen3', when='+eigen3')
    #variant('fftw', default=False)
    #depends_on('fftw', when='+fftw')


    def cmake_args(self):
        res = [
                self.define_from_variant('ENABLE_FCKIT', 'fckit')
                ] 
        return res

