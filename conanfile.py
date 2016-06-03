from conans import ConanFile, CMake, tools
import os


class EasyLoggingConan(ConanFile):
    name = "easyloggingpp"
    version = "8.91"
    license = "MIT"
    url = "https://github.com/memsharded/conan-easyloggingpp.git"

    def source(self):
        tools.download("https://github.com/easylogging/easyloggingpp/releases/download/v%s/easyloggingpp_v%s.zip" % (self.version, self.version),
                       "easyloggingpp.zip")
        tools.unzip("easyloggingpp.zip" )

    def package(self):
        self.copy("*.h", "include")

