void gadgets(void) {
	__asm__(
		"xor %eax, %eax;"
		"ret;"
		"pop %ecx;"
		"pop %edx;"
		"ret;"
		"mov %eax, 0x18(%edx);"
		"ret;"
		"or %cl, %al;"
		"ret;"
		"pop %ebx;"
		"ret;"
		"int $0x80;"
		"ret;"
	);
}