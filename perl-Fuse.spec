%define	upstream_name	 Fuse
%define	upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Write filesystems in Perl using FUSE
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DP/DPAVLIN/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  fuse-devel
BuildRequires:  fuse
BuildRequires:	perl-devel
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This lets you implement filesystems in perl, through the FUSE (Filesystem in
USErspace) kernel/lib interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorarch}/Fuse*
%{perl_vendorarch}/auto/Fuse*
%{_mandir}/man3/*
