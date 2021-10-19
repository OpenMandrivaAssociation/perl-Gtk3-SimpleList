%define modname	Gtk3-SimpleList
%define	modver	0.18

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Perl helper module for Gtk3
License:	LGPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	https://cpan.metacpan.org/authors/id/T/TV/TVIGNAUD/Gtk3-SimpleList-%{modver}.tar.gz

BuildArch:	noarch

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Gtk3)
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300

%description
This module provides a helper for Gtk3.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

%install
%make_install

%files
%doc COPYING Changes META.json META.yml README
%{perl_vendorlib}/Gtk3/SimpleList*
%doc %{_mandir}/*/*
