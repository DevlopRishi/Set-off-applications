#include <stdio.h>

void displayQuestion(char question[], char options[][50], char correctOption) {
    printf("\n%s\n", question);
    for (int i = 0; i < 4; i++) {
        printf("%c. %s\n", 'A' + i, options[i]);
    }
    printf("Your answer (A/B/C/D): ");
}

int main() {
    // Question bank
    char questions[][100] = {
        "What is the capital of France?",
        "What is 5 + 7?",
        "Which programming language is known as the mother of all languages?",
        "Who wrote 'Romeo and Juliet'?"
    };

    char options[][4][50] = {
        {"Paris", "Berlin", "Madrid", "Rome"},
        {"10", "12", "14", "15"},
        {"Assembly", "C", "Python", "JavaScript"},
        {"William Shakespeare", "Charles Dickens", "Mark Twain", "J.K. Rowling"}
    };

    char correctAnswers[] = {'A', 'B', 'A', 'A'};
    int score = 0;
    int numQuestions = sizeof(questions) / sizeof(questions[0]);

    printf("Welcome to the Educational Quiz Game!\n");
    printf("Answer the following questions to test your knowledge.\n");
    printf("------------------------------------------------------\n");

    for (int i = 0; i < numQuestions; i++) {
        char userAnswer;
        displayQuestion(questions[i], options[i], correctAnswers[i]);
        scanf(" %c", &userAnswer);

        if (userAnswer == correctAnswers[i] || userAnswer == correctAnswers[i] + 32) {
            printf("Correct!\n");
            score++;
        } else {
            printf("Wrong! The correct answer was %c.\n", correctAnswers[i]);
        }
    }

    printf("\nGame Over!\n");
    printf("Your total score is %d/%d.\n", score, numQuestions);

    if (score == numQuestions) {
        printf("Excellent! You got all answers right!\n");
    } else if (score >= numQuestions / 2) {
        printf("Good job! Keep learning!\n");
    } else {
        printf("Keep practicing and try again.\n");
    }

    return 0;
}