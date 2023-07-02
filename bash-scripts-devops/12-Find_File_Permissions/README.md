Save the script in a file, for example, permissions.sh, and make it executable using the following command:
chmod +x permissions.sh

To use the script, run it followed by the file path as an argument:
./permissions.sh /path/to/file

It will then display the permissions of the specified file.
--------------------------

Let's break down the command permissions=$(stat -c "%A" "$file_path"):

- stat: It is a command-line utility in Linux used to display file or file system status.
- -c "%A": This option is used to specify the format for the output of stat. In this case, %A is a format specifier that represents the access permissions of the file in human-readable form.
- "$file_path": This is the path to the file for which we want to retrieve the permissions. The value of the $file_path variable is provided as an argument to the stat command.

So, when the script executes the line permissions=$(stat -c "%A" "$file_path"), it runs the stat command with the specified format option and file path. The output of the command is captured and stored in the permissions variable.

For example, if the file at $file_path has permissions -rw-r--r--, the value stored in the permissions variable will be rw-r--r--. This value represents the file's access permissions in a human-readable format, where each character represents a specific permission (read, write, or execute) for the owner, group, and others.

Finally, the script displays the file path and its permissions using the echo command.
-------------------------------

THe full output of "stat" command looks like this:

Size: 538             Blocks: 8          IO Block: 4096   regular file
Device: 810h/2064d      Inode: 29729       Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2023-02-13 18:30:48.016848049 +0530
Modify: 2023-02-13 18:30:39.886848016 +0530
Change: 2023-02-13 18:30:39.886848016 +0530
 Birth: 2023-02-13 18:17:20.263138062 +0530
--------------------------------------------

