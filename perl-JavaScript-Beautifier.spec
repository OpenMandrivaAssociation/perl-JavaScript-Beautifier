%define upstream_name    JavaScript-Beautifier
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Beautify Javascript (beautifier for javascript)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/JavaScript/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module is mostly a Perl-rewrite of the
http://github.com/einars/js-beautify/tree/master/beautify.js manpage

You can check it through the http://jsbeautifier.org/ manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 654378
- update file list
- rebuild for updated spec-helper

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 483885
- update to 0.17

* Wed Sep 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 447603
- update to 0.16

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 444247
- update to 0.15

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 444025
- import perl-JavaScript-Beautifier


* Thu Sep 17 2009 cpan2dist 0.14-1mdv
- initial mdv release, generated with cpan2dist
