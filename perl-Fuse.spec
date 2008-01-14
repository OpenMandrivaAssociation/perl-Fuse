%define	module	Fuse
%define	name	perl-%{module}
%define	version	0.09
%define	release %mkrel	2

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

