A PID (Process ID) is a unique numerical identifier assigned to each running process in an operating system. It helps in tracking and managing individual processes. 

A process is an instance of a computer program that is currently running. It includes the program's code, data, and resources such as memory, CPU time, and file handles.

To find a process's PID, you can use various commands depending on the operating system. For example:
- In Linux/Unix, you can use the `ps` command to list processes along with their PIDs. For instance: `ps aux | grep "process_name"`
- In Windows, you can use the Task Manager or command-line tools like `tasklist` or `WMIC PROCESS GET Caption,ProcessId`.

To kill a process, you typically use the `kill` command in Unix-like systems (e.g., `kill <PID>`), while in Windows, you might use the Task Manager or command-line tools like `taskkill`.

A signal is a limited form of inter-process communication used in Unix-like operating systems to notify a process that a particular event has occurred. Signals can be sent to processes to perform specific actions like termination, interruption, or handling specific events.

The two signals that cannot be ignored are:
1. **SIGKILL (signal 9)**: This signal immediately terminates a process. It cannot be caught or ignored by the process and results in the abrupt termination of the program.
2. **SIGSTOP (signal 19 or 17)**: This signal halts the execution of a process. Similar to SIGKILL, it cannot be caught or ignored, and the process remains in a paused state until it receives a SIGCONT signal to resume execution.

These signals are powerful and used judiciously as they can forcefully stop or terminate processes without allowing them to perform any cleanup or graceful exit actions.
