FtpBackup Overview
====================

FtpBackup provides a simple way to backup all things in your folder to FTP.

FtpBackup take thesettings in the config file (default is `.ftpbackup`). And
you can add ignore files in `.ftpignore` and `.gitignore`.

Installation
------------
::

      pip install ftpbackup

Tested Platforms
-----------------

- Python:

 - 3.4-3.6

- Windows (32bit/64bit):

 - Only test on win10 now.


Getting started
---------------

1. Generate your config file ::

    ftpbk genconf

2. Edit your config file.
3. Add a new file called '`.ftpignore`' and edit it.
4. Backup your floder to FTP by the command. ::

    ftpbk backup

NOTE : Because `.ftpbackup` contains IP, password, and other pravite info. So
it's necessary to add it in `.gitignore` or `.ftpignore` manually. You can also
add it in git global ignore file list.

Set the config file (default: `.ftpconfig`)
-------------------------------------------

The default config is like below. ::

    {
        "protocol": "ftp", // string - Only 'ftp' now.
        "host": "localhost", // string - The hostname or IP address of the FTP server. Default: 'localhost'
        "encoding": "utf-8", // string - The encoding of the FTP server. Default: utf-8
        "port": 21, // integer - The port of the FTP server. Default: 21
        "user": "anonymous", // string - Username for authentication. Default: 'anonymous'
        "pass": "anonymous@", // string - Password for authentication. Default: 'anonymous@'
        "remote": ".", // string - The path on FTP to upload files.
        "local": ".", // string - The folder on local to be uploaded.
        "useGitIgnore": true, // bool - Use .gitignore in ignored file list.
        "gitIgnoreEncoding": "utf-8", // string - The encoding of .gitignore
        "useFtpIgnore": true, // bool - Use .ftpignore in ignored file list.
        "ftpIgnoreEncoding": "utf-8" // string - The encoding of .ftpignore
    }

Set the .ftpignore
------------------
The format of `.ftpignore` is just like `.gitignore`.

CLI
---
::

    usage: ftpbk [-h] {genconf,backup} ...

    Backup to FTP.

    optional arguments:
      -h, --help        show this help message and exit

    commands:
      {genconf,backup}

command 'genconf'::

    usage: ftpbk genconf [-h] [-F] [-f FILE]

    Generate a default config file.

    optional arguments:
      -h, --help            show this help message and exit
      -F, --force           overwrite the config file if it exists.
      -f FILE, --file FILE  assign the config file to be writed, default is
                            '.ftpbackup'.

command 'backup'::

    usage: ftpbk backup [-h] [-c CONFIGFILE]

    Backup all the file in the 'local' floder to 'remote' on ftp. You can change
    the config in config file(default is '.ftpbackup').

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIGFILE, --conf CONFIGFILE
                            assign the config file to be loaded, default is
                            '.ftpbackup'.
