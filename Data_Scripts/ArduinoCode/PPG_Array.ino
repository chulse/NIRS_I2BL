/* Author Hannaneh Hojaiji
 *  NIRS I2BL CORELAB
 *  This is the V1 of Multimode code to controle PPG measurement
 */

int red4 = 7;//red 4
int red3 = 4;//red 3
int red2 = 3;//red 2
int red1 = 9;//red 1

int ir4 = 6;//IR 4
int ir3 = 5;//IR 3
int ir2 = 2;//IR 2
int ir1 = 8;//IR 1

int pd1 = A0;//Reads A0 un-inverted PD 1 (mid), inv 1, 2 filt
int pd1filt = A2;//Reads A0 un-inverted PD 1 (mid), inv 1, 2 filt
int pd2 = A5;//Reads A5 un-inverted PD 2 (left), inv 3
int pd3 = A6;//Reads A6 un-inverted PD 3 (right), inv 4
int photodiode =0;
int photodiode_filt =0;
int photodiode2 =0;
int photodiode3 =0;
int i = 0;
int reds[5];
int irs[5];

void setup() {
  Serial.begin(9600);
  //analogReference(INTERNAL);

  pinMode(red1, OUTPUT);
  pinMode(red2, OUTPUT);
  pinMode(red3, OUTPUT); 
  pinMode(red4, OUTPUT);

  pinMode(ir1, OUTPUT);
  pinMode(ir2, OUTPUT);
  pinMode(ir3, OUTPUT); 
  pinMode(ir4, OUTPUT);

}

void loop() {

  // Test1: Ensure photodiode is detecting
  // Result: WORKS

  // Test2: Ensure timing is non-overlapping
  // Result: Maximum delay(20) aka 50Hz for non-overlapping --> any faster results in overlapping
  // Possible "solution": Just graph based on samples, and then set sampling frequency to whatever

  // Test3: Compare device placed on table vs. device placed on hand
  // Result: IR shows significant variations compared to on table, but still very noisy
  // Result: 

  //Red 1  
  digitalWrite(red1, HIGH);
  digitalWrite(red2, HIGH);
  digitalWrite(red3, HIGH);
  delay(1);
  Serial.print(',');
  Serial.print(analogRead(pd1));
  Serial.print(',');
  Serial.print(analogRead(pd2));
  digitalWrite(red1, LOW);
  digitalWrite(red2, LOW);
  digitalWrite(red3, LOW);
  delay(1); 
  digitalWrite(ir1, HIGH);
  digitalWrite(ir2, HIGH);
  digitalWrite(ir3, HIGH); 
  delay(1);
  Serial.print(',');
  Serial.print(analogRead(pd1));
  Serial.print(',');
  Serial.print(analogRead(pd2));
  digitalWrite(ir1, LOW);
  digitalWrite(ir2, LOW);
  digitalWrite(ir3, LOW); 
  delay(1);      
  Serial.println();
 
}
