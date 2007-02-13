Summary:	A utility to generate incremental patches from pristine patches
Summary(pl.UTF-8):	Narzędzie generujące patche przyrostowe ze zwykłych
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
interdiff creates a unified diff that expresses the difference between
two unified diffs (patches created with the -u option to diff). The
diffs must both be relative to the same files. For best results, the
diffs must have at least three lines of context.

%description -l pl.UTF-8
interdiff tworzy zunifikowany diff, który wyraża różnice pomiędzy
dwoma zunifikowanymi diffami (patchami zrobionymi przez diff -u). Oba
diffy muszą się odnosić do tych samych plików. Dla uzyskania
najlepszego efektu, diffy muszą mieć co najmniej 3 linie kontekstu.

%prep
%setup -q

%build
%{__make} interdiff \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install interdiff $RPM_BUILD_ROOT%{_bindir}/interdiff
install interdiff.1 $RPM_BUILD_ROOT%{_mandir}/man1/interdiff.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog TODO
%attr(755,root,root) %{_bindir}/interdiff
%{_mandir}/man1/interdiff.1*
