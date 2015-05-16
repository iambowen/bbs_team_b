Name:       bbs
Summary:    bbs application
Version:    1.0.0
Release:    1
License:    Proprietary
Group:      Applications/Internet
Vendor:     Myself
URL:        http://justdoit.com/
Source:     .

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:  noarch

Requires:   java-1.7.0-openjdk tomcat6

%description
This package installs the Resi REST Services with embedded server.

%pre

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/tomcat6/webapps/bbs_team_b/
cp -r ../SOURCES/* %{buildroot}/usr/share/tomcat6/webapps/bbs_team_b/

%clean
rm -rf %{buildroot}

%post
service tomcat6 restart

%preun

%files
%attr(0755,tomcat,tomcat)  			/usr/share/tomcat6/webapps/bbs_team_b/
