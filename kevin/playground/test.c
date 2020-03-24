#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int stringFormatting() {
    char characterName[] = "John";
    int characterAge = 35;

    printf("There was once a man named %s.\n", characterName);
    printf("He was %d years old.\n", characterAge);
    return 0;
}

int primitiveTypes() {
    int age = 40;
    double gpa = 3.6;
    char grade = 'A';
    char phrase[] = "Giraffe Academy";

    return 0;
}

// Backslash escape character in strings works as expected
// Need newline \n in printf

int otherFormatting() {

    int favNum = 90;
    char myChar = 'i';
    printf("My favorite %c is %d.\n", myChar, favNum);
    printf("%f", 8.9);

    return 0;

}

void numbers() {
    printf("%f\n", 5 + 4.5); // 9.500000
    printf("%d\n", 5 + 4); // 9
    printf("%d\n", 5 / 4); // 1
    printf("%f\n", 5 / 4.0); // 1.250000

    int num = 6;
    printf("%d\n", num); // 6
}

void math() {
    printf("%f\n", pow(2, 3)); // 8.000000
    printf("%f\n", pow(4, 3)); // 64.00000
    printf("%f\n", sqrt(36)); // 6.000000
    printf("%f\n", ceil(36.356)); // 37.000000
    printf("%f\n", floor(36.356)); // 36.000000
}

void comments() {
    /*
        ...
    */
    // printf("comments fun\n");
}

void constants() {
    /* This first block prints 5\n8\n. */
    // constants in C cannot be modified...
    /*
    int num = 5;
    printf("%d\n", num);
    num = 8;
    printf("%d\n", num);
    */

    /* This next block uses the const keyword. */
    // Note the use of SNAKE_CASE here for const
    const int NUM = 5;
    printf("%d\n", NUM);
}

void userInput() {
    /*
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("You are %d years old.\n", age);

    double gpa;
    printf("Enter your gpa: ");
    scanf("%lf", &gpa);
    printf("Your gpa is %f.\n", gpa);

    */

    /*
    // Had to comment above section out because grade was \n
    char grade;
    printf("Enter your grade: ");
    scanf("%c", &grade);
    printf("Your grade is %c.\n", grade);
    */

    // Had to comment above section out because name was \n
    // Read in string input
    char name[20];
    printf("Enter your name: ");
    // scanf("%s", name); - doesn't get spaces
    fgets(name, 20, stdin);
    printf("Your name is %s.\n", name);
}

void calc() {
    double num1;
    double num2;
    printf("Enter first number: ");
    scanf("%lf", &num1);
    printf("Enter second number: ");
    scanf("%lf", &num2);

    printf("Answer: %f.\n", num1 + num2);
}

void arrays() {
    // Basic creation and indexing
    int luckyNumbers[] = {1, 2, 3, 4, 5, 6};
    printf("%d\n", luckyNumbers[0]);

    // Modify
    luckyNumbers[1] = 0;
    printf("%d\n", luckyNumbers[1]);

    // Empty init
    int lucky[10];
    luckyNumbers[1] = 81;
    printf("%d\n", luckyNumbers[1]);

    // Char arrays
    char phrase[20] = "Array";
    printf("%s\n", phrase);
}

void funcs() {

}

int main() {

    // otherFormatting();
    // numbers();
    // math();
    // comments();
    // constants();
    // userInput();
    // calc();
    // arrays();
    funcs();

    return 0;

}
