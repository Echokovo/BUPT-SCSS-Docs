len = 560
location = 0x00427A40
xor = 0x18

for i in range(len):
    idc.patch_byte(location + i, idc.get_db_byte(location + i) ^ xor)