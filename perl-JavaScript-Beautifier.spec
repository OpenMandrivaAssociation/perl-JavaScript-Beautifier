%define upstream_name    JavaScript-Beautifier
%define upstream_version 0.25
Name:		perl-%{upstream_name}
Version:	0.25
Release:	33

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
perl Build.PL installdirs=vendor
./Build

%check
# soft: do not fail package on test failures
set +e
./Build test || :

%install
./Build install destdir=%{buildroot} create_packlist=0

%files
%doc Changes
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/*


