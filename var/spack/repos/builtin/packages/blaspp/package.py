# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack import *


class Blaspp(CMakePackage):
    """C++ API for the Basic Linear Algebra Subroutines. Developed by the 
       Innovative Computing Laboratory at the University of Tennessee, 
       Knoxville."""

    homepage = "https://bitbucket.org/icl/blaspp"
    #url      = "https://bitbucket.org/icl/blaspp"
    url      = "https://bitbucket.org/jfinney10/blaspp"

    # notify when the package is updated.
    maintainers = ['jmfinney-icl']

    version ('develop', hg=url)

    variant ('test', default=False, description = 'Enables tester build')

    # Dependencies.
    depends_on('blas')
    depends_on('lapack')
    depends_on('testsweeper', when='+test')

    # cmake 3.8.2 or newer
    depends_on("cmake@3.8.2:", type='build')

    def cmake_args(self):
        spec = self.spec
        cmake_args = [
            '-DBLASPP_BUILD_TESTS={}'.format ('ON' if '+test' in spec else 'OFF'),
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix,
            '-DCMAKE_INSTALL_NAME_DIR:PATH=%s/lib' % self.prefix,
            '-DBLAS_LIBRARIES=%s' % spec['blas'].libs.joined(';'),
            '-DLAPACK_LIBRARIES=%s' % (spec['lapack'].libs + spec['blas'].libs).joined(';')
        ]

        #build_targets = ['blaspp']

        return cmake_args
