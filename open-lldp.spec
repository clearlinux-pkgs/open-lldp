#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : open-lldp
Version  : 1.0.1
Release  : 15
URL      : http://localhost/cgit/projects/open-lldp/snapshot/open-lldp-1.0.1.tar.gz
Source0  : http://localhost/cgit/projects/open-lldp/snapshot/open-lldp-1.0.1.tar.gz
Summary  : LLDP Agent with Data Center Bridging support
Group    : Development/Tools
License  : GPL-2.0
Requires: open-lldp-bin
Requires: open-lldp-config
Requires: open-lldp-lib
Requires: open-lldp-data
Requires: open-lldp-doc
BuildRequires : flex
BuildRequires : pkgconfig(libconfig)
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : readline-dev

%description
Link Layer Discovery Protocol (LLDP) Agent with
Data Center Bridging (DCB) for Intel(R) Network Connections
===========================================================

%package bin
Summary: bin components for the open-lldp package.
Group: Binaries
Requires: open-lldp-data
Requires: open-lldp-config

%description bin
bin components for the open-lldp package.


%package config
Summary: config components for the open-lldp package.
Group: Default

%description config
config components for the open-lldp package.


%package data
Summary: data components for the open-lldp package.
Group: Data

%description data
data components for the open-lldp package.


%package dev
Summary: dev components for the open-lldp package.
Group: Development
Requires: open-lldp-lib
Requires: open-lldp-bin
Requires: open-lldp-data
Provides: open-lldp-devel

%description dev
dev components for the open-lldp package.


%package doc
Summary: doc components for the open-lldp package.
Group: Documentation

%description doc
doc components for the open-lldp package.


%package lib
Summary: lib components for the open-lldp package.
Group: Libraries
Requires: open-lldp-data

%description lib
lib components for the open-lldp package.


%prep
%setup -q -n open-lldp-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510693693
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1510693693
rm -rf %{buildroot}
%make_install BASH_COMPLETION_DIR=/usr/share/bash-completion/completions/

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dcbtool
/usr/bin/lldpad
/usr/bin/lldptool

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/lldpad.service
/usr/lib/systemd/system/lldpad.socket

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/lldpad
/usr/share/bash-completion/completions/lldptool

%files dev
%defattr(-,root,root,-)
/usr/include/lldpad/clif.h
/usr/include/lldpad/clif_msgs.h
/usr/include/lldpad/clif_sock.h
/usr/include/lldpad/dcb_types.h
/usr/include/lldpad/dcbnl.h
/usr/include/lldpad/lldp_8021qaz_cmds.h
/usr/include/lldpad/lldp_8023_cmds.h
/usr/include/lldpad/lldp_basman_cmds.h
/usr/include/lldpad/lldp_dcbx_cmds.h
/usr/include/lldpad/lldp_evb_cmds.h
/usr/include/lldpad/lldp_mand_cmds.h
/usr/include/lldpad/lldp_med_cmds.h
/usr/include/lldpad/lldp_util.h
/usr/include/lldpad/lldpad.h
/usr/include/lldpad/lldpad_status.h
/usr/include/lldpad/netlink.h
/usr/include/lldpad/qbg_vdp_cmds.h
/usr/include/lldpad/rtnetlink.h
/usr/lib64/liblldp_clif.so
/usr/lib64/pkgconfig/liblldp_clif.pc
/usr/lib64/pkgconfig/lldpad.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblldp_clif.so.1
/usr/lib64/liblldp_clif.so.1.0.0
