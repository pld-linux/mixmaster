Description: Anonymous remailer
Name: mixmaster
Version: 2.0.3
Release: 1
Copyright: GPL
Group: Applications/Networking
Source: ftp.hacktic.nl/pub/replay/pub/remailer/mixmaster-2.0.3.tar.gz
Patch: mixmaster-2.0.3-1-linux.patch



%prep 
%setup -c 
%setup -T -D -a 0
tar -xvf mix-2.0.3.tar
%patch -p0

%build
cd ./Mix/Src
make

%install
if [ ! -d /usr/lib/mixmaster ]; then
	mkdir /usr/lib/mixmaster
fi
cd ./Mix
cp ./destination.block	/usr/lib/mixmaster
cp ./mix.key		/usr/lib/mixmaster
cp ./mixmaster		/usr/bin              
cp ./mixmaster.conf	/usr/lib/mixmaster
cp ./pubring.mix	/usr/lib/mixmaster
cp ./source.block	/usr/lib/mixmaster 
cp ./type2.list		/usr/lib/mixmaster
cp ./mixmaster.1       /usr/man/man1

%files
%dir /usr/lib/mixmaster
%doc ./Mix/README
%doc ./Mix/README.client
%doc ./Mix/README.remailer
%doc ./Mix/README.chaining
%doc ./Mix/README.changes
%doc ./Mix/mix.help
/usr/bin/mixmaster
/usr/lib/mixmaster/destination.block
/usr/lib/mixmaster/mix.key
%config /usr/lib/mixmaster/mixmaster.conf
/usr/lib/mixmaster/pubring.mix
/usr/lib/mixmaster/source.block
/usr/lib/mixmaster/type2.list
/usr/man/man1/mixmaster.1
