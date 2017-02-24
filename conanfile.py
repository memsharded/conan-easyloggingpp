from conans import ConanFile, CMake, tools
import os


class EasyLoggingConan(ConanFile):
    name = "easyloggingpp"
    version = "9.94.1"
    license = "MIT"
    url = "https://github.com/memsharded/conan-easyloggingpp.git"
    description = """Single header C++ logging library. It is extremely powerful, extendable, 
light-weight, fast performing, thread and type safe and consists of many built-in features. 
It provides ability to write logs in your own customized format.
It also provide support for logging your classes, third-party libraries, STL and third-party containers etc."""

    def source(self):
        tools.download("https://github.com/muflihun/easyloggingpp/releases/download/v%s/easyloggingpp_v%s.zip" % (self.version, self.version),
                       "easyloggingpp.zip")
        tools.unzip("easyloggingpp.zip" )

    def package(self):
        self.copy("*.h", "include")
        self.copy("*.cc", "include")



