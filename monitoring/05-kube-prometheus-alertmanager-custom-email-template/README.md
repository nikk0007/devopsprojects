this project is continued from the previous project i.e. 04-kube-prometheus-alertmanager-gmail-receiver.
So, please setup gmail alerts using the previous project as a pre-requisite.

aletmanager.config and alertmanager.templateFiles has been modified in values.yaml and we are able to receive the HTML emael template response on our gmail id.

go in helm folder > helm install myprometh .
===========================================================

We can also modify the email receiver inline like below:

route:
      group_by: ['job']
      receiver: email_platform
      routes:
      - receiver: 'null'
        matchers:
          - alertname =~ "InfoInhibitor|Watchdog"
      - receiver: email_platform
        continue: true
    receivers:
    - name: email_platform

      # override subject line and html content 
      email_configs:
      - to: platform@k3s
        send_resolved: true
        headers:
          subject: "{{ .Status | toUpper }} {{ .CommonLabels.env }}:{{ .CommonLabels.cluster }} {{ .CommonLabels.alertname }}"

        html: |-
          <h3>You have the following alerts:</h3>
          {{ range .Alerts }}
          <p><b>{{.Labels.alertname}}</b>
            <ul>{{ range .Annotations.SortedPairs }}
            <li>{{ .Name }} = {{ .Value }}</li>
            {{ end }}</ul>
            <ul>{{ range .Labels.SortedPairs }}
            <li>{{ .Name }} = {{ .Value }}</li>
            {{ end }}</ul>
            {{ .GeneratorURL }}</p>
          {{ end }}
         
        text: |-
          You have the following alerts:
          {{ range .Alerts }}
          * {{.Labels.alertname}}
            {{ range .Annotations.SortedPairs }}
            {{ .Name }} = {{ .Value }}
            {{ end }}
            {{ range .Labels.SortedPairs }}
            {{ .Name }} = {{ .Value }}
            {{ end }}
            {{ .GeneratorURL }}
          {{ end }}

    - name: 'null'
    templates:
    - '/etc/alertmanager/config/*.tmpl'
=============================================================

the temp folder has various templates with increasing complexity from 1 to 5.
this fodler also has the default prometheus email html template.
we can use these templates and paste in values.yaml in alertmanager.templateFiles section.
=================================================================