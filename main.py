
#!/usr/bin/python3

import re

def compare_files(file1, file2):
    count = 0

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        cleaned_lines1 = [re.sub(r'\W+', '', line.strip()) for line in lines1 if line.strip()]
        cleaned_lines2 = [re.sub(r'\W+', '', line.strip()) for line in lines2 if line.strip()]

        for line1 in cleaned_lines1:
            if line1 in cleaned_lines2:
                count += 1

    return count


file1_path = "linuxmcqanswer.txt" 
file2_path = input("Enter : ")

matching_lines = compare_files(file1_path, file2_path)
print("correct \t:", matching_lines)
print("total marks\t:",matching_lines *2)