// let's do day 1

#include <iostream>
#include <fstream>
#include <string>

int main(){
    std::ifstream file ("input.txt");

    std::string line;
    int score = 0;
    int max_score = 0;

    while(std::getline(file, line)){
        if (line == "")
            {
                if(score > max_score) 
                    max_score = score;
                score = 0;
                continue;
            }

        int a = std::stoi(line);
        score += a; 
    }

    std::cout << max_score;
}