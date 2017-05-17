acsim mips.ac -abi
make
mips-newlib-elf-gcc -specs=archc hello2.c -o hello2.mips
./mips.x --load=hello2.mips
