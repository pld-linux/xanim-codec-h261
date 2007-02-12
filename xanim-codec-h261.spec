Summary:	H.261 codec for XAnim
Summary(pl.UTF-8):   Kodek H.261 dla XAnima
Name:		xanim-codec-h261
Version:	1.0
Release:	1
License:	BSD (but no sources available)
Group:		X11/Applications/Graphics
# old dlls at http://xanim.polter.net/dlls/
Source1:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_h261_1.0_linuxELFx86c6.tgz
# Source1-md5:	72ccd7ca669a003b6ccd9c421fdcbfa9
Source2:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_h261_1.0_linuxELFalphaC6.tgz
# Source2-md5:	f7d9e398fc222ab9ce5b39c9f55f4995
Source3:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_h261_1.0_linuxELFppc.tgz
# Source3-md5:	56120050bf20d6cfb90f6b901027fd99
URL:		http://xanim.polter.net/
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
H.261 codec decompression DLL for XAnim.

%description -l pl.UTF-8
Biblioteka do dekompresji kodeka H.261 dla XAnima.

%prep
%ifarch %{ix86}
%setup -q -c -T -a1
%endif
%ifarch alpha
%setup -q -c -T -a2
%endif
%ifarch ppc
%setup -q -c -T -a3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_h261_*.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc h261.readme
%attr(755,root,root) %{_libdir}/xanim/vid_h261_*.xa
