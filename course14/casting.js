/**
 * Created by sobolevn on 01.04.16.
 */

// 'use strict';

var apples = "2";
var oranges = "3";

console.log(apples + oranges);
console.log(+apples + +oranges);

console.log(parseInt('02.34ssd'));
console.log(parseFloat('2.34ssd'));

console.log(Number('2.3'));

var toBool = 'string';
console.log(!!toBool);
console.log(Boolean(toBool));

console.log(String(null));
console.log(+undefined);

/**
 > !!'s'
true
> !!''
false
> !!'1'
true
> !!'0'
true
> !!0
false
> !!!!0
false
> !![]
true
> !!{}
true
> !!null
false
> !!undefined
 false
 **/

// Comparing different types:
console.log(1 == '1');  // true
console.log(1 === '1');  // false
console.log(0 == false);  // true
console.log(1 == true);  // true
console.log(1 === true); // false
console.log('' == null); // false
console.log(null == undefined); // true
console.log(null === undefined); // false
console.log(0 == []); // false
console.log(1 == {}); // true
