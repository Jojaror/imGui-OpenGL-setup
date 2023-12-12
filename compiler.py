import subprocess

file_name = "main"
include_dir = "dependencies/include"
lib_dir = "dependencies/lib"
lib = "-lglew32s -lopengl32 -lgdi32 -lfreeglut"
imguih = "dependencies/include/*.h"
imguicpp = "dependencies/include/*.cpp"
preprocessor = "-DGLEW_STATIC"

def main():
    subprocess.call(f"g++ {preprocessor} -c main.cpp -I{include_dir}")
    subprocess.call(f"g++ {preprocessor} *.o -o {file_name} -L{lib_dir} {lib} -g {imguih} {imguicpp}")

if __name__ == "__main__":
    main()