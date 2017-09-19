# This script is called by openHAB after the persistence service has started
sleep 5
cd /etc/openhab/configurations/rules/
RULES=`find *.rules | grep -v refresh.rules`
for f in $RULES
do
  touch $f
done 
