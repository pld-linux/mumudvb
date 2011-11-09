Summary:	DVB IPTV streaming software
Name:		mumudvb
Version:	1.6
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://mumudvb.braice.net/mumudvb/mumudvb-1.6/%{name}_%{version}.tar.gz
# Source0-md5:	a463af541d0395ba3a2286e92f080615
URL:		http://mumudvb.braice.net/
BuildRequires:	linuxtv-dvb-apps-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MuMuDVB (Multi Multicast DVB) is a program for streaming TV over a
network originally based on dvbstream.
MuMuDVB can redistribute a stream from a DVB source (digital satellite
television, digital terrestrial television, or digital cable
television) on a network, in multicast or in HTTP unicast. Its main
feature is to take a whole transponder and put each channel on a
different multicast group. MuMuDVB have a low memory and CPU footprint.

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p doc/%{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT%{_mandir}/man8

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/configuration_examples doc/html doc/logo doc/*.txt doc/TODO scripts/debian
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
