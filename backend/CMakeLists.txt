cmake_minimum_required(VERSION 3.10)
project(CEV2)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_BINARY_DIR}/bin/Debug)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_BINARY_DIR}/bin/Release)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_executable(CEV2 
    main.cpp 
    tweaks_utils.cpp
    tweaks_missing.cpp
)

if(WIN32)
    target_link_libraries(CEV2 advapi32)
endif()

message(STATUS "Build with: cmake --build . --config Release")
message(STATUS "Run with: ./CEV2 test (Linux/macOS) or .\\CEV2.exe test (Windows)") 