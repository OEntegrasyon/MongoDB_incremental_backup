Name:           mongoInc-backup
Version:        0.1
Release:        1%{?dist}
Summary:        A script that provides mongodb incremental backup 

License:      GNU
Group:        System
URL:          https://github.com/OEntegrasyon  
Source0:      mongoInc-backup-0.1.tar.gz
Packager:   Ergün Elvan Bilsel
Requires:   bash
Requires:   jq >= 1.6
Requires:   dialog >= 1.3
Requires:   mongodb-org-tools >= 4.4.4
Requires:   mongodb-org-shell >= 4.4.7

%description
Deneme

%prep
if [ -d /etc/mongobackup/ ]; then
    mv /etc/mongobackup/  /etc/mongobackup.old/
fi
mkdir -p $RPM_BUILD_ROOT/etc/mongobackup/
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/usr/share/licenses/mongoInc-backup/
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/mongoInc-backup/

cp /home/ergunbilsel/PycharmProjects/mongoinc/mongoInc-backup-0.1/mongodb-backup.config $RPM_BUILD_ROOT/etc/mongobackup/
cp /home/ergunbilsel/PycharmProjects/mongoinc/mongoInc-backup-0.1/mongodb-replica  $RPM_BUILD_ROOT/usr/local/bin/
cp /home/ergunbilsel/PycharmProjects/mongoinc/mongoInc-backup-0.1/mongodb-restore  $RPM_BUILD_ROOT/usr/local/bin/ 
cp /home/ergunbilsel/PycharmProjects/mongoinc/mongoInc-backup-0.1/COPYING  $RPM_BUILD_ROOT/usr/share/licenses/mongoInc-backup/
cp /home/ergunbilsel/PycharmProjects/mongoinc/mongoInc-backup-0.1/AUTHORS  $RPM_BUILD_ROOT/usr/share/doc/mongoInc-backup/
cp /home/ergunbilsel/PycharmProjects/mongoinc/mongoInc-backup-0.1/README  $RPM_BUILD_ROOT/usr/share/doc/mongoInc-backup/
cp /home/ergunbilsel/PycharmProjects/mongoinc/mongoInc-backup-0.1/THANKS  $RPM_BUILD_ROOT/usr/share/doc/mongoInc-backup/
%post
if [ -d /opt/mongo/ ]; then
    mv /opt/mongo/ /opt/mongo.old/
fi


#%clean
#rm -rf $RPM_BUILD_ROOT/etc/mongobackup/
#rm -rf $RPM_BUILD_ROOT/usr/local/bin
#rm -rf $RPM_BUILD_ROOT/usr/share/mongoInc-backup








%files
%attr(0600, root, root) /etc/mongobackup/mongodb-backup.config
%attr(0744, root, root) /usr/local/bin/mongodb-replica
%attr(0744, root, root) /usr/local/bin/mongodb-restore
%attr(0400, root, root) /usr/share/licenses/mongoInc-backup
%attr(0400, root, root) /usr/share/doc/mongoInc-backup


%doc AUTHORS README THANKS
%license COPYING


%changelog
* Tue Jul 27 2021 Ergün Elvan Bilsel <bilselergun@gmail.com>
 - This script is used to take incremental backups and upload them again. The developers disclaim responsibility.
