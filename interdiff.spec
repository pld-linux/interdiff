Summary:	A utility to generate incremental patches from pristine patches
Name:		interdiff
Version:	0.0.9
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://people.redhat.com/twaugh/interdiff/stable/%{name}-%{version}.tar.gz
URL:		http://people.redhat.com/twaugh/interdiff/
Requires:	diffutils, patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
interdiff creates a unified diff that expresses the difference between
two unified diffs (patches created with the -u option to diff). The
diffs must both be relative to the same files. For best results, the
diffs must have at least three lines of context.

%prep
%setup -q -n interdiff

%build
%{__make} interdiff CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install interdiff $RPM_BUILD_ROOT/%{_bindir}/interdiff
install interdiff.1 %{buildroot}/%{_mandir}/man1/interdiff.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/interdiff
%{_mandir}/man1/interdiff.1*
