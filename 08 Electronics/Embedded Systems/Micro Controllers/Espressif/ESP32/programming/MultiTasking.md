---
id: MultiTasking
aliases: []
tags:
  - electronics
  - embedded_systems
  - micro_controllers
  - espressif
  - esp32
  - programming
dg-publish: true
---
### Multi Tasking using Free RTOS

##### Simple Task which uses only one core

- [[Academics/S6/Embedded Systems/RTOS/Free RTOS  Scheduling]]

1. Defining Tasks

```c
int count1 = 0;
int count2 = 0;

void task1 (void * parameters){
	for (;;){
		Serial.println("From Task1");
		vTaskDelay(1000 / portTICK_PERIODS_MS);
}

void task1 (void * parameters){
	for (;;){
		Serial.println("From Task2");
		vTaskDelay(1000 / portTICK_PERIODS_MS);
}

```

```c
vTaskDelay(1000 / portTICK_PERIODS_MS);

```

- This line is used to get 1 second delay

2. Creating Task

```c
xTaskCreate(
	task1, // This is the name of the function
	"Some Name", // Just a taskname for later debuging
	1000, // stack size
	NULL, // Parameter List
	1,
	NULL
);
xTaskCreate(
	task2, // This is the name of the function
	"Some Name 2", // Just a taskname for later debuging
	1000, // stack size
	NULL, // Parameter List
	1,
	NULL
);

```

##### Managing Free RTOS Tasks

- Stopping the task

```c
vTaskDelete(NULL);

```

##### Creating Taskhandles

```cpp
TaskHandle_t task1_handle = NULL;

```

- Now when calling xTaskCreate use this task_handle for task1

```c
xTaskCreate(
	task1, // This is the name of the function
	"Some Name", // Just a taskname for later debuging
	1000, // stack size
	NULL, // Parameter List
	1,
	&task1_handle
);

```

> [!NOTE] Taskhandles
> `Taskhandles` are used to talk to the task

##### Suspend A running Task

```c
void task1 (void * parameters){
for (;;){
	Serial.println("From Task2");
	vTaskDelay(1000 / portTICK_PERIODS_MS);
	count1++;
		if (count1 > 3){
			vTaskSuspend(NULL);
		}
}

```

```c
vTaskSuspend(NULL);

```

- This is used to suspend the task within it self , we can also suspend the task from outside

###### Suspend the task from outside

```

void loop(){
    if (count > 3){ // will this variable bee accesible from outside
	vTaskSuspend(task1_handle);
	}
}

```

- If we run the above programm the `vTaskSuspend` will suspend the main function = `loop`
- To avoid that use the following

```c
void loop(){
    if (count > 3 && task1_handle != NULL){ // will this variable bee accesible from outside
	vTaskSuspend(task1_handle);
	}
	vTaskSuspend(task1_handle);
	}
}

```

##### Resuming a Task

```cpp
vTaskResume(task1_handle);

```

##### Semaphore

```c
SemaphoreHandle_t semaphore;

```

- It is Just a flag like yes/no

#eg

```c
TaskHandle_t Task0;
TaskHandle_t Task1;
SemaphoreHandle_t semaphore;

void Task1(void * parameters){
      for(;;){
          Serial.print("Running on the core : ");
          Serial.println(xPortGetCoreID());
                // Code here

          xSemaphoereGive(semaphore);

  }
}

```

#### Multi Threding

```c
/*
Source : https://randomnerdtutorials.com/esp32-dual-core-arduino-ide/ */
*/
/*********
  Rui Santos
  Complete project details at https://randomnerdtutorials.com
*********/

TaskHandle_t solar_tracking_id;
TaskHandle_t energy_managment_id;

// LED pins
const int led1 = 2;
const int led2 = 4;
//
void setup() {
  Serial.begin(9600);
  // pinMode(led1, OUTPUT);
  // pinMode(led2, OUTPUT);

  //create a task that will be executed in the Task1code() function, with priority 1 and executed on core 0
  xTaskCreatePinnedToCore(
                    Solar_Managment,   /* Task function. */
                    "Task1",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    1,           /* priority of the task */
                    &solar_tracking_id,      /* Task handle to keep track of created task */
                    0);          /* pin task to core 0 */
  delay(500);

  //create a task that will be executed in the Task2code() function, with priority 1 and executed on core 1
  xTaskCreatePinnedToCore(
                    Energy_Managment,   /* Task function. */
                    "Task2",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    1,           /* priority of the task */
                    &energy_managment_id,      /* Task handle to keep track of created task */
                    1);          /* pin task to core 1 */
    delay(500);
}

//Task1code: blinks an LED every 1000 ms
void Solar_Managment( void * pvParameters ){
  Serial.print("Task1 running on core ");
  Serial.println(xPortGetCoreID());

  for(;;){
    digitalWrite(led1, HIGH);
    delay(1000);
    digitalWrite(led1, LOW);
    delay(1000);
  }
}

//Task2code: blinks an LED every 700 ms
void Energy_Managment( void * pvParameters ){

  Serial.print("Task2 running on core ");
  Serial.println(xPortGetCoreID());

  // for(;;){
  //   digitalWrite(led2, HIGH);
  //   delay(700);
  //   digitalWrite(led2, LOW);
  //   delay(700);
  // }
}

void loop() {

}

```

#### New Multithreading

```cpp
Serial.println(xPortGetCoreID());

```

_It Prints in which core the current task or process is been executing_
