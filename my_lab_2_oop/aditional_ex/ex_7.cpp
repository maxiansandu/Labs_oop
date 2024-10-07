#include <iostream>
#include <string>
#include <exception>
#include <vector>
using namespace std;

class StudentNotFoundException : public exception
{
public:
    const char *what() const noexcept override
    {
        return "Error: Student not found";
    }
};

class InvalidFacultyOperation : public exception
{
private:
    string message;

public:
    InvalidFacultyOperation(const string &msg) : message(msg) {}
    const char *what() const noexcept override
    {
        return message.c_str();
    }
};

class Student
{
private:
    string name;
    string id;

public:
    Student(const string &name, const string &studentID) : name(name), id(studentID) {}
    string get_name() const { return name; }
    string get_id() const { return id; }
};

class Faculty
{
private:
    string name;
    vector<Student> students;

public:
    Faculty(const string &name) : name(name)
    {
        if (name.empty())
        {
            throw InvalidFacultyOperation("Error: Faculty name cannot be empty!");
        }
    }

    void add_student(const Student &student)
    {
        students.push_back(student);
    }

    Student find_by_id(const string &student_id)
    {
        for (const auto &student : students)
        {
            if (student.get_id() == student_id)
            {
                return student;
            }
        }
        throw StudentNotFoundException();
    }

    void rm_by_id(const string &studentID)
    {
        for (auto it = students.begin(); it != students.end(); ++it)
        {
            if (it->get_id() == studentID)
            {
                students.erase(it);
                return;
            }
        }
        throw StudentNotFoundException();
    }
};

int main()
{

        try
    {
        Faculty TI_faculty("TI");

        TI_faculty.add_student(Student("John D", "1"));
        TI_faculty.add_student(Student("Jane Sh", "2"));

        cout << "Looking for student 2..." << endl;
        Student foundStudent = TI_faculty.find_by_id("3");
        cout << "Student found: " << foundStudent.get_name() << endl;
    }
    catch (const exception &e)
    {
        cerr << e.what() << endl;
    }

    return 0;
}
