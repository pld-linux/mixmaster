# $Revision: 1.2 $ $Date: 1999-12-15 11:11:19 $
Summary:    Mixmaster anonymous remailer.
Summary(pl):    Anonimowy remailer typu Mixmaster.
Name:       mixmaster
Version: 2.0.3
Release:    1
Copyright:  BSD
Group: 		Applications/Networking
Group(pl):  Narzêdzia/Sieciowe
Source: 	ftp://ftp.hacktic.nl/pub/replay/pub/remailer/%{name}-%{version}.tar.gz
Patch: mixmaster-2.0.3-1-linux.patch
BuildRoot:  /tmp/%{name}-%{version}-root

%description
Mixmaster is a remailer, allowing you to send an anonymous email.
Mixmaster is type II remailer, which is improved version of old
,,cypherpunks'' remailers.

%description -l pl
Mixmaster jest remailerem, pozwalaj±cym na wysy³anie anonimowej
poczty elektronicznej. Mixmaster to remailer typu II, stanowi±cy
ulepszon± wersjê remailerów ,,cypherpunk''. 

%prep 
%setup -q
%setup -T -D -a 0
tar -xvf mix-%{version}.tar
%patch -p0

%build
cd ./Mix/Src
make

%install
rm -rf $RPM_BUILD_ROOT
if [ ! -d %{_datadir}/mixmaster ]; then
	install -d %{_datadir}/mixmaster
fi
if [ ! -d /etc/mixmaster ]; then
	install -d %{_sysconfdir}/mixmaster
fi
cd ./Mix
install mixmaster {%_bindir}
install	mixmaster.conf %{_sysconfdir}
install destination.block \
		mix.key \
		pubring.mix	\
		source.block \
		type2.list \
		%{_datadir}/mixmaster
install mixmaster.1 %{_mandir}/man1
cp ./mixmaster.1       /usr/man/man1

gzip -9nf Mix/README Mix/mix.help ${_mandir}/man1/* || :

%files
%defattr(644,root,root,755)
%dir %{_datadir}/mixmaster
%dir %{_sysconfdir}/mixmaster
%config /etc/mixmaster/mixmaster.conf
%doc ./Mix/README*
%doc ./Mix/mix.help
%{_bindir}/mixmaster
%{_datadir}/mixmaster/destination.block
%{_datadir}/mixmaster/mix.key
%{_datadir}/mixmaster/pubring.mix
%{_datadir}/mixmaster/source.block
%{_datadir}/mixmaster/type2.list
%{_mandir}/man1/*
