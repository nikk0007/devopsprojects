we will create an app that will send predefined sample logs(from some url) and store them in a file.

tail -f /dev/null  ==> to keep the pod running even after the file is downloaded.

to check inside the pod:
k exec -it myapp-6c977769b4-xglwj -- ls /var/log/

To see top 10 lines of the log file from the container:
k exec -it myapp-6c977769b4-7pmrc -- cat /var/log/myapp.log | head -n 10

Our fluentd daemonset will fetch the logs of our custom app and then push them to some other desired file. For this we will be using file type match blocks. we can have multiple match blocks even for the same type if logs.







