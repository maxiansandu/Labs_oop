#include <iostream>
#include <string>
using namespace std;


class Person {
public:
    
    virtual string getRole() = 0;

    // Destructor
    virtual ~Person() = default;
};


class Student : public Person {
public:
    string getRole() override {
        return "Student";
    }
};


class Teacher : public Person {
public:
    std::string getRole() override {
        return "Teacher";
    }
};


class Administrator : public Person {
public:
    std::string getRole() override {
        return "Administrator";
    }
};

int main() {
    
    Person* student = new Student();
    Person* teacher = new Teacher();
    Person* administrator = new Administrator();

   
    cout << "Role: " << student->getRole() << endl;
    cout << "Role: " << teacher->getRole() << endl;
    cout << "Role: " << administrator->getRole() << endl;

   
    delete student;
    delete teacher;
    delete administrator;

    return 0;
}
