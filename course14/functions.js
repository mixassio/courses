/**
 * Created by sobolevn on 01.04.16.
 */

'use strict';

function log(value) {
    console.log(value);
    return 'as';
}


var namedLog = function(value) {
    console.log('named', value);
};


var nfe = function namedFunctionalExpression (i) {
    if (i == 0) {
        return 0;
    }
    // namedFunctionalExpression = null;
    return i + namedFunctionalExpression(i - 1); // i-- or --i
};

var returnValue = log(123);
console.log(returnValue);

namedLog('asd');
console.log(nfe(5));
// namedFunctionalExpression(5);

log = console.log;
log();

console.log(typeof namedLog);
namedLog = null;
// namedLog(23);
