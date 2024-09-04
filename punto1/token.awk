#!/usr/bin/awk -f

{
    if ($0 ~ /^\+$/) {
        print "Token: SUMA"
    } else if ($0 ~ /^\+\+$/) {
        print "Token: INCR"
    } else if ($0 ~ /^[0-9]+$/) {
        print "Token: ENTERO"
    } else if ($0 ~ /^[0-9]+\.[0-9]+$/) {
        print "Token: REAL"
    } else {
        print "Token: UNKNOWN"
    }
}
