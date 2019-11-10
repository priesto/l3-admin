#! /bin/bash

cat alertes_template/disk.txt | mailx -v \
    -r "Sender email address here" \
    -s "Alerte disque" \
    -S smtp="smtpz.univ-avignon.fr:25" \
    -S smtp-use-starttls \
    -S smtp-auth=login \
    -S smtp-auth-user="Sender email address here" \
    -S smtp-auth-password="Sender email password here" \
    -S ssl-verify=ignore \
    # Admin email here