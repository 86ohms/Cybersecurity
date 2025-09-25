**Execution**
Use run.sh against flawed-program.c

**Return to Libc (Ret2libc) exercise**
- Prohibits execution on the stack
- Set an address on tack to redirect execution of libc functions that does something for attacker (e.g., run /bin/sh)
- Use GDB for search tool in practice

**Notes:**
Architecture
- x86 function args are on stack
- x86_64 function args are in registers
- ARM has some args in register (usually in first four) while the rest are on stack
- MIPS is typically the same as ARM

**Stack Layout**

<img width="513" height="603" alt="image" src="https://github.com/user-attachments/assets/9361a64b-746a-4faf-8dcd-d7d02b748a55" />

