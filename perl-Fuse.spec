%define	module	Fuse
%define	name	perl-%{module}
%define	version	0.06
%define	rel	4

Name:		%{name}
Summary:	Fuse module for perl
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DP/DPAVLIN/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  fuse-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{module} perl module

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc AUTHORS Changes README
%{perl_vendorarch}/%{module}.pm
%{perl_vendorarch}/auto/%{module}
%{_mandir}/man3/*

