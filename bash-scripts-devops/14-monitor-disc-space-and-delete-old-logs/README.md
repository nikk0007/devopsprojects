To monitor disk space and delete old log files using a bash script, you can utilize the df command to check the disk usage and the find command to locate and delete old log files.

In this script:

We set the threshold variable to specify the maximum acceptable disk usage percentage. Adjust this value according to your requirements.

The df command with the --output=pcent option is used to get the disk usage percentage of the root file system (/). The output is parsed using awk to extract the percentage value.

If the disk usage exceeds the threshold, we proceed to delete old log files.
We set the age_limit variable to specify the maximum age (in days) for log files to be considered as old. Modify this value based on your desired timeframe.

The find command is used to locate log files (*.log) in the specified log_directory that are older than the defined age_limit. The -delete option is used to delete the matched files.
If disk usage is below the threshold or no old log files are found, appropriate messages are displayed.

You can customize this script by adjusting the threshold, log directory, age limit, or file patterns according to your specific monitoring and cleanup requirements. Additionally, you can schedule this script to run periodically using cron or any other task scheduling mechanism.
-----------------------------------

==> disk_usage=$(df -h --output=pcent / | awk 'NR==2 {print substr($0, 1, length($0)-1)}')

- df -h --output=pcent /: This command displays the disk usage information for the root file system (/). The -h option is used to display the output in a human-readable format, and the --output=pcent option specifies that only the percentage of disk usage should be shown.

- |: The vertical pipe symbol (|) is used to pipe or redirect the output of the preceding command (df) as input to the next command (awk).

- awk 'NR==2 {print substr($0, 1, length($0)-1)}': This awk command is used to extract the disk usage percentage from the df command output.

- NR==2: NR represents the current record number, and ==2 checks if the record number is equal to 2. In this case, it ensures that the command processes only the second line of the df output, which contains the disk usage information for the root file system.

- {print substr($0, 1, length($0)-1)}: This part is the action block of the awk command. $0 represents the entire input record (in this case, the second line of the df output). substr($0, 1, length($0)-1) extracts a substring from the input record, starting from the first character and ending at the second last character. The -1 is used to exclude the percentage sign at the end of the disk usage value.

Finally, the extracted disk usage value is printed as the output of the awk command.

disk_usage=$(...): This syntax assigns the output of the entire command within the parentheses to the disk_usage variable. It captures the disk usage percentage value for further processing or display within the bash script.

In summary, the disk_usage=$(df -h --output=pcent / | awk 'NR==2 {print substr($0, 1, length($0)-1)}') command calculates the disk usage percentage of the root file system (/) by executing the df command, extracting the necessary information using awk, and storing the result in the disk_usage variable for further use in the script.
-------------------------------------------

To schedule a cron job in Linux to run this script every Friday at 5 PM, you can follow these steps:

Open the crontab file for editing using the following command:
crontab -e
If prompted, choose an editor to edit the crontab file (such as nano or vim).

Add the following line to the crontab file:
0 17 * * 5 /path/to/your/script.sh

Here:
- 0 represents the minute (0-59) when the cron job should run.
- 17 represents the hour (0-23) when the cron job should run (5 PM).
- * represents any value for the day of the month and month.
- 5 represents Friday (0-6, where Sunday is 0 and Saturday is 6).
- /path/to/your/script.sh represents the actual path to your script.
Save the file and exit the editor.

The above cron schedule expression will run the script at 5 PM every Friday. Make sure to replace /path/to/your/script.sh with the actual path to your script.

Once you save the crontab file, the cron daemon will automatically schedule and execute the script according to the specified schedule. 

You can check the system logs (/var/log/syslog or /var/log/cron) to verify that the cron job is running as expected.

--------------------------------------------

Good To Read regarding Linux file systems and Windows Drives:

In some ways, the concept of file systems and drives in Windows operating system can be related to each other, but they are not exactly the same.

In Windows, each drive (e.g., C:, D:, E:) typically represents a separate storage device or partition with its own file system. These drives can be formatted with different file systems like NTFS, FAT32, or exFAT. Each file system has its own characteristics and features.

Similarly, in Unix-like operating systems (including Linux), multiple file systems can exist on a single physical storage device. However, instead of assigning different drive letters to each file system, these systems are typically mounted at specific directories within a unified directory tree.

For example, in Linux, the root file system is typically mounted at the root directory ("/"), and additional file systems can be mounted at various directories such as "/home", "/var", or "/mnt/data". Each mounted file system behaves as a separate entity within the overall directory structure.

So, while both Windows drives and Unix-like file systems serve the purpose of organizing and managing data on storage devices, they differ in how they are represented and accessed. Windows uses drive letters to represent separate storage devices or partitions, while Unix-like systems use a unified directory tree and mount points to represent and access different file systems on a single storage device.
-------------------------------------------------