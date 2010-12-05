%define name hid-device-dump
%define version 9.04.04
%define release %mkrel 2

Summary: hid device dump tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.zip
License: GPLv3+
Group: System/X11
Url: http://sourceforge.net/projects/hidtouchsuite/
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
