%define name hid-device-dump
%define version 9.04.04
%define release 3

Summary: hid device dump tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.zip
License: GPLv3+
Group: System/X11
Url: https://sourceforge.net/projects/hidtouchsuite/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tool to dump packets from hid devices.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/hidDeviceDump


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 9.04.04-2mdv2011.0
+ Revision: 611094
- rebuild

* Tue Mar 23 2010 Olivier Blin <oblin@mandriva.com> 9.04.04-1mdv2010.1
+ Revision: 526863
- initial hid-device-dump package
- create hid-device-dump

