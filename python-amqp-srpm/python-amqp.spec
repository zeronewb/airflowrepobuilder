%{?scl:%scl_package python-amqp}
%{!?scl:%global pkg_name %{name}}

%global srcname amqp

%define version 1.4.7
%define release 1

Summary: Low-level AMQP client for Python (fork of amqplib)
Name: %{?scl_prefix}python-amqp
Version: 1.4.7
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ask Solem <pyamqp@celeryproject.org>
Url: http://github.com/celery/py-amqp
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
=====================================================================
 Python AMQP 0.9.1 client library
=====================================================================

:Version: 1.4.7
:Web: http://amqp.readthedocs.org/
:Download: http://pypi.python.org/pypi/amqp/
:Source: http://github.com/celery/py-amqp/
:Keywords: amqp, rabbitmq

About
=====

This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by `kombu`_ as a pure python
alternative when `librabbitmq`_ is not available.

This library should be API compatible with `librabbitmq`_.

.. _amqplib: http://pypi.python.org/pypi/amqplib
.. _Celery: http://celeryproject.org/
.. _kombu: http://kombu.readthedocs.org/
.. _librabbitmq: http://pypi.python.org/pypi/librabbitmq

Differences from `amqplib`_
===========================

- Supports draining events from multiple channels (``Connection.drain_events``)
- Support for timeouts
- Channels are restored after channel error, instead of having to close the
  connection.
- Support for heartbeats

    - ``Connection.heartbeat_tick(rate=2)`` must called at regular intervals
      (half of the heartbeat value if rate is 2).
    - Or some other scheme by using ``Connection.send_heartbeat``.
- Supports RabbitMQ extensions:
    - Consumer Cancel Notifications
        - by default a cancel results in ``ChannelError`` being raised
        - but not if a ``on_cancel`` callback is passed to ``basic_consume``.
    - Publisher confirms
        - ``Channel.confirm_select()`` enables publisher confirms.
        - ``Channel.events['basic_ack'].append(my_callback)`` adds a callback
          to be called when a message is confirmed. This callback is then
          called with the signature ``(delivery_tag, multiple)``.
    - Exchange-to-exchange bindings: ``exchange_bind`` / ``exchange_unbind``.
        - ``Channel.confirm_select()`` enables publisher confirms.
        - ``Channel.events['basic_ack'].append(my_callback)`` adds a callback
          to be called when a message is confirmed. This callback is then
          called with the signature ``(delivery_tag, multiple)``.
- Support for ``basic_return``
- Uses AMQP 0-9-1 instead of 0-8.
    - ``Channel.access_request`` and ``ticket`` arguments to methods
      **removed**.
    - Supports the ``arguments`` argument to ``basic_consume``.
    - ``internal`` argument to ``exchange_declare`` removed.
    - ``auto_delete`` argument to ``exchange_declare`` deprecated
    - ``insist`` argument to ``Connection`` removed.
    - ``Channel.alerts`` has been removed.
    - Support for ``Channel.basic_recover_async``.
    - ``Channel.basic_recover`` deprecated.
- Exceptions renamed to have idiomatic names:
    - ``AMQPException`` -> ``AMQPError``
    - ``AMQPConnectionException`` -> ConnectionError``
    - ``AMQPChannelException`` -> ChannelError``
    - ``Connection.known_hosts`` removed.
    - ``Connection`` no longer supports redirects.
    - ``exchange`` argument to ``queue_bind`` can now be empty
      to use the "default exchange".
- Adds ``Connection.is_alive`` that tries to detect
  whether the connection can still be used.
- Adds ``Connection.connection_errors`` and ``.channel_errors``,
  a list of recoverable errors.
- Exposes the underlying socket as ``Connection.sock``.
- Adds ``Channel.no_ack_consumers`` to keep track of consumer tags
  that set the no_ack flag.
- Slightly better at error recovery

Further
=======

- Differences between AMQP 0.8 and 0.9.1

    http://www.rabbitmq.com/amqp-0-8-to-0-9-1.html

- AMQP 0.9.1 Quick Reference

    http://www.rabbitmq.com/amqp-0-9-1-quickref.html

- RabbitMQ Extensions

    http://www.rabbitmq.com/extensions.html

- For more information about AMQP, visit

    http://www.amqp.org

- For other Python client libraries see:

    http://www.rabbitmq.com/devtools.html#python-dev

.. image:: https://d2weczhvl823v0.cloudfront.net/celery/celery/trend.png
    :alt: Bitdeli badge
    :target: https://bitdeli.com/free


%prep
%setup -q -n %{srcname}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}


%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc Changelog LICENSE README.rst
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.4.7-0.1
- Build from setup.py
- Add python(abi) dependency
