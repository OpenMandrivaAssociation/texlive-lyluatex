Name:		texlive-lyluatex
Version:	64967
Release:	1
Summary:	Commands to include lilypond scores within a (Lua)LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lyluatex
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lyluatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lyluatex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros for the inclusion of LilyPond
scores within LuaLaTeX. It calls LilyPond to compile scores,
then includes the produced files. Dependencies: currfile,
environ, graphicx, luaotfload, luaoptions, luatexbase,
metalogo, minibox, pdfpages, xkeyval.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/lyluatex
%{_texmfdistdir}/scripts/lyluatex
%doc %{_texmfdistdir}/doc/support/lyluatex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
