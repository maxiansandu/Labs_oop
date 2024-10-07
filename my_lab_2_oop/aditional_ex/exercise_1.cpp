#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int credits;

public:
    
    Student(std::string name, int credits) : name(name), credits(credits) {}

   
    Student& operator++() {
        ++credits; 
        return *this;
    }

   
    Student& operator--() {
        --credits; 
        return *this;
    }

   
    Student operator+(const Student& other) {
        return Student(name, credits + other.credits);
    }

   
    Student operator+(int additionalCredits) {
        return Student(name, credits + additionalCredits);
    }

    void display() const {
        std::cout << "Student: " << name << ", Credits: " << credits << std::endl;
    }
};

int main() {
    Student student1("student_1", 30);
    Student student2("student_2", 20);

    std::cout << "Initial Credits:\n";
    student1.display();
    student2.display();

   
    ++student1;
    std::cout << "\nAfter Incrementing Credits for Alice:\n";
    student1.display();

  
    --student2;
    std::cout << "\nAfter Decrementing Credits for Bob:\n";
    student2.display();

    
    Student combinedStudent = student1 + student2;
    std::cout << "\nCombined Credits of Alice and Bob:\n";
    combinedStudent.display();

    
    combinedStudent = student1 + 10; 
    std::cout << "\nCredits after adding 10 from faculty to Alice:\n";
    combinedStudent.display();

    return 0;
}
