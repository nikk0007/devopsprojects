we will create an app that will send predefined sample logs(from some url) and store them in a file.

tail -f /dev/null  ==> to keep the pod running even after the file is downloaded.

to check inside the pod:
k exec -it myapp-6c977769b4-xglwj -- ls /var/log/

To see top 10 lines of the log file from the container:
k exec -it myapp-6c977769b4-7pmrc -- cat /var/log/myapp.log | head -n 10

Our fluentbit daemonset will fetch the logs of our custom app and then push them to elasticsearch.

Fluentbit volume paths are according to Docker-desktop. They can be modified as per requirement.
=============================================================================

to check all elasticsearch indexes manually to verify if it is working fine:(elasticsearch is exposed as a nodeport service on port 31349). It should show our "my_app_logs" index which we have configured in fluentbit config file.
curl -X GET "http://localhost:31349/_cat/indices?v"

To display an index with name my-app-logs:
curl -X GET "http://localhost:31349/my-app-logs/_search?pretty"

==============================================================================

In kibana, we can create an index pattern to see the logs.

===============================================================================