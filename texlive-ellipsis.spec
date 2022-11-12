Name:		texlive-ellipsis
Version:	55418
Release:	1
Summary:	Fix uneven spacing around ellipses in LaTeX text mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ellipsis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a simple package that fixes a problem in the way LaTeX
handles ellipses: it always puts a tiny bit more space after
\dots in text mode than before it, which results in the
ellipsis being off-center when used between two words.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ellipsis
%doc %{_texmfdistdir}/doc/latex/ellipsis
#- source
%doc %{_texmfdistdir}/source/latex/ellipsis

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
