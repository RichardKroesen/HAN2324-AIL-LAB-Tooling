cmake_minimum_required(VERSION 3.18)
project(eml-course-model-tester C CXX ASM)

set(CMAKE_C_STANDARD 11)

include(FetchContent)
FetchContent_Declare(
  libserialport
  GIT_REPOSITORY     git://sigrok.org/libserialport
  SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/libserialport
)

# FetchContent_GetProperties(libserialport)
# if(NOT libserialport_POPULATED)
#   FetchContent_Populate(libserialport)
#   execute_process(
#     COMMAND ./autogen.sh
#     WORKING_DIRECTORY ${libserialport_SOURCE_DIR}
#   )
#   execute_process(
#     COMMAND ./configure
#     WORKING_DIRECTORY ${libserialport_SOURCE_DIR}
#   )
# endif()
FetchContent_MakeAvailable(libserialport)

if(UNIX AND NOT APPLE) 
    add_library(libserialport libserialport/linux.c libserialport/linux_termios.c libserialport/serialport.c libserialport/timing.c)
    target_compile_definitions(libserialport PUBLIC "-DSP_PRIV=__attribute__((visibility(\"hidden\")))")
elseif(WIN32) 
    add_library(libserialport libserialport/windows.c)
else()
    add_library(libserialport libserialport/macosx.c)
endif()

target_include_directories(libserialport PUBLIC libserialport/ ${CMAKE_CURRENT_LIST_DIR})


add_executable(main main.c lib/normalizations.c
lib/filters.c
lib/features_calc.c) 
target_include_directories(main PUBLIC lib/)
target_link_libraries(main libserialport)