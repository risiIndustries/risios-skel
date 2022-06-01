Name:           risios-skel
Version:        36
Release:        %autorelease
Summary:        risiOS /etc/skel
License:        GPL3
URL:            http://risi.io/
Source0:        https://github.com/risiOS/risios-skel/archive/refs/heads/main.tar.gz
BuildArch:      noarch
 
 
%description
Provides some extra files by default in the home dir.
 
%prep
%autosetup -n %{name}-main

%build
%install
%{__mkdir_p} %{buildroot}%{_sysconfdir}/skel
cp -a skel %{buildroot}%{_sysconfdir}

%files
%dir %{_sysconfdir}/skel/.mozilla/.firefox
%dir %{_sysconfdir}/templates
 
%changelog
%autochangelog
