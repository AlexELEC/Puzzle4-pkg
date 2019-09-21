#!/bin/sh

# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2011-present Alex@ELEC (http://alexelec.in.ua)

################################################################################
# Colors
ESC_SEQ="\x1b["
COL_RESET=$ESC_SEQ"39;49;00m"
COL_RED=$ESC_SEQ"31;01m"
COL_GREEN=$ESC_SEQ"32;01m"
COL_YELLOW=$ESC_SEQ"33;01m"
COL_BLUE=$ESC_SEQ"34;01m"
COL_MAGENTA=$ESC_SEQ"35;01m"
COL_CYAN=$ESC_SEQ"36;01m"
################################################################################

BASEDIR=`dirname $0`
PROJECT_PATH=`cd $BASEDIR; pwd`
VERSION=`cat $PROJECT_PATH/version`
PTV_NAME="Puzzle"
RELEASE_DIR="Release"

rm -fr $PROJECT_PATH/$RELEASE_DIR
mkdir -p $PROJECT_PATH/$RELEASE_DIR

echo ""
echo -e "${COL_BLUE}Creating release $PTV_NAME-$VERSION...${COL_RESET}"
echo ""

cp -a serv tvh webui.files $RELEASE_DIR
cp -a *.py *.empty *.htm *.so version $RELEASE_DIR

pushd $PROJECT_PATH/$RELEASE_DIR > /dev/null
tar -cvjf $PROJECT_PATH/$PTV_NAME-$VERSION.tar.bz2 *
rm -rf *
popd > /dev/null
mv -f $PROJECT_PATH/$PTV_NAME-$VERSION.tar.bz2 $PROJECT_PATH/$RELEASE_DIR

echo ""
echo -e "${COL_YELLOW}Done:${COL_MAGENTA} $PTV_NAME-$VERSION.tar.bz2${COL_RESET}"
echo ""
