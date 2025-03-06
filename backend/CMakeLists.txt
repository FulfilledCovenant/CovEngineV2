cmake_minimum_required(VERSION 3.10)
project(CEV2)

set(CMAKE_CXX_STANDARD 11)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_executable(CEV2 
    main.cpp 
    tweaks_utils.cpp
    tweaks_performance.cpp
    tweaks_gaming.cpp
    tweaks_privacy.cpp
    tweaks_security.cpp
)

if(WIN32)
    target_link_libraries(CEV2 advapi32)
endif()

message(STATUS "Build with: cmake --build . --config Release")
message(STATUS "Run with: ./CEV2 test (Linux/macOS) or .\\CEV2.exe test (Windows)") 