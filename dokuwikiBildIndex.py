#!/usr/bin/env python3                                                           
# -*- coding: utf-8 -*-                                                         
""" write a DokuWike Page with Pictureinfos """                                                                                
                                                             
                                                                                
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
                    text2 = '| | '
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
    elif args.dirname != "Nothing-to-dir":
        # write one DokuWikipage to given parameters
        PicHelper.write_dir_to_wikipicturelist(dirname)
    else:
        print(" Error less Parameter.... use --help or -h")


if __name__ == "__main__":
    main()
