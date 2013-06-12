#!/usr/bin/env python3                                                           
# -*- coding: utf-8 -*-                                                         
""" 
write a DokuWike Page with Pictureinfos 

********************************************
GPL License
********************************************
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
    der GNU General Public License, wie von der Free Software Foundation,
    Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren
    veröffentlichten Version, weiterverbreiten und/oder modifizieren.

    Dieses Programm wird in der Hoffnung, dass es nützlich sein wird, aber
    OHNE JEDE GEWÄHRLEISTUNG, bereitgestellt; sogar ohne die implizite
    Gewährleistung der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
    Siehe die GNU General Public License für weitere Details.

    Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
    Programm erhalten haben. Wenn nicht, siehe <http://www.gnu.org/licenses/>.

Author: Oerb
e-mail: bjoern@oerb.de
Date: 12.06.2013

"""                                                                             
                                                             
                                                                                
import os
import sys
import argparse

class Pictodokuwiki(object):
    def __init__(self, wikipath, picturepath):
        """
        Example:
        central = 084-koebenerstr-gruenewald:bilddokumentation:0084-2013-04-09-begehung:'
        picturepath = './' 
        """
        if self.isdir(wikipath):
            self.central = wikipath
        if self.isdir(picturepath):
            self.dirlist = os.listdir(picturepath)
        self.picsize = '500'

    def isdir(self, path):
        """
        Test if Path is Directory
        """
        if os.path.isdir(path):
            return True
        else:
            print("[Error] No such file or directory: %s  ( -h --help )" %path)
            quit()

    def get_imgdict(self):
        """
        iterates nextlevel directorys and collects
        the inhereted Imagefilenames in a dict. 
        dict-key is = dirname
        """    
        fileinf = {}
        for element in self.dirlist:
            path = './' + element + '/'
            if os.path.isdir(path):
                fileinf[element] = os.listdir(path)
        
        return fileinf

    def write_alldir_to_wikipicturelists(self):
        """
        creates separate DokuWikePages for every
        Directory as a List of images for Textdokumantation
        """    
        fileinf = self.get_imgdict()
        for key in fileinf.keys():
            filepath = './' + key + '.txt'
            datei = open(filepath, 'w')
            path = './' + key + '/'
            header = '^ Datum | ' + key + ' |'
            print(header, file=datei)
            print('', file=datei)
            for element in fileinf[key]:
                text = '| {{:' + self.central + element + '?' + self.picsize + '|}} |'
                text2 = ' | | '
                print(text, file=datei)
                print(text2, file=datei)

            datei.close() 
                
    def write_dir_to_wikipicturelist(self, dirname):
        """
        creates DokuWikePage for given Directory 
        as a List of images for Textdokumantation
        """    
        info = False
        fileinf = self.get_imgdict()
        for key in fileinf.keys():
            if key == dirname:
                info = True
                filepath = './' + key + '.txt'
                datei = open(filepath, 'w')
                path = './' + key + '/'
                header = '^ Datum | ' + key + ' |'
                print(header, file=datei)
                print('', file=datei)
                for element in fileinf[key]:
                    text = '| {{:' + self.central + element + '?' + self.picsize + '|}} |'
                    text2 = ' | | '
                    print(text, file=datei)
                    print(text2, file=datei)

                datei.close()
        if not info:
            text = "There is no Directory: " + dirname
            print(text)


def main():
    # some Options on Toolstart
    parser = argparse.ArgumentParser()
    parser.add_argument("-wp", "--wikipath=", 
            dest="wikipath", 
            help= "Example '084-koebenerstr-gruenewald:bilddokumentation:0084-2013-04-09-begehung:'",
            default= "",) 
    parser.add_argument("-pp", "--picturepath", 
            dest="picturepath", 
            help="Example './' ",
            default= './',)
    parser.add_argument("-d", "--directory", 
            dest="dirname", 
            help="Example '2013-05-06'",
            default= "Nothing-to-dir",)
    parser.add_argument("-a", "--alldirectory",
            dest="alldirectory",
            help="include all following Directorys from --directory",
            action = 'store_true',)
    # parse the options
    args = parser.parse_args()
    # get option infos
    wikipath = args.wikipath
    picturepath = args.picturepath
    dirname = args.dirname
    # instantiate Pictodokuwiki and include two Parameters
    PicHelper = Pictodokuwiki(wikipath, picturepath)
    if args.alldirectory:
        PicHelper.write_alldir_to_wikipicturelists()
    elif args.directory != "Nothing-to-dir":
        # write one DokuWikipage to given parameters
        PicHelper.write_dir_to_wikipicturelist(dirname)
    else:
        print(" Error less Parameter.... use --help or -h")


if __name__ == "__main__":
    main()