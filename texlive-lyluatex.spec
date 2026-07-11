%global tl_name lyluatex
%global tl_revision 79159

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.6
Release:	%{tl_revision}.1
Summary:	Commands to include lilypond scores within a (Lua)LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/lyluatex
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lyluatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lyluatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros for the inclusion of LilyPond scores within
LuaLaTeX. It calls LilyPond to compile scores, then includes the
produced files. Dependencies: currfile, environ, graphicx, luaotfload,
luaoptions, luatexbase, metalogo, minibox, pdfpages, xkeyval.

