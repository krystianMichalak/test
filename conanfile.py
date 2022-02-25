from ensurepip import version
from conans import ConanFile, CMake, tools
import os, platform

class FilesystemConan(ConanFile):
    name ="Filesystem"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"

def source(self):
    self.run("git clone https://github.com/krystianMichalak/test.git")

def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

def package(self):
    cmake = CMake(self)
    cmake.install()

def package_info(self):
    self.cpp_info.libs = ["hello"]