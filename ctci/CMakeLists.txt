cmake_minimum_required(VERSION 3.8)

project(ctci)

set(CMAKE_CXX_FLAGS "-std=c++11 -g -Wall")

include(GoogleTest)
enable_testing()
add_subdirectory("/usr/src/gtest" ${CMAKE_BINARY_DIR}/gtest)
include_directories(${GTEST_INCLUDE_DIRS})

file(GLOB SRCS *.cpp)
add_executable(ctci ${SRCS})
target_link_libraries(ctci gtest gtest_main)

gtest_add_tests(ctci ${SRCS})
