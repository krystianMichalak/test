#include <iostream>
#include <string>
#include <boost/filesystem/operations.hpp>

int main() {
    std::string tempDir = boost::filesystem::temp_directory_path().string();
    std::cout << std::endl << "Temp dir: " << tempDir << std::endl;
    return 0;
}