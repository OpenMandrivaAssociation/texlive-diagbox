Name:		texlive-diagbox
Version:	54080
Release:	1
Summary:	Table heads with diagonal lines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diagbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/diagbox
%doc %{_texmfdistdir}/doc/latex/diagbox
#- source
%doc %{_texmfdistdir}/source/latex/diagbox

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
