// Jokes and messages array
const jokes = [
    "Why don't calculators tell jokes? Because they take things too literally!",
    "Loading answer.exe... Error 404: Correct answer not found",
    "Sorry, I was too busy calculating the meaning of life",
    "Have you tried turning it off and on again?",
    "I'm not wrong, I'm just creatively correct!",
    "Error: Brain.exe has stopped working",
];

const wrongAnswers = [
    "π (approximately)",
    "404 - Answer not found",
    "Your age + 7",
    "A bazillion",
    "ERROR: Division by chocolate",
];

let display = document.getElementById('result');
let buttons = document.querySelectorAll('.btn');
let jokeDisplay = document.querySelector('.joke-display');
let currentExpression = '';
let lastWasMischievous = false;

// Add event listeners to all buttons
buttons.forEach(button => {
    button.addEventListener('mouseover', handleMouseOver);
    button.addEventListener('click', handleClick);
});

function handleMouseOver(e) {
    // 30% chance of button running away
    if (Math.random() < 0.3) {
        const btn = e.target;
        const rect = btn.getBoundingClientRect();
        const moveX = (Math.random() - 0.5) * 100;
        const moveY = (Math.random() - 0.5) * 100;
        
        btn.style.transform = `translate(${moveX}px, ${moveY}px)`;
        setTimeout(() => {
            btn.style.transform = 'translate(0, 0)';
        }, 1000);
    }

    // 10% chance of button falling
    if (Math.random() < 0.1) {
        e.target.classList.add('falling');
        setTimeout(() => {
            e.target.classList.remove('falling');
        }, 1000);
    }
}

function handleClick(e) {
    const value = e.target.textContent;
    
    // Handle different button types
    if (value === 'C') {
        clearDisplay();
    } else if (value === '=') {
        calculate();
    } else {
        appendToDisplay(value);
    }

    // 20% chance of showing a joke
    if (Math.random() < 0.2) {
        showJoke();
    }

    // Add shake animation
    e.target.classList.add('shake');
    setTimeout(() => {
        e.target.classList.remove('shake');
    }, 500);
}

function appendToDisplay(value) {
    currentExpression += value;
    display.value = currentExpression;
}

function clearDisplay() {
    currentExpression = '';
    display.value = '';
    lastWasMischievous = false;
}

function calculate() {
    try {
        // 30% chance of giving wrong answer if last answer wasn't mischievous
        if (Math.random() < 0.3 && !lastWasMischievous) {
            display.value = wrongAnswers[Math.floor(Math.random() * wrongAnswers.length)];
            lastWasMischievous = true;
            display.classList.add('rainbow-text');
            setTimeout(() => {
                display.classList.remove('rainbow-text');
            }, 2000);
        } else {
            // Replace × and ÷ with * and /
            let expression = currentExpression.replace(/×/g, '*').replace(/÷/g, '/');
            let result = eval(expression);
            display.value = result;
            lastWasMischievous = false;
        }
    } catch (error) {
        display.value = "Nice try! 😜";
    }
    currentExpression = '';
}

function showJoke() {
    const joke = jokes[Math.floor(Math.random() * jokes.length)];
    jokeDisplay.textContent = joke;
    jokeDisplay.style.opacity = '1';
    
    setTimeout(() => {
        jokeDisplay.style.opacity = '0';
    }, 3000);
}

// Easter egg: Konami code handler
let konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
let konamiIndex = 0;

document.addEventListener('keydown', (e) => {
    if (e.key === konamiCode[konamiIndex]) {
        konamiIndex++;
        if (konamiIndex === konamiCode.length) {
            // Make all buttons fall when Konami code is entered
            buttons.forEach(button => {
                button.classList.add('falling');
            });
            konamiIndex = 0;
        }
    } else {
        konamiIndex = 0;
    }
});

// Occasionally make buttons dodge the cursor
document.addEventListener('mousemove', (e) => {
    buttons.forEach(button => {
        const rect = button.getBoundingClientRect();
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        
        // If mouse is close to button
        if (Math.abs(mouseX - (rect.left + rect.width/2)) < 50 &&
            Math.abs(mouseY - (rect.top + rect.height/2)) < 50) {
            // 10% chance of dodging
            if (Math.random() < 0.1) {
                const angle = Math.random() * Math.PI * 2;
                const distance = 50;
                const moveX = Math.cos(angle) * distance;
                const moveY = Math.sin(angle) * distance;
                
                button.style.transform = `translate(${moveX}px, ${moveY}px)`;
                setTimeout(() => {
                    button.style.transform = 'translate(0, 0)';
                }, 500);
            }
        }
    });
});