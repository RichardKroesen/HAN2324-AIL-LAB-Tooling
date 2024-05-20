# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/libserialport"
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-build"
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix"
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/tmp"
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp"
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src"
  "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/mnt/586d8ccd-e023-4531-ad6e-e06b8e495334/HAN2324-AIL-LAB-Tooling/model_tester_app/build/_deps/libserialport-subbuild/libserialport-populate-prefix/src/libserialport-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
