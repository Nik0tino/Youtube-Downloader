from pytube import Playlist
from pytube import YouTube
from pytube import *
import os
## == primarySection == ##

print(""" 
     *******                                 **                         ** **                 
/**////**                               /**                        /**//            ***** 
/**    /**  ******  ***     ** *******  /**  ******   ******       /** ** *******  **///**
/**    /** **////**//**  * /**//**///** /** **////** //////**   ******/**//**///**/**  /**
/**    /**/**   /** /** ***/** /**  /** /**/**   /**  *******  **///**/** /**  /**//******
/**    ** /**   /** /****/**** /**  /** /**/**   /** **////** /**  /**/** /**  /** /////**
/*******  //******  ***/ ///** ***  /** ***//****** //********//******/** ***  /**  ***** 
///////    //////  ///    /// ///   // ///  //////   ////////  ////// // ///   //  /////  
\n
\n
\n

 """)

print("[1] Video Download\n[2] Playlist Download")
option = input("\nSelect A Type : ")

## == Video Download Option == ##

if option == "1":
     vidurl = input("Entre video link : ")
     os.system("cls")
     print("Downloading")
     video = YouTube(vidurl).streams.get_highest_resolution().download()
## == Playlist Download Option == ##

if option == "2":
     url1 = input("Entre playlist url : ")
     playlist = Playlist(url1)
     os.system("cls") # clear
     for pd in playlist.videos:
          print("Downloading ",pd.title)
          pds = pd.streams.get_highest_resolution()
          pds.download()