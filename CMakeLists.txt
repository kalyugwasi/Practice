cmake_minimum_required(VERSION 3.25)
project(Practice)

set(CMAKE_CXX_STANDARD 17)

add_executable(Practice )

# Add include/lib paths (only needed if CLion can't auto-detect them)
include_directories("D:/Clion 2025.2.2/bin/mingw/include")
link_directories("D:/Clion 2025.2.2/bin/mingw/lib")

# Link BGI and Windows system libraries
target_link_libraries(Practice
        -lbgi
        -lgdi32
        -lcomdlg32
        -luuid
        -loleaut32
        -lole32
)
