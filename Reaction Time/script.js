let startBtn = document.getElementById('startBtn');
let container = document.getElementById('container');
let reactionTimeDisplay = document.getElementById('reactionTimeDisplay');

let startTime, endTime, timeout;

startBtn.addEventListener('click', startTest);

function startTest() {
    startBtn.disabled = true;
    container.style.backgroundColor = 'black';
    reactionTimeDisplay.textContent = '';

    // Wait for a random time between 2 and 5 seconds
    timeout = setTimeout(() => {
        container.style.backgroundColor = 'red';
        // After a random time, change to green
        let delay = Math.random() * (5000 - 2000) + 2000;
        setTimeout(() => {
            container.style.backgroundColor = 'green';
            startTime = Date.now();  // Start the stopwatch when it turns green
        }, delay);
    }, Math.random() * (5000 - 2000) + 2000);
}

container.addEventListener('click', stopTest);

function stopTest() {
    if (container.style.backgroundColor === 'green') {
        endTime = Date.now();
        let reactionTime = endTime - startTime;
        reactionTimeDisplay.textContent = `Your reaction time is: ${reactionTime} ms`;
        container.style.backgroundColor = 'black';
        startBtn.disabled = false;  // Re-enable the start button
    }
}