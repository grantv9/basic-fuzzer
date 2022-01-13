# fuzzer.py
Summer 2020 - Computer System Security
Grant V

## Overview
A Fuzzer helps software developers test code by automatically providing
target programs with malformed and unexpected information. This program
will identify reflected XSS bugs in target websites. See below for detailed
usage requirements/explanations.

## How To Use
Run this program on the command line without any arguments to use its default
mode. In this state, the Fuzzer will test https://www.cs.tufts.edu/comp/120/
hackme.php for reflected XSS vulnerabilities with the 'target' querystring.
It operates using HTTP GET requests.

This program can also run with optional flags. See explanations below:
   Flag              Behavior
    -h                Help: Get help using the Fuzzer
    -t                Target: Set the target URI
    -q                Query: Set the querysting parameter
    -l                Lists: A local file path to any fuzzing lists to use

## What has been correctly implemented
I believe that this assignment has been implemented correctly.

This program is capable of using Daniel Miessler's Fuzzing SecLists. Use
the optional `-l` flag to provide the path to the lists on your machine.

This program can test any other webpage for reflected XSS vulnerabilities. Use
the `-t` flag to pass the address you'd like to test.
