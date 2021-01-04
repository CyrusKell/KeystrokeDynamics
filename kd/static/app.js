let dwelldata = {};
let flightdata = {};
let key = [];

let dwellDownTime,
  dwellUpTime,
  dwellTimeDiff,
  flightBeginTime,
  flightEndTime,
  flightTimeDiff,
  flightBeginKeyCode,
  flightEndKeyCode;

let isFirst = true;

const input = document.getElementsByClassName("input");

for (i = 0; i <= input.length - 1; i++) {
  input[i].onkeydown = function (e) { onKeyDown(e); }
  input[i].onkeyup = function (e) { onKeyUp(e); }
  input[i].onfocus = function () { isFirst = true; }
};

function onKeyDown(e) {
  if (!isFirst) {
    flightEndTime = +new Date();
    flightTimeDiff = flightEndTime - flightBeginTime;
    flightEndKeyCode = e.keyCode;

    if (typeof flightdata[flightBeginKeyCode + "-" + flightEndKeyCode] === 'undefined') {
      flightdata[flightBeginKeyCode + "-" + flightEndKeyCode] = flightTimeDiff;
    } else {
      flightdata[flightBeginKeyCode + "-" + flightEndKeyCode] += ',' + flightTimeDiff;
    }

    flightBeginKeyCode = e.keyCode;
    flightBeginTime = +new Date();
  };

  if (isFirst) {
    flightBeginKeyCode = e.keyCode;
    flightBeginTime = +new Date();

    isFirst = false;
  };

  key[e.keyCode] = +new Date();
};

function onKeyUp(e) {
  dwellUpTime = +new Date();
  dwellTimeDiff = dwellUpTime - dwellDownTime;

  dwellTimeDiff = +new Date() - key[e.keyCode];

  if (typeof dwelldata[e.keyCode] === 'undefined') {
    dwelldata[e.keyCode] = dwellTimeDiff;
  } else {
    dwelldata[e.keyCode] += ',' + dwellTimeDiff;
  }
};

function submitForm() {
  document.getElementById('dwelldata').value = JSON.stringify(Object.assign({}, dwelldata));
  document.getElementById('flightdata').value = JSON.stringify(Object.assign({}, flightdata));
  document.getElementById('form').submit();
}