from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        requirements = self.conan_data["dependencies"]
        for key in requirements:
            self.requires(key + "/" + requirements[key]["version"])

    def layout(self):
        cmake_layout(self)
