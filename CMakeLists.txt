cmake_minimum_required(VERSION 3.10)
project(CovEngineV2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

add_subdirectory(backend)

add_custom_target(build_all
    COMMAND ${CMAKE_COMMAND} -E echo "Building complete application..."
    COMMAND ${Python_EXECUTABLE} ${CMAKE_SOURCE_DIR}/build.py
    DEPENDS CEV2
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Building complete application with PyInstaller"
)

find_package(Python COMPONENTS Interpreter Development)
if(Python_FOUND)
    message(STATUS "Python found: ${Python_EXECUTABLE}")
    
    
    add_custom_target(install_dependencies
        COMMAND ${Python_EXECUTABLE} -m pip install -r ${CMAKE_SOURCE_DIR}/frontend/requirements.txt
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
        COMMENT "Installing Python dependencies"
    )
    
    
    add_dependencies(build_all install_dependencies)
else()
    message(WARNING "Python not found. Frontend build will not be available.")
endif()


install(DIRECTORY ${CMAKE_BINARY_DIR}/bin/
        DESTINATION bin
        PATTERN "*"
        PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE
                    GROUP_READ GROUP_EXECUTE
                    WORLD_READ WORLD_EXECUTE)

if(CMAKE_BUILD_TYPE STREQUAL "Release")
    install(DIRECTORY ${CMAKE_SOURCE_DIR}/dist/CovEngineV2/
            DESTINATION .
            PATTERN "*"
            PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE
                        GROUP_READ GROUP_EXECUTE
                        WORLD_READ WORLD_EXECUTE)
endif() 