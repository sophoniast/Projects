insulin = """ORIGIN      
    1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
   61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//"""

clean_Insulin = insulin.replace(" ", "")
print(clean_Insulin)
clean_Insulin = clean_Insulin.replace("\n", "")
print(clean_Insulin)
clean_Insulin = clean_Insulin.replace("ORIGIN", "")
print(clean_Insulin)

for digit in range(0, 10):
    clean_Insulin = clean_Insulin.replace(str(digit), "")

print(clean_Insulin)

clean_Insulin = clean_Insulin.replace("//", "")

# for UNDESIRED in ["\n", " ", "//", "ORIGIN"]:
#     clean_Insulin=clean_Insulin.replace(UNDESIRED,"")
#     print(f"Replaced {UNDESIRED} with nothing!")

lsinsulin = clean_Insulin[0:24]
print(len(lsinsulin))
binsulin = clean_Insulin[24:54]
print(len(binsulin))
cinsulin = clean_Insulin[54:89]
print(len(cinsulin))
ainsulin = clean_Insulin[89:]
print(len(ainsulin))


lsfile = open("lsinsulin_seq_clean.txt", "w")
lsfile.write(lsinsulin)
lsfile.close()

bfile = open("binsulin_seq_clean.txt", "w")
bfile.write(binsulin)
bfile.close()

cfile = open("cinsulin_seq_clean.txt", "w")
cfile.write(cinsulin)
cfile.close()

afile = open("ainsulin_seq_clean.txt", "w")
afile.write(ainsulin)
afile.close()
