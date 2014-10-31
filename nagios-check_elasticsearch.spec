Name:		nagios-check_elasticsearch
Version:	0.1
Release:	1%{?dist}
Summary:	Nagios plugin for retrieving cluster status and statistics from ElasticSearch

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/pall-valmundsson/nagios-check_elasticsearch
Source0:	%{name}-%{version}.tar.gz

Requires:	pynag >= 0.4.9
Requires:	python
Requires:	python-requests

BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

%description
Nagios plugin for retrieving cluster status and statistics from ElasticSearch

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 check_elasticsearch ${RPM_BUILD_ROOT}%{_libdir}/nagios/plugins/check_elasticsearch

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_libdir}/nagios/plugins/check_elasticsearch

%changelog

