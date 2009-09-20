Name:           ocaml-sexplib
Version:        4.2.13
Release:        %mkrel 3
Summary:        OCaml library for converting OCaml values to S-expressions

Group:          Development/Other
License:        LGPLv2+ with exceptions and BSD
URL:            http://www.ocaml.info/home/ocaml_sources.html#sexplib310
Source0:        http://hg.ocaml.info/release/sexplib310/archive/sexplib310-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/sexplib310/archive/release-%{version}.tar.bz2 > sexplib310-release-${version}.tar.bz2
Patch0:         sexplib-4.0.1-unix-fix.patch
Patch1:         sexplib-lib_test-makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-type-conv >= 1.6.1
BuildRequires:  camlp4
BuildRequires:  dos2unix

Requires:       ocaml-type-conv

%description
This library contains functionality for parsing and pretty-printing
S-expressions. In addition to that it contains an extremely useful
preprocessing module for Camlp4, which can be used to automatically
generate code from type definitions for efficiently converting
OCaml-values to S-expressions and vice versa. In combination with the
parsing and pretty-printing functionality this frees users from having
to write their own I/O-routines for datastructures they
define. Possible errors during automatic conversions from
S-expressions to OCaml-values are reported in a very human-readable
way. Another module in the library allows you to extract and replace
sub-expressions in S-expressions.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n sexplib310-release-%{version}
%patch0 -p1
# lib_test is used by check and test is installed with a patched Makefile
cp -R lib_test test
%patch1 -p0
dos2unix LICENSE.Tywith

%build
make

%check
./lib_test/conv_test
./lib_test/sexp_test < lib_test/test.sexp

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE LICENSE.Tywith
%{_libdir}/ocaml/sexplib
%exclude %{_libdir}/ocaml/sexplib/*.a
%exclude %{_libdir}/ocaml/sexplib/*.cmxa
%exclude %{_libdir}/ocaml/sexplib/*.mli
%exclude %{_libdir}/ocaml/sexplib/*.ml

%files devel
%defattr(-,root,root,-)
%doc LICENSE LICENSE.Tywith COPYRIGHT README.txt
%doc test/
%{_libdir}/ocaml/sexplib/*.a
%{_libdir}/ocaml/sexplib/*.cmxa
%{_libdir}/ocaml/sexplib/*.mli
%{_libdir}/ocaml/sexplib/*.ml

