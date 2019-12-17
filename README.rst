=======
IPyPass
=======

.. image:: https://travis-ci.org/marshki/IPyPass.svg?branch=master
    :target: https://travis-ci.org/marshki/IPyPass

.. image:: https://api.codacy.com/project/badge/Grade/abec29ce4acc44b299628499dc55e632    
    :target: https://www.codacy.com/manual/marshki/IPyPass?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marshki/IPyPass&amp;utm_campaign=Badge_Grade

.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

.. image:: https://badges.frapsoft.com/os/v3/open-source.svg?v=103
   :target: https://github.com/ellerbrock/open-source-badges/


IP-based password generator
---------------------------
Python3 utility for converting IPv4 IP address to an 8- or 12-bit password.

.. image:: https://github.com/marshki/IPyPass/blob/master/docs/IPyPass.png

Requirements
------------
Install required packages: 
::
    pip3 install -r requirements.txt

Usage
-----
From a shell: 
::
    python3 ipypass.py

At prompt, enter IPv4 address. Program will: 

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

.. CHANGELOG: https://github.com/marshki/IPyPass/blob/master/CHANGES.rst

License
-------
LICENSE_

.. _LICENSE: https://github.com/marshki/IPyPass/blob/master/LICENSE.txt
