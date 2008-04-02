#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	GnuPG
Summary:	Mail::GnuPG - Process email with GPG
Summary(pl.UTF-8):	Mail::GnuPG - przetwarzanie poczty elektronicznej przy użyciu GPG
Name:		perl-Mail-GnuPG
Version:	0.15
Release:	1
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7f18a7af0d8998a3f362e8e12abe16a2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-GnuPG-Interface
BuildRequires:	perl-MailTools
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Use GnuPG::Interface to process or create PGP signed or encrypted
email.

%description -l pl.UTF-8
GnuPG::Interface służy do przetwarzania i tworzenia podpisanej lub
zaszyfrowanej PGP poczty elektronicznej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Mail/*.pm
%{_mandir}/man3/*
