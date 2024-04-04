IPyPass :closed_lock_with_key:
========================================================================================
|travis| |codacy| |maintained| |python| |mit| |open source|

.. |travis| image:: https://app.travis-ci.com/marshki/IPyPass.svg?branch=master
    :target: https://app.travis-ci.com/marshki/IPyPass
    :alt: Travis

.. |codacy| image:: https://app.codacy.com/project/badge/Grade/bd0bef504604497da04a41b58f09a44e
   :target: https://www.codacy.com/gh/marshki/IPyPass/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marshki/IPyPass&amp;utm_campaign=Badge_Grade
   :alt: Codacy

.. |maintained| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity
   :alt: Maintained

.. |python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
   :alt: Python

.. |mit| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/
   :alt: MIT

.. |open source| image:: https://badges.frapsoft.com/os/v3/open-source.svg?v=103
   :target: https://github.com/ellerbrock/open-source-badges/
   :alt: Open Source

IP-based password generator
---------------------------
Python3 utility (w/PySimpleGUI) for converting IPv4 IP address to an 8- or 12-bit password.
Modify the algo to suit your needs.

.. image:: https://github.com/marshki/IPyPass/blob/master/docs/IPyPass.png

Requirements
------------
Install required packages:

.. code-block:: Python3

    pip3 install -r requirements.txt

Usage
-----
From a shell (argument parser):

.. code-block:: Python3

    python3 ipypass.py --ip 192.168.1.1

From a shell (interactive):

.. code-block:: Python3

    python3 ipypass.py

then, at prompt, enter IPv4 address. Program will:

* validate address
* split address by '.'
* take 3rd octet and append `*`
* take 4th octet then add 8 or 12 and append `*`
  such that the string is 8 or 12 characters in length. 

For example: 

.. csv-table:: 
   :header: "IP address", "8-bit password", "12-bit password"
   :widths: 20, 20, 20

   "10.1.1.1", "1*9*****", "1*13*1******"
   "192.168.1.1", "1*9****", "1*13*168****"

Change Log
----------
CHANGELOG_

.. _CHANGELOG: https://github.com/marshki/IPyPass/blob/master/CHANGELOG.rst

License
-------
LICENSE_

.. _LICENSE: https://github.com/marshki/IPyPass/blob/master/LICENSE.txt
