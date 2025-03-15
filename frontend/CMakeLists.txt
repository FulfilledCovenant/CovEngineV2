cmake_minimum_required(VERSION 3.10)
project(SpoofBackend)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(SPF spoofer_backend.cpp)

if(MSVC)
    target_compile_options(SPF PRIVATE /W4)
    
    target_link_libraries(SPF PRIVATE wininet shlwapi)
else()
    target_compile_options(SPF PRIVATE -Wall -Wextra)
endif()

set_target_properties(SPF
    PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin") 