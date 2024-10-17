Name:		texlive-longfbox
Version:	39028
Release:	2
Summary:	Draw framed boxes with standard CSS attributes that can break over multiple pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/longfbox
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longfbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longfbox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The longfbox package provides framed boxes that can be
customized using standard CSS attributes. It was written to
support precise rendering of Madoko documents in LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/longfbox
%doc %{_texmfdistdir}/doc/latex/longfbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
