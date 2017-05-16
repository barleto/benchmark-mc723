# NÃO ESQUECER DE ATULIZAR OS PATHs (tanto do trace quanto do Dinero)
# Copie, cole e modifique este arquivo para os outros traces
# NÃO ESQUEÇA DE ATUALIZAR NO .cpp TAMBÉM!!

#!/bin/bash
trace="/home/path/to/trace-name"
# Configuração 1 de cache
/home/mc723/dinero4sbc/dineroIV -maxtrace 20 -l1-usize 32K -l1-ubsize 64 -l1-uassoc 2 -l2-usize 256K -l2-ubsize 1024 -l2-uassoc 2 -informat d < ${trace}.din

# Configuração 2 de cache
/home/mc723/dinero4sbc/dineroIV -maxtrace 20 -l1-usize 64K -l1-ubsize 128 -l1-uassoc 2 -l2-usize 512K -l2-ubsize 1024 -l2-uassoc 2 -informat d < ${trace}.din

# Configuração 3 de cache
/home/mc723/dinero4sbc/dineroIV -maxtrace 20 -l1-usize 128K -l1-ubsize 128 -l1-uassoc 2 -l2-usize 1024K -l2-ubsize 2048 -l2-uassoc 2 -informat d < ${trace}.din

# Configuração 4 de cache
/home/mc723/dinero4sbc/dineroIV -maxtrace 20 -l1-usize 128K -l1-ubsize 128 -l1-uassoc 2 -l2-usize 1024K -l2-ubsize 2048 -l2-uassoc 4 -informat d < ${trace}.din
