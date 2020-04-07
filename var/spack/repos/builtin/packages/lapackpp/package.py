# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lapackpp(CMakePackage):
    """C++ API for LAPACK.  Developed as part of SLATE linear algebra library
       project for ECP.."""

    homepage = "https://icl.utk.edu/icl"
    url      = "https://bitbucket.org/icl/lapackpp"

    # notify when the package is updated.
    maintainers = ['jmfinney-icl']

    # Versions and checksums.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version ('develop', hg=url)

    variant ('test', default=False, description='Builds and installs testers')

    # Add dependencies if required.
    depends_on('blaspp')
    depends_on('lapack@3.4.0')
    depends_on('testsweeper', when='+test')

    # cmake 3.8.2 or newer
    depends_on("cmake@3.8.2:", type='build')

    def cmake_args(self):
        spec = self.spec
        cmake_args = [
            '-DLAPACKPP_BUILD_TESTS={}'.format ('ON' if '+test' in spec else 'OFF'),
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix,
            '-DCMAKE_INSTALL_NAME_DIR:PATH=%s/lib' % self.prefix,
            '-DBLAS_LIBRARIES=%s' % spec['blas'].libs.joined(';')#,
            #'-DLAPACK_LIBRARIES=%s' % (spec['lapack'].libs + spec['blas'].libs).joined(';')
        ]
        #build_targets = ['lapackpp']
        return cmake_args
