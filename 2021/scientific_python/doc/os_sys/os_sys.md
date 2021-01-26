---
layout :  page
title  :  Python Os integration
date   :  2021/01/20  
permalink: /sys/sys/
---


# Introduction #

In this unit, we will introduce some useful *python* modules to communicate with
the operating system. This set of functions will allow the user to easily
manipulate the **files and folders** of the your system. Using the module `os`,
a user will benefit from all the OS-dependent tasks. The second module is `sys`
will help us manipulate the arguments of program, change the input or output
stream. Finally, we will dive in the `argparse` module for deep control of the
program arguments.

# Table of Contents #

1. [Using the os functionality](#OsModule)
 - [Introduction](#osIntro)
 - [Basic Function](#osBasic)
 - [List Content](#osList)
 - [Change Working Directory](#oscwd)
 - [Directory Structure](#osStructure)
 - [Remove Structure](#osRemove)
 - [Example](#osExample)

2. [Python sys module](#SysModule)
3. [Custom arguments](#argsParse)



# Using the Os functionality #
<a name="#OsModule"> </a>

## Introduction ##
<a name="#osIntro"></a>

In this section, we will learn about the `os` module, which offer a clean
API to communicate with your operating system. For this introduction we will
learn to simple concept

- How to import this module.
- print the **name** of your system.


The following listing will print the name of your operating system in the
console:

```python
#import the os module
import os

#use the attribute name to print the system name
print("The system name is {}".format(os.name))
```


## Basic Function ##
<a name="#osBasci"> </a>

For a simple, case let's imagine that we want to know where our code is being
executed. Otherwise know as the **The working directory**. The `os` module
offer a *getter* to easily get the name of this folder as a string


- `os.getcwd()`: will return string representing the name of the current
directory


```python
import os


#print the working directory
print("I'm on {} folder".format(os.getcwd()))
```



Another useful information we would like to know is the **content** of a given
folder.

## List folder content ##
<a name="osList"> </a>
Another useful function it **get the content** of a directory and the names of
its *files* and *folders*. To illustrate this example, let's suppose we have
list of clients that are stored according to their town.


<img src="/assets/tree_clients.png" width="40%" height="100">      


## Change working directory ##
<a name="#oswd"> </a>


## Create a directory Structure ##
<a name="osStructure"> </a>


## Remove Structure ##
<a name="osRemove"></a>


## Example ##
<a name="osExample"> </a>

# Python sys module #
<a name="#SysModule"> </a>


# Custom arguments #
<a name="#argsParse"> </a>


