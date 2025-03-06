cmake_minimum_required(VERSION 3.10)

if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_SOURCE_DIR)
    project(CEV2)
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/nlohmann)

set(SOURCES
    main.cpp
    tweaks.cpp
    tweaks_utils.cpp
    tweaks_performance.cpp
    tweaks_gaming.cpp
    tweaks_privacy.cpp
    tweaks_security.cpp
)

set(HEADERS
    tweaks.h
)

add_executable(CEV2 ${SOURCES} ${HEADERS})

if(WIN32)
    target_link_libraries(CEV2 advapi32)
endif()

if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_SOURCE_DIR)
    set_target_properties(CEV2 PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/build/Release"
    )
endif()

install(TARGETS CEV2
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

message(STATUS "Backend configuration complete")
message(STATUS "Build with: cmake --build . --config Release")
message(STATUS "Run with: ./CEV2 test (Linux/macOS) or .\\CEV2.exe test (Windows)") 