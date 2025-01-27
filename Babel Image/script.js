const canvas = document.getElementById('imageCanvas');
const ctx = canvas.getContext('2d');
const width = 100;  // Width of the grid (number of columns)
const height = 100; // Height of the grid (number of rows)
canvas.width = width * 10; // Each pixel is 10px in size
canvas.height = height * 10;

const targetImage = new Image();
targetImage.src = 'target-image.jpg'; // Replace with the path to your target image
const pixelData = [];

// Random color generation
function randomColor() {
    return `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
}

// Draw a grid of random colors
function generateRandomGrid() {
    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
            ctx.fillStyle = randomColor();
            ctx.fillRect(x * 10, y * 10, 10, 10); // Draw 10x10 pixel block
        }
    }
}

// Function to get pixel data of the target image
function loadTargetImage() {
    targetImage.onload = () => {
        ctx.drawImage(targetImage, 0, 0, width * 10, height * 10);
        pixelData.length = 0;  // Clear previous data
        let imageData = ctx.getImageData(0, 0, width * 10, height * 10);
        for (let i = 0; i < imageData.data.length; i += 4) {
            pixelData.push({
                r: imageData.data[i],
                g: imageData.data[i + 1],
                b: imageData.data[i + 2]
            });
        }
    };
}

// Start the generation process
function startGeneration() {
    loadTargetImage();
    setInterval(() => {
        mutateImage();
    }, 100);
}

// Compare pixel color and mutate towards the target image
function mutateImage() {
    const imageData = ctx.getImageData(0, 0, width * 10, height * 10);
    for (let i = 0; i < pixelData.length; i++) {
        const targetPixel = pixelData[i];
        const currentPixel = {
            r: imageData.data[i * 4],
            g: imageData.data[i * 4 + 1],
            b: imageData.data[i * 4 + 2]
        };

        // Mutate current pixel towards target pixel
        imageData.data[i * 4] = mutateColor(currentPixel.r, targetPixel.r);
        imageData.data[i * 4 + 1] = mutateColor(currentPixel.g, targetPixel.g);
        imageData.data[i * 4 + 2] = mutateColor(currentPixel.b, targetPixel.b);
    }

    ctx.putImageData(imageData, 0, 0);
}

// Mutate a single color channel towards the target
function mutateColor(current, target) {
    if (current < target) {
        return current + Math.floor(Math.random() * 5); // Slowly increase towards target
    } else if (current > target) {
        return current - Math.floor(Math.random() * 5); // Slowly decrease towards target
    }
    return current; // If it's close enough, leave it unchanged
}

// Initial random grid
generateRandomGrid();