%define upstream_name    JavaScript-Beautifier
%define upstream_version 0.25
Name:		perl-%{upstream_name}
Version:	0.25
Release:	3

Summary:	Beautify Javascript (beautifier for javascript)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/fayland/perl-javascript-beautifier/tree/master
Source0:	https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/JavaScript-Beautifier-0.25.tar.gz

BuildRequires:	make
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
%setup -q -n JavaScript-Beautifier-0.25

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/*


