#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;
Servo s4;
Servo s5;
Servo s6;

bool CENTER_SERVO = true;
int CENTER_ANGLE = 90;

int STARTING_ANGLE = 65; // 65
int STRUM_ANGLE = 180; // 100

int S1_START = 65;
int S1_STOP = 108;
int s1_pos = 0;

int S2_START = 75; // 78
int S2_STOP = 112; // 110
int s2_pos = 0;

int S3_START = 60;
int S3_STOP = 102;
int s3_pos = 0;

int S4_START = 57;
int S4_STOP = 102;
int s4_pos = 0;

int S5_START = 60;
int S5_STOP = 102;
int s5_pos = 0;

int S6_START = 78;
int S6_STOP = 119;
int s6_pos = 0;

int S3_OFFSET = 0;
int S4_OFFSET = 0;
int S5_OFFSET = 0;
int S6_OFFSET = 0;

int TEST_STRUM_DELAY = 1000;

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

void loop() {
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
