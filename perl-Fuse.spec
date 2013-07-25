%define	upstream_name	 Fuse
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.15
Release:	1

Summary:	Write filesystems in Perl using FUSE
License:	GPLv2+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/D/DP/DPAVLIN/Fuse-0.15.tar.gz

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.130.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 688747
- update to new version 0.13

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1
+ Revision: 677343
- update to new version 0.12

* Tue Mar 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.110.0-1
+ Revision: 641128
- update to 0.11

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 409018
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.09-4mdv2009.0
+ Revision: 257076
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.09-2mdv2008.1
+ Revision: 151380
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - description is not a programmer manual

* Thu Dec 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2008.1
+ Revision: 115858
- update to new version 0.09

* Thu Jul 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.0
+ Revision: 53372
- new version

  + Funda Wang <fwang@mandriva.org>
    - New version

* Mon Apr 30 2007 Michael Scherer <misc@mandriva.org> 0.06-4mdv2008.0
+ Revision: 19631
- rebuild
- use %%rel


* Mon Jan 23 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-3mdk
- Add BuildRequires

* Fri Jan 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.06-2mdk
- fix requires

* Fri Jan 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.06-1mdk
- initial Mandriva release


