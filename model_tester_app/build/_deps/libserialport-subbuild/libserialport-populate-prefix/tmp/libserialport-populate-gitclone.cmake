# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

if(EXISTS "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitclone-lastrun.txt" AND EXISTS "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitinfo.txt" AND
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitclone-lastrun.txt" IS_NEWER_THAN "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitinfo.txt")
  message(STATUS
    "Avoiding repeated git clone, stamp file is up to date: "
    "'/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitclone-lastrun.txt'"
  )
  return()
endif()

execute_process(
  COMMAND ${CMAKE_COMMAND} -E rm -rf "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/libserialport"
  RESULT_VARIABLE error_code
)
if(error_code)
  message(FATAL_ERROR "Failed to remove directory: '/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/libserialport'")
endif()

# try the clone 3 times in case there is an odd git clone issue
set(error_code 1)
set(number_of_tries 0)
while(error_code AND number_of_tries LESS 3)
  execute_process(
    COMMAND "/usr/bin/git"
            clone --no-checkout --config "advice.detachedHead=false" "git://sigrok.org/libserialport" "libserialport"
    WORKING_DIRECTORY "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app"
    RESULT_VARIABLE error_code
  )
  math(EXPR number_of_tries "${number_of_tries} + 1")
endwhile()
if(number_of_tries GREATER 1)
  message(STATUS "Had to git clone more than once: ${number_of_tries} times.")
endif()
if(error_code)
  message(FATAL_ERROR "Failed to clone repository: 'git://sigrok.org/libserialport'")
endif()

execute_process(
  COMMAND "/usr/bin/git"
          checkout "master" --
  WORKING_DIRECTORY "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/libserialport"
  RESULT_VARIABLE error_code
)
if(error_code)
  message(FATAL_ERROR "Failed to checkout tag: 'master'")
endif()

set(init_submodules TRUE)
if(init_submodules)
  execute_process(
    COMMAND "/usr/bin/git" 
            submodule update --recursive --init 
    WORKING_DIRECTORY "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/libserialport"
    RESULT_VARIABLE error_code
  )
endif()
if(error_code)
  message(FATAL_ERROR "Failed to update submodules in: '/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/libserialport'")
endif()

# Complete success, update the script-last-run stamp file:
#
execute_process(
  COMMAND ${CMAKE_COMMAND} -E copy "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitinfo.txt" "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitclone-lastrun.txt"
  RESULT_VARIABLE error_code
)
if(error_code)
  message(FATAL_ERROR "Failed to copy script-last-run stamp file: '/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/libserialport-populate-gitclone-lastrun.txt'")
endif()
