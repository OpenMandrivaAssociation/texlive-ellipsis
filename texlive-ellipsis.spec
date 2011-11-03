# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ellipsis
# catalog-date 2007-01-02 01:17:18 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-ellipsis
Version:	20070102
Release:	1
Summary:	Fix uneven spacing around ellipses in LaTeX text mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ellipsis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipsis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is a simple package that fixes a problem in the way LaTeX
handles ellipses: it always puts a tiny bit more space after
\dots in text mode than before it, which results in the
ellipsis being off-center when used between two words.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ellipsis/ellipsis.sty
%doc %{_texmfdistdir}/doc/latex/ellipsis/README
%doc %{_texmfdistdir}/doc/latex/ellipsis/ellipsis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ellipsis/ellipsis.dtx
%doc %{_texmfdistdir}/source/latex/ellipsis/ellipsis.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
