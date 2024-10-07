#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// clasa de baza, logarea abstracta
class OperationLogger {
public:
    virtual void log(const string& message) = 0; 
    virtual ~OperationLogger() {} 
};

// clasa derivata, file mesage log
class FileLogger : public OperationLogger {
private:
        string file_name;

public:
    FileLogger(const string& file_name) : file_name(file_name) {}

    void log(const std::string& message) override {
            ofstream file(file_name, ios_base::app); // deschidem file-ul in modul de scriere
            
            file << message << endl;
            file.close();
        
    }
};


class ConsoleLogger : public OperationLogger {
public:
    void log(const std::string& message) override {
         cout << "Console Log: " << message << endl;
    }
};


void perform_operation(OperationLogger& logger, const string& operation) {
    
    logger.log("Operation performed: " + operation);
}

int main() {
    
    FileLogger fileLogger("logfile.txt");
    ConsoleLogger consoleLogger;

   
    perform_operation(fileLogger, "File operation: Saving data to file");
    perform_operation(consoleLogger, "Console operation: Displaying information");

    return 0;
}
