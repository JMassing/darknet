from conans import ConanFile, CMake, tools
from pathlib import Path

class DarknetConan(ConanFile):
    name = "Darknet"
    version = "1.0.0"
    license = "Open Source"
    author = "Julian Massing julimassing@gmail.com"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        pass

    def imports(self):
        #self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        pass

    def build(self, keep_imports=True):
        cmake = CMake(self)
        # cmake defines for darknet build
        cmake.definitions["CMAKE_VERBOSE_MAKEFILE"] = "ON"
        cmake.definitions["CUDA_VERBOSE_BUILD"] = "ON"
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.definitions["BUILD_AS_CPP"] = "ON"
        cmake.definitions["BUILD_USELIB_TRACK"] = "OFF"
        cmake.definitions["MANUALLY_EXPORT_TRACK_OPTFLOW"] = "OFF"
        cmake.definitions["ENABLE_OPENCV"] = "ON"
        cmake.definitions["ENABLE_CUDA"] = "OFF"
        cmake.definitions["ENABLE_CUDNN"] = "ON"
        cmake.definitions["ENABLE_CUDNN_HALF"] = "ON"
        cmake.definitions["ENABLE_ZED_CAMERA"] = "OFF"
        cmake.definitions["ENABLE_VCPKG_INTEGRATION"] = "ON"
        cmake.definitions["ENABLE_CSHARP_WRAPPER"] = "OFF"
        cmake.definitions["VCPKG_BUILD_OPENCV_WITH_CUDA"] = "OFF"
        cmake.definitions["VCPKG_USE_OPENCV2"] = "OFF"
        cmake.definitions["VCPKG_USE_OPENCV3"] = "OFF"
        cmake.definitions["VCPKG_USE_OPENCV4"] = "ON"
        vcpkg_toolchainfile = Path(self.source_folder) / "external/vcpkg/scripts/buildsystems/vcpkg.cmake"
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = vcpkg_toolchainfile.resolve().as_posix()
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        pass
        # if self.settings.os == "Windows":
        #     tools.rename("app/config_windows.ini", "app/config.ini")
        # else:
        #     tools.rename("app/config_linux.ini", "app/config.ini")

        # self.copy("*.lib", dst="lib", keep_path=False)
        # self.copy("*.dll", dst="bin", keep_path=False)
        # self.copy("*.so", dst="lib", keep_path=False)
        # self.copy("*.a", dst="lib", keep_path=False)
        # self.copy("Pokerbot.exe", dst="bin", src="bin", keep_path=False)
        # self.copy("Pokerbot", dst="bin", src="bin", keep_path=False)
        # self.copy("Card_Imgs/*", dst="", keep_path=True)
        # self.copy("app/config.ini", dst="", keep_path=False)
        # self.copy("app/imgui.ini", dst="bin", keep_path=False) 
 
    def package_info(self):
        pass
        #self.cpp_info.libs = ["opencv", "boost", "gtest"]

