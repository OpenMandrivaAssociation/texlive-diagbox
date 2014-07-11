# revision 24646
# category Package
# catalog-ctan /macros/latex/contrib/diagbox
# catalog-date 2011-11-24 16:48:22 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-diagbox
Version:	1.0
Release:	8
Summary:	Table heads with diagonal lines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diagbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package's principal command, \diagbox, takes two arguments
(texts for the slash-separated parts of the box), and an
optional argument with which the direction the slash will go,
and the box dimensions, etc., may vbe controlled. The package
also provides \slashbox and \backslashbox commands for
compatibility with the slashbox package, which it supersedes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/diagbox/diagbox.sty
%doc %{_texmfdistdir}/doc/latex/diagbox/diagbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/diagbox/diagbox.dtx
%doc %{_texmfdistdir}/source/latex/diagbox/diagbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750921
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 739585
- texlive-diagbox
- texlive-diagbox

