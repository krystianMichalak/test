cmake_minimum_required(VERSION 3.15)
project(filesystem CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(fs main.cpp)
target_link_libraries(fs ${CONAN_LIBS})