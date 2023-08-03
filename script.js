// script.js
let typingTimer;
let aiResponseValue = ""; // Variable to store the AI response

const doneTypingInterval = 500; // Adjust the delay (in milliseconds) as per your preference

async function getAIResponse() {
    clearTimeout(typingTimer);
    const userInput = document.getElementById('userInput').value;
    if (userInput) {
        typingTimer = setTimeout(async function () {
            const response = await fetch(`http://localhost:5001/process_input/${encodeURIComponent(userInput)}`);
            const responseData = await response.json();
            aiResponseValue = responseData.response; // Store the AI response
            document.getElementById('aiResponse').value = aiResponseValue; // Update the text area
            runCode(); // Execute the code automatically when AI response is updated
        }, doneTypingInterval);
    }
}

async function runCode() {
    const code = document.getElementById('aiResponse').value; // Get the code from "Code" text area
    if (code) {
        const requestBody = { code: code };
        try {
            const response = await fetch('http://localhost:5001/process_input/run', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
            });
            const responseData = await response.json();
            const output = responseData.response;
            document.getElementById('output').value = output;
        } catch (error) {
            console.error(error);
        }
    }
}


async function submitAnswer() {
    const question = document.getElementById('userInput').value;
    const userAnswer = document.getElementById('userAnswer').value;
    if (question && userAnswer) {
        try {
            const requestBody = { question: question, answer: userAnswer };
            const response = await fetch('http://localhost:5001/add_to_knowledge', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
            });
            const responseData = await response.json();
            if (responseData.success) {
                alert('Your answer has been added to knowledge!');
            } else {
                alert('Failed to add your answer. Please try again.');
            }
        } catch (error) {
            console.error(error);
            alert('Failed to add your answer. Please try again.');
        }
    } else {
        alert('Please enter both a question and your answer before submitting.');
    }
}


document.getElementById('userInput').addEventListener('input', getAIResponse);
document.getElementById('aiResponse').addEventListener('keyup', runCode); // Add event listener for "Code" textarea