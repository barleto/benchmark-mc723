acsim mips.ac -abi
make
mips-newlib-elf-gcc -specs=archc hello.c -o hello.mips
./mips.x --load=hello.mips
