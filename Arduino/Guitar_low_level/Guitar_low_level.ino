#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;
Servo s4;
Servo s5;
Servo s6;

const int CMD_SIZE = 4;
char received_command[9];

bool CENTER_SERVO = true;
int CENTER_ANGLE = 90;

int STARTING_ANGLE = 75; // 65
int STRUM_ANGLE = 180; // 100

int S1_START = 71;
int S1_STOP = 105;
int s1_pos = 0;

int S2_START = 78;
int S2_STOP = 110;
int s2_pos = 0;

int S3_START = 60;
int S3_STOP = 100;
int s3_pos = 0;

int S4_START = 70;
int S4_STOP = 113;
int s4_pos = 0;

int S5_START = 70;
int S5_STOP = 105;
int s5_pos = 0;

int S6_START = 77;
int S6_STOP = 120;
int s6_pos = 0;

int S3_OFFSET = 0;
int S4_OFFSET = 0;
int S5_OFFSET = 0;
int S6_OFFSET = 0;

int TEST_STRUM_DELAY = 500;

void strum(int strum1, int strum2, int strum3, int strum4, int strum5, int strum6){
  if (s1_pos == S1_START && strum1) 
  {
    s1.write(S1_STOP);
    s1_pos = S1_STOP;
  }
  else if (strum1)
  {
    s1.write(S1_START);
    s1_pos = S1_START;
  }

  if (s2_pos == S2_START && strum2) 
  {
    s2.write(S2_STOP);
    s2_pos = S2_STOP;
  }
  else if (strum2)
  {
    s2.write(S2_START);
    s2_pos = S2_START;
  }

  if (s3_pos == S3_START && strum3) 
  {
    s3.write(S3_STOP);
    s3_pos = S3_STOP;
  }
  else if (strum3)
  {
    s3.write(S3_START);
    s3_pos = S3_START;
  }

  if (s4_pos == S4_START && strum4) 
  {
    s4.write(S4_STOP);
    s4_pos = S4_STOP;
  }
  else if (strum4)
  {
    s4.write(S4_START);
    s4_pos = S4_START;
  }

  if (s5_pos == S5_START && strum5) 
  {
    s5.write(S5_STOP);
    s5_pos = S5_STOP;
  }
  else if (strum5)
  {
    s5.write(S5_START);
    s5_pos = S5_START;
  }
  
  if (s6_pos == S6_START && strum6) 
  {
    s6.write(S6_STOP);
    s6_pos = S6_STOP;
  }
  else if (strum6)
  {
    s6.write(S6_START);
    s6_pos = S6_START;
  }
}


void setup() {
  s1.attach(11);
  s2.attach(9);
  s3.attach(6);
  s4.attach(5);
  s5.attach(10);
  s6.attach(3);
  strum(0,0,0,0,0,0);
}

void pressFret(const char *cmd) {
  // S{string #}F{fret #}
  if (cmd == "S3F0") {

  }
  else if (cmd == "S3F2") {
    
  }
  else if (cmd == "S2F0") {
    
  }
  else if (cmd == "S2F1") {
    
  }
  else if (cmd == "S2F2") {
    
  }
  else if (cmd == "S2F3") {
    
  }
  else if (cmd == "S1F0") {
    
  }
  else if (cmd == "S1F2") {
    
  }
  else if (cmd == "S1F3") {
    
  }
  else if (cmd == "S6F0") {
    
  }
  else if (cmd == "S6F3") {
    
  }
  else if (cmd == "S5F0") {
    
  }
  else if (cmd == "S5F2") {
    
  }
  else if (cmd == "S4F0") {
    
  }
}

void releaseALlFrets() {
  // Add implementation
}

void receiveCommand() {
  if (Serial.available() >= CMD_SIZE) {
    int len = Serial.readBytes(received_command, 8);
    received_command[len] = '\0';

    releaseALlFrets();

    if (len == 4) {
      pressFret(received_command);
      int string_num = *(received_command + 1) - '0';
      strum(string_num == 1, string_num == 2, string_num == 3, string_num == 4,
            string_num == 5, string_num == 6);
    }
    // With bass notes
    else if (len == 8) {
      char cmd1[5];
      char cmd2[5];

      strncpy(cmd1, received_command, 4);
      strncpy(cmd2, received_command + 4, 4);

      cmd1[4] = '\0';
      cmd2[4] = '\0';

      pressFret(cmd1);
      pressFret(cmd2);

      int string_num1 = *(received_command + 1) - '0';
      int string_num2 = *(received_command + 5) - '0';

      strum(string_num1 == 1 || string_num2 == 1,
            string_num1 == 2 || string_num2 == 2,
            string_num1 == 3 || string_num2 == 3,
            string_num1 == 4 || string_num2 == 4,
            string_num1 == 5 || string_num2 == 5,
            string_num1 == 6 || string_num2 == 6);
    }
  }
}

void loop() {
  receiveCommand();
  if(CENTER_SERVO){
    s1.write(CENTER_ANGLE);
    s2.write(CENTER_ANGLE);
    s3.write(CENTER_ANGLE);
    s4.write(CENTER_ANGLE);
    s5.write(CENTER_ANGLE);
    s6.write(CENTER_ANGLE);
  }
  else{
  strum(0,0,0,0,0,1);
  delay(TEST_STRUM_DELAY);
  strum(0,0,0,0,0,1);
  delay(TEST_STRUM_DELAY);
  }
}
