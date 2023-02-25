from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
in_data = in_file.read()

print(f"Does the output file already exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(in_data)

print("All right. All done.")

out_file.close()
in_file.close()