//EDC project of lsl 
//Modified by lsl & tzy
//last update: 2020/9/9

//-----------------------------------------

//引脚定义：
//温度：pin7
//湿度：pin2
//气压：SCL -> A5, SDA -> A4
//压力：analog 3
//命令：cmd[0] - pin8, cmd[1] - pin9
//继电器控制：12
//光敏输入 11
//光敏模拟输入 a0
//光敏PWM输出 13
//光敏输出 10



#include<OneWire.h>
#include<DallasTemperature.h>
#define BUS 7
#include <dht11.h>
dht11 DHT11;
#define DHT11PIN 2
#include <Wire.h>
#define BMP180ADD 0x77  // I2C address of BMP180  
                           //write is (0xEE)     read is (0xEF)       
unsigned char OSS;                            
/**********************MSB      LSB******/
int ac1;           // 0xAA     0xAB
int ac2;           // 0xAC     0xAD
int ac3;           // 0xAE     0xAE
unsigned int ac4;  // 0xB0     0xB1
unsigned int ac5;  // 0xB2     0xB3
unsigned int ac6;  // 0xB4     0xB5
int b1;            // 0xB6     0xB7
int b2;            // 0xB8     0xB9
int mb;            // 0xBA     0xBB
int mc;            // 0xBC     0xBD
int md;            // 0xBE     0xBF
float temperature;  
double pressure;   
double pressure2;
long b5;          
double altitude;  
int request[2];
int value = 0;
int weight_1024 = 0;
int weight_1024_average = 0;
int have_light = 0;
float weight = 0; // 
int light_value = 0;


OneWire onewire(BUS);
DallasTemperature sensors(&onewire);



