---
id: painlessMesh
aliases: []
tags: []
---

#### painlessMesh

> [!float|right-small] painlessMesh
> I'm using `painlessMesh` which is not compatible with `3.X` version board
>
> - Choose ESP32 Board Version `2.0.X`

- Do not require a central node , the nodes are responsible for others conversation.
- [painlessMesh](https://gitlab.com/painlessMesh/painlessMesh) Allows to create mesh network
- Maximum size of the mesh is limited by the amount of memory in the heap that can be allocated to the sub-connections buffer
- When communication they both act as `AP` and `STATION`

#builerplate

```c
#include "painlessMesh.h"
#define   MESH_PREFIX     "meshname"
#define   MESH_PASSWORD   "password" // must be > 7
#define   MESH_PORT       8080

Scheduler userScheduler;
painlessMesh  mesh;

void sendMessage() ;

Task taskSendMessage( TASK_SECOND * 1 , TASK_FOREVER, &sendMessage );

void sendMessage() {
  String msg = "Hi from node1";
  msg += mesh.getNodeId();
  mesh.sendBroadcast( msg );
  taskSendMessage.setInterval( random( TASK_SECOND * 1, TASK_SECOND * 5 ));
}

// Needed for painless library
void receivedCallback( uint32_t from, String &msg ) {
  Serial.printf("startHere: Received from %u msg=%s\n", from, msg.c_str());
}

void newConnectionCallback(uint32_t nodeId) {
    Serial.printf("--> startHere: New Connection, nodeId = %u\n", nodeId);
}

void changedConnectionCallback() {
  Serial.printf("Changed connections\n");
}

void nodeTimeAdjustedCallback(int32_t offset) {
    Serial.printf("Adjusted time %u. Offset = %d\n", mesh.getNodeTime(),offset);
}

void setup() {
  Serial.begin(115200);

//mesh.setDebugMsgTypes( ERROR | MESH_STATUS | CONNECTION | SYNC | COMMUNICATION | GENERAL | MSG_TYPES | REMOTE ); // all types on
  mesh.setDebugMsgTypes( ERROR | STARTUP );  // set before init() so that you can see startup messages

  mesh.init( MESH_PREFIX, MESH_PASSWORD, &userScheduler, MESH_PORT );
  mesh.onReceive(&receivedCallback);
  mesh.onNewConnection(&newConnectionCallback);
  mesh.onChangedConnections(&changedConnectionCallback);
  mesh.onNodeTimeAdjusted(&nodeTimeAdjustedCallback);

  userScheduler.addTask( taskSendMessage );
  taskSendMessage.enable();
}

void loop() {
  mesh.update();
}
```

1. `MESH_PREFIX` -> name of the network , `MESH_PASSWORD` -> password for that

```c
#include "painlessMesh.h"
#define   MESH_PREFIX     "mesh_name"
#define   MESH_PASSWORD   "password"
#define   MESH_PORT       8080
```

_all nodes in the network should use the same password_

2. Creating a `Scheduler` object and `mesh` object

```
Scheduler userScheduler;
painlessMesh  mesh;
```

3.  Running Tasks Indefinitely

- `TASK_SECOND * 1` -> run every second
  - `TASK_SECOND * x` <- where `x` is the second you want that task to repeat to
- `TASK_FOREVER` -> run $\infty$
- `&sendMessage` -> pointer to `sendMessage()`. ? so may be need to define `sendMessage()` before use

```c
Task taskSendMessage( TASK_SECOND * 1 , TASK_FOREVER, &sendMessage );
```

4. Custom functions

```c
void sendMessage() {
  String msg = "Hi from node1";
  msg += mesh.getNodeId();
  mesh.sendBroadcast( msg );
  taskSendMessage.setInterval( random( TASK_SECOND * 1, TASK_SECOND * 5 ));
}
```

- `mesh.sendBroadcast()` -> sends to all nodes in the network
- `taskSendMessage.setInterval( random( TASK_SECOND * 1, TASK_SECOND * 5 ))` send in a random intervell between `1 and 5`
  To send to a specific node

```c
void sendMessage() {
String msg = "Hi from node1";
uint32_t targetNodeId = /* Target Node ID */;
msg += mesh.getNodeId();
mesh.sendSingle(targetNodeId, msg);
// Send to a specific node
taskSendMessage.setInterval(random(TASK_SECOND * 1, TASK_SECOND * 5)); }
```

5. Callback Functions

- Similar like `ACK`
- `from` -> sender node id
- `msg` -> recieved message

```c
// Needed for painless library
void receivedCallback( uint32_t from, String &msg ) {
  Serial.printf("startHere: Received from %u msg=%s\n", from, msg.c_str());
}
```

- `newConnectionCallback` when a new node is joins the network

```c
void newConnectionCallback(uint32_t nodeId) {
    Serial.printf("--> startHere: New Connection, nodeId = %u\n", nodeId);
}

```

- `changedConnectionCallback` -> when a connection between the nodes changes

```c
void changedConnectionCallback() {
  Serial.printf("Changed connections\n");
}

```

6. when the time synchronization between nodes is adjusted

```c

void nodeTimeAdjustedCallback(int32_t offset) {
    Serial.printf("Adjusted time %u. Offset = %d\n", mesh.getNodeTime(),offset);
}

```

7. Setup Section

- `mesh.setDebugMsgTypes(ERROR | STARTUP)` -> debug messages
  - Available types
    - `ERROR` | `MESH_STATUS` | `CONNECTION` | `SYNC` | `COMMUNICATION` | `GENERAL` | `MSG_TYPES `| `REMOTE`
    - `mesh.setDebugMsgTypes( )` -> simply using this enables all the aboves
- `mesh.init(...)` -> initializes the mesh
- connection feedbacks
  - `mesh.onReceive(&receivedCallback)`
  - `mesh.onNewConnection(&newConnectionCallback)`
  - `mesh.onChangedConnections(&changedConnectionCallback)`
  - `mesh.onNodeTimeAdjusted(&nodeTimeAdjustedCallback)`
  - [ ] Need to change the name of the functions

```c
void setup() {
  Serial.begin(9600);
  mesh.setDebugMsgTypes( ERROR | STARTUP );
  mesh.init( MESH_PREFIX, MESH_PASSWORD, &userScheduler, MESH_PORT );
  mesh.onReceive(&receivedCallback);
  mesh.onNewConnection(&newConnectionCallback);
  mesh.onChangedConnections(&changedConnectionCallback);
  mesh.onNodeTimeAdjusted(&nodeTimeAdjustedCallback);
  userScheduler.addTask( taskSendMessage );
  taskSendMessage.enable();
}

```

- `userScheduler.addTask(taskSendMessage);` adds the message-sending task to the scheduler.
- `taskSendMessage.enable();` enables the task so that it starts running.

8.  continuously run the mesh network

```c
void loop() {
  // it will run the user scheduler as well
  mesh.update();
}
```
