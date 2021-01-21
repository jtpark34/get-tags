# get-tags
Count and extract tags from Stack Enterprise.

This procedure explains how to use the *get-tags.py* script to call the Stack Enterprise tags API and extract tag names. 
It counts the tags and saves the output to a file named *output.txt* in the same directory.

# Prerequisite
Download and install Python 3.6: https://www.python.org/downloads/release/python-360/

# Procedure
1. Create an API access key: https://linkedin.stackenterprise.co/users/access-keys/149
2. Save and open *get-tags.py* and find/replace *keyID* with your unique access key. Save your changes.
3. Run the script: *python3.6 get-tags.py* 
    
**Note:** This script only outputs tags from pages 1-14 of the API results.
If/when there are additional pages of results, add those to the list of links in the script.
