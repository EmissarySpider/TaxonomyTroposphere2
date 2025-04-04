This script will search a directory for any shell scripts that match the specified regex and output the results to a text file named 'cred_file_names.txt'.

It isn't any more powerful than using egrep on its own. The most practical use case is when you are looking at a directory with many files and you want to know which ones are interacting with a consistent variable name.

You may need to change permissions on this script for it to execute:
chmod +x cred_file_variable_extractor.sh

Run the script using bash and provide the target directory as an argument:

bash cred_file_variable_extractor.sh ~/{workshop_directory}/malware

The output is saved to 'cred_file_names.txt', which contains paths for the files that match your search.
