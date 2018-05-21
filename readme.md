## Install
`pip install ftpbackup`


## Usage
usage: ftpbk [-h] {genconf,backup} ...

Backup to FTP.

optional arguments:
  -h, --help        show this help message and exit

subcommands:
  {genconf,backup}

### backup
usage: ftpbk backup [-h] [-c CONFIGFILE]

Backup all the file in the 'local' floder to 'remote' on ftp. You can change
the config in config file(default is '.ftpbackup').

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIGFILE, --conf CONFIGFILE
                        assign the config file to be loaded, default is
                        '.ftpbackup'.

### genconf
usage: ftpbk genconf [-h] [-F] [-f FILE]

Generate a default config file.

optional arguments:
  -h, --help            show this help message and exit
  -F, --force           overwrite the config file if it exists.
  -f FILE, --file FILE  assign the config file to be writed, default is
                        '.ftpbackup'.
