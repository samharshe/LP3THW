from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Hit return to continue or ^C to exit.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("All right. All done.")

out_file.close()
in_file.close()