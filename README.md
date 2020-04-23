This is a simple script I created to create a single text file of all the source code in a project.
This was created due to the need of a single file containing all source code needing to be uploaded to a turnitin point on blackboard.

Usage example:

python3 dir.py --e .js .txt .php --i txt

where --e are the file extensions to include and --i are the folders/files to ignore

The above will output a text file called source.txt containing all the code in the files in the root directory of the project ending in the provided extensions as cli arguments.i

Example output of source.txt:

####################################################
test/js/example.js
####################################################

from inside the js folder

#####################################################
test/php/example.php
#####################################################

from inside the php folder
