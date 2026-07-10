%global tl_name ellipsis
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Fix uneven spacing around ellipses in LaTeX text mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ellipsis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a simple package that fixes a problem in the way LaTeX handles
ellipses: it always puts a tiny bit more space after \dots in text mode
than before it, which results in the ellipsis being off-center when used
between two words.

