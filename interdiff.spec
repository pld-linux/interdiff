Summary:	A utility to generate incremental patches from pristine patches
Summary(pl):	Narzêdzie generuj±ce patche przyrostowe ze zwyk³ych
Name:		interdiff
Version:	0.0.10
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://people.redhat.com/twaugh/interdiff/stable/%{name}-%{version}.tar.gz
# Source0-md5:	339cfade7b3d96585fb579f442b7084e
URL:		http://people.redhat.com/twaugh/interdiff/
Requires:	diffutils
Requires:	patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
interdiff creates a unified diff that expresses the difference between
two unified diffs (patches created with the -u option to diff). The
diffs must both be relative to the same files. For best results, the
diffs must have at least three lines of context.

%description -l pl
interdiff tworzy zunifikowany diff, który wyra¿a ró¿nice pomiêdzy
dwoma zunifikowanymi diffami (patchami zrobionymi przez diff -u). Oba
diffy musz± siê odnosiæ do tych samych plików. Dla uzyskania
najlepszego efektu, diffy musz± mieæ co najmniej 3 linie kontekstu.

%prep
%setup -q

%build
%{__make} interdiff CFLAGS="%{rpmcflags}"

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
