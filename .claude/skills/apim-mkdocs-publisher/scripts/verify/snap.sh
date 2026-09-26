#!/bin/bash
# usage: snap.sh <product-dir> <label> [dir-with-mv.db-copies]
# Dumps WSO2AM_DB and WSO2SHARED_DB (one INSERT per row) to $VERIFY_OUT/snaps/<product>/<label>/.
# Without the 3rd arg it connects through the running server (needs ;AUTO_SERVER=TRUE on both H2 URLs);
# with it, it reads offline copies of the .mv.db files. Set JAVA to a JDK matching the product.
set -e
: "${VERIFY_OUT:?set VERIFY_OUT to an absolute scratch directory}"
P=$(cd "$1" && pwd); LABEL=$2; SRC=${3:-$P/repository/database}
OUT=$VERIFY_OUT/snaps/$(basename "$P")/$LABEL; mkdir -p "$OUT"
JAR=$(ls "$P"/repository/components/plugins/h2*.jar | grep -v grant | head -1)
for DB in WSO2AM_DB WSO2SHARED_DB; do
  URL="jdbc:h2:$SRC/$DB"; [ -z "$3" ] && URL="$URL;AUTO_SERVER=TRUE" || URL="$URL;IFEXISTS=TRUE"
  "${JAVA:-java}" -cp "$JAR" org.h2.tools.Shell -url "$URL" -user wso2carbon -password wso2carbon \
    -sql "SCRIPT SIMPLE NOPASSWORDS NOSETTINGS TO '$OUT/$DB.sql'" >/dev/null
done
echo "$OUT"
