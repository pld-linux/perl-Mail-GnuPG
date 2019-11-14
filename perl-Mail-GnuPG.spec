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
Version:	0.23
Release:	1
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9661f16109d957720a924fa58ed8b09d
URL:		http://search.cpan.org/dist/Mail-GnuPG/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-GnuPG-Interface
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-MailTools
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
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Mail/*.pm
%{_mandir}/man3/*
