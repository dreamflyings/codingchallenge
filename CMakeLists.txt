cmake_minimum_required(VERSION 2.8)

set(CMAKE_CXX_FLAGS "-std=c++11 -g -Wall")

project(ctci)

file(GLOB SRCS *.cpp *.h)

add_executable(ctci ${SRCS})

target_link_libraries(ctci gtest gtest_main)

