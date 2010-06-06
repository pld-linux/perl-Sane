#
# Conditional build:
%bcond_with	tests		# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sane
Summary:	Sane - Perl extension for the SANE (Scanner Access Now Easy) Project
#Summary(pl.UTF-8):	
Name:		perl-Sane
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RA/RATCLIFFE/%{pdir}-%{version}.tar.gz
# Source0-md5:	db83b8b07e1263b78187c4349a183082
URL:		http://search.cpan.org/dist/Sane/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sane-backends-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Sane module allows a Perl developer to use SANE-compatible scanners.
Find out more about SANE at http://www.sane-project.org.

Most methods set $Sane::STATUS, which is overloaded to give either an integer
as dictated by the SANE standard, or the the corresponding message, as required.

Returns an array with the SANE_VERSION_(MAJOR|MINOR|BUILD) versions:

  join('.',Sane->get_version)



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Sane.pm
%dir %{perl_vendorarch}/auto/Sane/
%{perl_vendorarch}/auto/Sane/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Sane/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
