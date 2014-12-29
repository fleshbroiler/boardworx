#!/bin/sh
#
# Performs a backup and restore of the /xos directory
#
#
####################################################
ROOT_DIR=/xos/
DEST_DIR=/data/

#########################################################
########  LOOK IN DATA DIR FOR A BACKUP FILE...  ########
########  VALIDATE BY LOCATING & PARSING         ########
########  SIGNATURE FILE                         ########
#########################################################

TRG_FILES=$DEST_DIR'*.tgz'
echo "searching for backup files:" $TRG_FILES

files=$(ls /data/*.tgz 2> /dev/null | wc -l)
if [ "$files" != "0" ]
then
	echo "performing restore from backup..."
# what is the name of the file?
TARGET=$(ls /data/*.tgz)

echo "found tgz backup [" $TARGET "]"

### TRY EXTRACTING SIGNATURE FILE #######################
tar -zxvf $TARGET xos/.xosbackup.txt
# were we successful? find the file 1st...

echo "searching for signature file..."
#SIGFILE=$(find xos/.xosbackup.txt 2> /dev/null)

if [ -f xos/.xosbackup.txt ]
then
	# FOUND THE SIGNATURE FILE, PROCEED
	echo "signature file found..." $SIGFILE	

#CLEAN UP THE XOS DIR ON THE SDCARD
rm -r xos

#UNPACK THE TGZ TO THE XOS DIRECTORY

tar -zxf $TARGET -C /xos

else
	echo "SIGFILE NOT FOUND.. "
	# HOW DO WE HANDLE THIS POSSIBILITY?
fi


else
	echo "performing backup"
######## CREATE SIGNATURE FILE ##########################
DATE=`date +%F`
TIME=`date +%T`
MILLI=000
TIMEZONE=`date +%Z`
#echo "${DATE} ${TIME}.${MILLI} $TIMEZONE"  > $ROOT_DIR.xosbackup.txt
echo "${DATE} ${TIME}"  > $ROOT_DIR.xosbackup.txt
####################################################
######## CREATE TAR 
#dt=`date +%Y%m%d"-"%H%M%S`
dt=`date +%Y%m%d`
PREFIX=xosbackup_
APP_NAME=$PREFIX$dt'.tar'
NEW_NAME=$PREFIX$dt'.tgz'
TARFILE=$TMP_DIR$APP_NAME

echo "creating tar: " $TARFILE

tar cv $ROOT_DIR | gzip > $DEST_DIR$NEW_NAME

######## CLEAN UP ########################################
#remove signature file
rm /xos/.xosbackup.txt

fi



