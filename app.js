// Registration form submit 

const inputRegisterUsername = document.getElementById("input-register-username");
const inputRegisterPassword = document.getElementById("input-register-password");
const buttonRegisterSubmit = document.getElementById("button-register-submit");

buttonRegisterSubmit.addEventListener("click", nextTest);
document.getElementById('notification-button').addEventListener("click", nextTest);

let testsCompleted = 0;

function nextTest() {
  if (testsCompleted === 0) {
    document.getElementById('notification').style.display = 'none';
    document.getElementById('gray-back').style.display = 'none';
  }
  if (testsCompleted === 1) {
    document.getElementById('title-text').textContent = 'Type Your Username and Password 3 More Times';
    document.getElementById('title-subtext').textContent = '';
  };
  if (testsCompleted === 2) {
    document.getElementById('title-text').textContent = 'Type Your Username and Password 2 More Times';
    document.getElementById('gray-back').style.display = 'block';
    document.getElementById('ad').style.display = 'block';
    setTimeout(function () { document.getElementById('ad').style.display = 'none'; document.getElementById('gray-back').style.display = 'none'; }, 7700);
  }
  if (testsCompleted === 3) {
    document.getElementById('title-text').textContent = 'Type Your Username and Password 1 More Time';
    document.getElementById('title-subtext').textContent = '(Also, That Pop-up Was There On Purpose To Stress You Out)';
  }
  if (testsCompleted === 4) {
    document.getElementById('title-subtext').textContent = '';
    document.getElementById('notification-text').textContent = 'Thank Your For Your Input and Get Ready for the Testing Phase';
    document.getElementById('notification-button').textContent = 'I Am Ready To Begin Testing';
    document.getElementById('notification').style.display = 'block';
    document.getElementById('gray-back').style.display = 'block';
  }
  if (testsCompleted === 5) {
    document.getElementById('notification').style.display = 'none';
    document.getElementById('gray-back').style.display = 'none';
    document.getElementById('title-text').textContent = 'Please Enter the Username "RandomlySelectedUser1" and "RandomlySelectedPass1"';
  }
  if (testsCompleted === 6) {
    document.getElementById('title-text').textContent = 'Please Enter the Username "RandomlySelectedUser2" and "RandomlySelectedPass2"';
  }
  if (testsCompleted === 7) {
    document.getElementById('title-text').textContent = 'Please Enter the Username "RandomlySelectedUser3" and "RandomlySelectedPass3"';
  }
  if (testsCompleted === 8) {
    document.getElementById('notification-text').textContent = 'Thank You for Your Help! You Have Finished.';
    document.getElementById('notification-button').style.display = 'none';
    document.getElementById('notification').style.display = 'block';
    document.getElementById('gray-back').style.display = 'block';
  }
  document.getElementById('input-register-username').value = '';
  document.getElementById('input-register-password').value = '';
  testsCompleted++;
}

let dwellDownTime,
  dwellUpTime,
  dwellTimeDiff,
  flightBeginTime,
  flightEndTime,
  flightTimeDiff,
  flightBeginKeyCode,
  flightEndKeyCode;

let isKeyUp = true;
let hasTypedKey = false;
let begunTyping = false;
let isFinished = false;


inputRegisterUsername.onkeydown = function (e) {
  onKeyDown(e);
};
inputRegisterUsername.onkeyup = function (e) {
  onKeyUp(e);
};
inputRegisterPassword.onkeydown = function (e) {
  onKeyDown(e);
};
inputRegisterPassword.onkeyup = function (e) {
  onKeyUp(e);
};

// Evaluate Text For Errors func

function onKeyDown(e) {
  if (isKeyUp) {
    isKeyUp = false;

    dwellDownTime = +new Date();

    if (hasTypedKey) {
      flightEndTime = +new Date();
      flightTimeDiff = flightEndTime - flightBeginTime;
      flightEndKeyCode = e.keyCode;
      console.log(
        `${flightBeginKeyCode} to ${flightEndKeyCode}'s flight time is ${flightTimeDiff}ms`
      );
    }
  }

  if (!begunTyping) {
    typingStartTime = +new Date();
    begunTyping = true;
  }
};

function onKeyUp(e) {
  hasTypedKey = true;

  dwellUpTime = +new Date();

  dwellTimeDiff = dwellUpTime - dwellDownTime;

  console.log(`${e.keyCode}'s dwell time is ${dwellTimeDiff}ms`);
  isKeyUp = true;

  flightBeginKeyCode = e.keyCode;
  flightBeginTime = +new Date();
};
