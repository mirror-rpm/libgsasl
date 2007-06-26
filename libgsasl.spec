Name:           libgsasl
Version:        0.2.18 
Release:        3%{?dist}
Summary:        GNU SASL library 

Group:          System Environment/Libraries
License:        LGPL     
URL:            http://www.gnu.org/software/gsasl/
Source0:        http://josefsson.org/gsasl/releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libidn-devel
BuildRequires:  krb5-devel
BuildRequires: 	libntlm-devel

BuildRequires:  pkgconfig

%description
The library includes support for the SASL framework
and at least partial support for the CRAM-MD5, EXTERNAL,
GSSAPI, ANONYMOUS, PLAIN, SECURID, DIGEST-MD5, LOGIN,
and NTLM mechanisms.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README THANKS
%{_libdir}/libgsasl.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/gsasl*
%{_libdir}/libgsasl.so
%{_libdir}/pkgconfig/libgsasl.pc


%changelog
* Tue Jun 26 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.18-3
- added NTLM support
* Fri Jun 22 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.18-2
- fixed mixed-use-of-spaces-and-tabs
- fixed timestamps for header files 
- edited summary
* Thu Jun 21 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.18-1
- initial release

