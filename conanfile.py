from conans import ConanFile, CMake, tools
import os


class EasyLoggingConan(ConanFile):
    name = "easyloggingpp"
    version = "9.80"
    license = "MIT"
    url = "https://github.com/memsharded/conan-easyloggingpp.git"

    def source(self):
        tools.download("https://github.com/easylogging/easyloggingpp/releases/download/v9.80/easyloggingpp_v%s.zip" % self.version,
                       "easyloggingpp.zip")
        tools.unzip("easyloggingpp.zip" )

    def package(self):
        self.copy("*.h", "include")

