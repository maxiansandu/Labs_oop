#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Student
{
private:
    string name;
    int id;

public:
    Student(const string &name, int id) : name(name), id(id) {}

    void display()
    {
        cout << "Student Name: " << name << ", ID: " << id << endl;
    }

    string grt_name() const
    {
        return name;
    }
};

class Faculty
{
private:
    string faculty_name;
    vector<Student *> students; // Agregam intr-un fel clasa student la Faculty

public:
    Faculty(const std::string &facultyName) : faculty_name(facultyName) {}

    void addStudent(Student *student)
    {
        students.push_back(student); // pointer la student existent
    }

    void displayFacultyInfo()
    {
        cout << "Faculty: " << faculty_name << endl;
        cout << "Students in this faculty:" << endl;
        for (auto student : students)
        {
            student->display();
        }
    }
};

int main()
{

    Student student1("John.W", 101);
    Student student2("Jane.Sh", 102);

    Faculty faculty("TI");

    faculty.addStudent(&student1);
    faculty.addStudent(&student2);

    faculty.displayFacultyInfo();

    return 0;
}
