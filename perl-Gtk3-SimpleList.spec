%define modname	Gtk3-SimpleList
%define	modver	0.15

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	3

Summary:	Perl helper module for Gtk3
License:	LGPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	%{modname}-%{modver}.tar.gz

BuildArch:	noarch

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Gtk3)
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300

%description
This module provides a helper for Gtk3.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%files
%doc COPYING Changes META.json META.yml MYMETA.yml README
%{perl_vendorlib}/Gtk3/SimpleList*
%{_mandir}/*/*
