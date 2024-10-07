#include <iostream>
#include <string>
using namespace std;

class Person
{
protected:
    std::string name;
    int age;

public:
    Person(const std::string &name, int age) : name(name), age(age) {}

    void displayPersonInfo()
    {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

class Student : public Person
{
private:
    std::string id;
    std::string faculty;

public:
    Student(const std::string &name, int age, const std::string &studentID, const std::string &faculty) : Person(name, age), id(studentID), faculty(faculty) {}

    void displayStudentInfo()
    {
        displayPersonInfo(); // Call base class method
        cout << "Student ID: " << id << ", Faculty: " << faculty << endl;
    }
};

// Multiple Inheritance

class Employee
{
protected:
    string employeeID;
    string department;

public:
    Employee(const std::string &employeeID, const std::string &department) : employeeID(employeeID), department(department) {}

    void displayEmployeeInfo()
    {
        cout << "Employee ID: " << employeeID << ", Department: " << department << endl;
    }
};

class StudentEmployee : public Student, public Employee
{
public:
    StudentEmployee(const std::string &name, int age, const std::string &studentID, const std::string &faculty,
                    const std::string &employeeID, const std::string &department) : Student(name, age, studentID, faculty), Employee(employeeID, department) {}

    void displayInfo()
    {
        displayStudentInfo();
        displayEmployeeInfo();
    }
};

int main()
{

    Student student("John.W", 20, "S123456", "TI");
    std::cout << "Student Information:" << std::endl;
    student.displayStudentInfo();

    StudentEmployee studentEmployee("Jane.Sh", 22, "S654321", "Business",
                                    "E789101", "Marketing");
    cout << "\nStudent Employee Information:" << endl;
    studentEmployee.displayInfo();

    return 0;
}
