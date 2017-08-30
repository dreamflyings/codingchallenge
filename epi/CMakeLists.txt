cmake_minimum_required(VERSION 2.8)

set(CMAKE_CXX_FLAGS "-std=c++11 -g -Wall")

project(epi)

file(GLOB SRCS *.cpp *.h)

add_executable(epi ${SRCS})

target_link_libraries(epi gtest gtest_main)
