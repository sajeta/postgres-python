# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:49:18 2019

@author: marin
"""
#!/usr/bin/python

from configparser import ConfigParser

CONFIG_FILE = 'config.ini'
 
#Database name, host, username and password are in "config.ini" file
#Changes should be made there

#returns name, host, username and password of postgres database
def config(filename = CONFIG_FILE, section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        
    #print(db)
    return db

#returns name of the table, stored in config.ini
def tableInfo(filename = CONFIG_FILE, section='table_info'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    tableInfo = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            tableInfo[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        
    return tableInfo

#returns name of the excel file, stored in config.ini
def excelInfo(filename = CONFIG_FILE, section='excel_info'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    excelInfo = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            excelInfo[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        
    return excelInfo