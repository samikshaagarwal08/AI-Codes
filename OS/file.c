// #include <stdio.h>
// #include <fcntl.h>
// #include <unistd.h>

// #define FILE_NAME "sample.txt"
// #define BUFFER_SIZE 100

// int main() {
//     int file_desc;
//     char buffer[BUFFER_SIZE];
//     char *data = "Hello, this is a UNIX file operation demo!\n";
//     ssize_t bytes_written, bytes_read;

//     // 1. Open/Create the file with read and write permissions (rw-r--r--)
//     file_desc = open(FILE_NAME, O_CREAT | O_RDWR, 0644);
//     if (file_desc < 0) {
//         perror("Error opening file");
//         return 1;
//     }

//     // 2. Write data to the file
//     bytes_written = write(file_desc, data, strlen(data));
//     if (bytes_written < 0) {
//         perror("Error writing to file");
//         close(file_desc);
//         return 1;
//     }

//     // 3. Reset file pointer to the beginning
//     if (lseek(file_desc, 0, SEEK_SET) < 0) {
//         perror("Error using lseek");
//         close(file_desc);
//         return 1;
//     }

//     // 4. Read the content from the file
//     bytes_read = read(file_desc, buffer, BUFFER_SIZE - 1);
//     if (bytes_read < 0) {
//         perror("Error reading file");
//         close(file_desc);
//         return 1;
//     }

//     buffer[bytes_read] = '\0';  // Null-terminate the string
//     printf("File Content: \n%s", buffer);

//     // 5. Close the file
//     close(file_desc);

//     return 0;
// }
