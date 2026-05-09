#!/usr/bin/python3
""" Module to Search and update"""

def append_after(filename="", search_string="", new_string=""):
    """ append after"""
    updated_lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

        #Process lines
        for line in lines:
            updated_lines.append(line)
        
            if search_string in line:
                updated_lines.append(new_string)
        
    # Rewrite file with updated content
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)
