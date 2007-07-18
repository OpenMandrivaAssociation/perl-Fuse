%define	module	Fuse
%define	name	perl-%{module}
%define	version	0.08
%define	release %mkrel	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Write filesystems in Perl using FUSE
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DP/DPAVLIN/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  fuse-devel
BuildRequires:  fuse
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
This lets you implement filesystems in perl, through the FUSE (Filesystem in
USErspace) kernel/lib interface.

FUSE expects you to implement callbacks for the various functions.

In the following definitions, "errno" can be 0 (for a success), -EINVAL,
-ENOENT, -EONFIRE, any integer less than 1 really.

You can import standard error constants by saying something like "use POSIX
qw(EDOTDOT ENOANO);".

Every constant you need (file types, open() flags, error values, etc) can be
imported either from POSIX or from Fcntl, often both. See their respective
documentations, for more information.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc AUTHORS Changes README
%{perl_vendorarch}/%{module}.pm
%{perl_vendorarch}/auto/%{module}
%{_mandir}/man3/*

