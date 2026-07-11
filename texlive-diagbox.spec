%global tl_name diagbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Table heads with diagonal lines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/diagbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diagbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package's principal command, \diagbox, takes two arguments (texts
for the slash-separated parts of the box), and an optional argument with
which the direction the slash will go, the box dimensions, etc., may be
controlled. The package also provides \slashbox and \backslashbox
commands for compatibility with the slashbox package, which it
supersedes. diagbox depends on e-TeX as well as the packages array,
calc, fp, keyval, and pict2e.