void setup() {
  //6.8k (DS18b20数字输出引脚需要接4.7k-10k上拉电阻)
  //针脚定义 面朝印字面，左为GND,右为VCC,中间为数字输出引脚（接4.7-10k上拉电阻）
  pinMode(8,INPUT);
  pinMode(9,INPUT);
  pinMode(3,INPUT);
  pinMode(12,OUTPUT);
  pinMode(11,INPUT);
  pinMode(10,OUTPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  sensors.begin();
  Wire.begin();
  OSS = 2;  // Oversampling Setting           0: single    1: 2 times    2: 4 times   3: 8 times 
  BMP180start();

  Serial.begin(9600,SERIAL_8N2); //设置串口波特率9600，停止位2
}
 
void loop() { 
  
  // put your main code here, to run repeatedly:
  //pin8 pin9: 00/01/10/11
  request[0] = digitalRead(8);
  request[1] = digitalRead(9);

  have_light = digitalRead(11);
  sensors.requestTemperatures();
  float temp = sensors.getTempCByIndex(0);
  //Serial.print(temp);
  if(temp < 28.00){
    digitalWrite(12,1); //turn on
    }
  else{
    digitalWrite(12,0);
    }
 // request = {digitalRead(8),digitalRead(9)};
 /*
  if(have_light){
    digitalWrite(10,1); //off
  }else{
    digitalWrite(10,0); //on
  }
 */
  light_value = analogRead(0);
  //Serial.print(light_value/4);
  analogWrite(13,light_value/4);
  
  if(request[1] == 0 && request[0] == 0)
  {
              //----------temperature--------
      sensors.requestTemperatures();
      //Serial.println("温度传感器：-------");
      Serial.print(sensors.getTempCByIndex(0));
      Serial.print("0");
      delay(100);
  }
  if(request[1] == 0 && request[0] == 1)
  {
         //---------humidity---------
      int chk = DHT11.read(DHT11PIN);
     // Serial.println("湿度传感器: ----------");
     /*switch (chk)
     {
       case DHTLIB_OK: 
                 Serial.print(""); 
                 break;
       case DHTLIB_ERROR_CHECKSUM: 
                 Serial.println("Checksum error"); 
                 break;
       case DHTLIB_ERROR_TIMEOUT: 
                 Serial.println("Time out error"); 
                 break;
       default: 
                 Serial.println("Unknown error"); 
                 break;
      }
      */

      Serial.print(DHT11.humidity);
      Serial.print("0000");
      //Serial.println("%");
      //Serial.print(DHT11.temperature);
      //Serial.println("C"); 
      delay(100);     
 }
  if(request[1] == 1 && request[0] == 0)
  {
             //------------气压传感器------------
     calculate();
     //show();
     Serial.print(pressure,0);
     //---------
     delay(100);
  }
  if(request[1] == 1 && request[0] == 1)
  {
             //------------重量传感器------------
     
     //---------
    int sum = 0;
    for(int i = 0; i < 10; i++){
      value = analogRead(3);
      weight_1024 = 1024 - value;
      sum = sum + weight_1024;
      delay(100);
    }
    weight_1024_average = sum/10;
    weight = weight_1024_average * 0.00937;
    Serial.print(weight);
    Serial.print("00");
  }

   



}
/** calculate centure **/
void calculate()
{
  temperature = bmp180GetTemperature(bmp180ReadUT());
  temperature = temperature*0.1;
  pressure = bmp180GetPressure(bmp180ReadUP());
  pressure2 = pressure/101325;
  pressure2 = pow(pressure2,0.19029496);
  altitude = 44330*(1-pressure2);                            //altitude = 44330*(1-(pressure/101325)^0.19029496);
}
 
/** print reslut **/
void show()
{
  Serial.println("气压传感器：-----------");
  Serial.print(temperature, 1);                            //10 hexadecimal
  Serial.println("C");
  Serial.print(pressure, 0);                               //10 hexadecimal
  Serial.println(" Pa");
  Serial.print(altitude);
  Serial.println("m");
}
 
/**BMP180 satrt program**/
void BMP180start()
{                     /*MSB*/
  ac1 = bmp180ReadDate(0xAA);                      //get full data
  ac2 = bmp180ReadDate(0xAC);  
  ac3 = bmp180ReadDate(0xAE);  
  ac4 = bmp180ReadDate(0xB0);  
  ac5 = bmp180ReadDate(0xB2);  
  ac6 = bmp180ReadDate(0xB4);  
  b1  = bmp180ReadDate(0xB6);  
  b2  = bmp180ReadDate(0xB8);  
  mb  = bmp180ReadDate(0xBA);  
  mc  = bmp180ReadDate(0xBC);  
  md  = bmp180ReadDate(0xBE);
}
 
/***BMP180 temperature Calculate***/
short bmp180GetTemperature(unsigned int ut)
{
  long x1, x2;
  x1 = (((long)ut - (long)ac6)*(long)ac5) >> 15;  //x1=((ut-ac6)*ac5)/(2^15)
  x2 = ((long)mc << 11)/(x1 + md);                //x2=(mc*2^11)/(x1+md)
  b5 = x1 + x2;                                   //b5=x1+x2
  return ((b5 + 8)>>4);                           //t=(b5+8)/(2^4)
}
 
/***BMP180 pressure Calculate***/
 
long bmp180GetPressure(unsigned long up)
{
  long x1, x2, x3, b3, b6, p;
  unsigned long b4, b7;
  
  b6 = b5 - 4000;
 
  x1 = (b2 * (b6 * b6)>>12)>>11;
  x2 = (ac2 * b6)>>11;
  x3 = x1 + x2;
  b3 = (((((long)ac1)*4 + x3)<<OSS) + 2)>>2;
  
  x1 = (ac3 * b6)>>13;
  x2 = (b1 * ((b6 * b6)>>12))>>16;
  x3 = ((x1 + x2) + 2)>>2;
  b4 = (ac4 * (unsigned long)(x3 + 32768))>>15;
  
  b7 = ((unsigned long)(up - b3) * (50000>>OSS));
  if (b7 < 0x80000000)
    p = (b7<<1)/b4;
  else
    p = (b7/b4)<<1;
    
  x1 = (p>>8) * (p>>8);
  x1 = (x1 * 3038)>>16;
  x2 = (-7357 * p)>>16;
  p += (x1 + x2 + 3791)>>4;
  
  return p;
}
 
 
/*** Read 1 bytes from the BMP180  ***/
 
int bmp180Read(unsigned char address)
{
  unsigned char data;
  
  Wire.beginTransmission(BMP180ADD);
  Wire.write(address);
  Wire.endTransmission();
  
  Wire.requestFrom(BMP180ADD, 1);
  while(!Wire.available());
    
  return Wire.read();
}
 
/*** Read 2 bytes from the BMP180 ***/
int bmp180ReadDate(unsigned char address)
{
  unsigned char msb, lsb;
  Wire.beginTransmission(BMP180ADD);
  Wire.write(address);
  Wire.endTransmission();
  Wire.requestFrom(BMP180ADD, 2);
  while(Wire.available()<2);
  msb = Wire.read();
  lsb = Wire.read();
  return (int) msb<<8 | lsb;
}
 
/*** read uncompensated temperature value ***/
unsigned int bmp180ReadUT()
{
  unsigned int ut;
  Wire.beginTransmission(BMP180ADD);
  Wire.write(0xF4);                       // Write 0x2E into Register 0xF4
  Wire.write(0x2E);                       // This requests a temperature reading
  Wire.endTransmission();  
  delay(5);                               // Wait at least 4.5ms
  ut = bmp180ReadDate(0xF6);               // read MSB from 0xF6 read LSB from (16 bit)
  return ut;
}
 
/*** Read uncompensated pressure value from BMP180 ***/
unsigned long bmp180ReadUP()
{
  unsigned char msb, lsb, xlsb;
  unsigned long up = 0;
  
  Wire.beginTransmission(BMP180ADD);
  Wire.write(0xF4);                        // Write 0x34+(OSS<<6) into register 0xF4
  Wire.write(0x34 + (OSS<<6));             // 0x34+oss*64
  Wire.endTransmission(); 
  delay(2 + (3<<OSS));                     // Wait for conversion, delay time dependent on OSS
  
  Wire.beginTransmission(BMP180ADD);
  Wire.write(0xF6);                        // Read register 0xF6 (MSB), 0xF7 (LSB), and 0xF8 (XLSB)
  Wire.endTransmission();
  
  Wire.requestFrom(BMP180ADD, 3); 
  while(Wire.available() < 3);             // Wait for data to become available
  msb = Wire.read();
  lsb = Wire.read();
  xlsb = Wire.read();
  up = (((unsigned long) msb << 16) | ((unsigned long) lsb << 8) | (unsigned long) xlsb) >> (8-OSS);//16 to 19 bit
  return up;
}
