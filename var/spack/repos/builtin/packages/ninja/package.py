# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ninja(Package):
    """Ninja is a small build system with a focus on speed. It differs from
    other build systems in two major respects: it is designed to have its input
    files generated by a higher-level build system, and it is designed to run
    builds as fast as possible."""

    homepage = "https://ninja-build.org/"
    url      = "https://github.com/ninja-build/ninja/archive/v1.7.2.tar.gz"
    git      = "https://github.com/Kitware/ninja.git"

    version('kitware', branch='features-for-fortran')
    version('1.10.0', sha256='3810318b08489435f8efc19c05525e80a993af5a55baa0dfeae0465a9d45f99f')
    version('1.9.0', sha256='5d7ec75828f8d3fd1a0c2f31b5b0cea780cdfe1031359228c428c1a48bfcd5b9')
    version('1.8.2', sha256='86b8700c3d0880c2b44c2ff67ce42774aaf8c28cbf57725cb881569288c1c6f4')
    version('1.7.2', sha256='2edda0a5421ace3cf428309211270772dd35a91af60c96f93f90df6bc41b16d9')
    version('1.6.0', sha256='b43e88fb068fe4d92a3dfd9eb4d19755dae5c33415db2e9b7b61b4659009cde7')

    depends_on('python', type='build')

    phases = ['configure', 'install']

    def configure(self, spec, prefix):
        python('configure.py', '--bootstrap')

    @run_after('configure')
    @on_package_attributes(run_tests=True)
    def test(self):
        ninja = Executable('./ninja')
        ninja('-j{0}'.format(make_jobs), 'ninja_test')
        ninja_test = Executable('./ninja_test')
        ninja_test()

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('ninja', prefix.bin)
        install_tree('misc', prefix.misc)

        # Some distros like Fedora install a 'ninja-build' executable
        # instead of 'ninja'. Install both for uniformity.
        with working_dir(prefix.bin):
            symlink('ninja', 'ninja-build')
