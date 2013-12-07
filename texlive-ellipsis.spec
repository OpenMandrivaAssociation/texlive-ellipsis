# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ellipsis
# catalog-date 2007-01-02 01:17:18 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-ellipsis
Version:	20070102
Release:	3
Summary:	Fix uneven spacing around ellipses in LaTeX text mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ellipsis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.source.tar.xz
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
%{_texmfdistdir}/tex/latex/ellipsis/ellipsis.sty
%doc %{_texmfdistdir}/doc/latex/ellipsis/README
%doc %{_texmfdistdir}/doc/latex/ellipsis/ellipsis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ellipsis/ellipsis.dtx
%doc %{_texmfdistdir}/source/latex/ellipsis/ellipsis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070102-2
+ Revision: 751404
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070102-1
+ Revision: 718319
- texlive-ellipsis
- texlive-ellipsis
- texlive-ellipsis
- texlive-ellipsis

