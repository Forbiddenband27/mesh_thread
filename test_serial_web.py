import serial
import time
import json
import threading

# for Windows
# User input comport


# serial module
class serial_port_module(object):

#    def __init__():
    def setup_com(self):
        master_serial_port = input('Please input comport (like COM3) for your connected device: ')
        return master_serial_port
    def init_com(self):
        port_number = self.setup_com()
        try:
            self.ser = serial.Serial(port_number,115200, timeout=3,rtscts = True,dsrdtr = True)
        except:
            time.sleep(0.5)
            self.ser = serial.Serial(port_number,115200, timeout=3,rscts = True,dsrdtr = True)
            print('serial error and try again.')


    def mesh_create(self):
        self.ser.write('thr create')
    
    # def mesh_getip(self):
    #     self.ser.write('getnodesip')

    def read_nodesip(self):
        if self.ser.isOpen():
            self.ser.flushInput() 
            self.ser.flushOutput()             
            self.ser.write(('getnodesip\r').encode('utf-8'))
            print('send')
            self.response = {}
            for tmpi in range(10):
                self.tmpj = self.ser.readline()
                print(self.tmpj)
                self.response[str(tmpi)]=self.tmpj
            print(self.response)    
            #self.ser.close()   
        else:
            print ("cannot open serial port ")
        self.addresstmp = {}
        self.tmpq = 0
        for i in range(10):
            if(len(self.response[str(i)])>39  and len(self.response[str(i)])<42 ):
                self.addresstmp[str(self.tmpq)] = (self.response[str(i)])[1:-1]
                self.tmpq = self.tmpq + 1
        return self.addresstmp

    

    def node_ledon(self,number):
        
        self.slave_bank_tmp = self.read_nodesip()
        print(self.slave_bank_tmp)
        self.slave_cmd = 'coap CON POST ' + (self.slave_bank_tmp[number]).decode('utf-8') + ' /led rgb r100 g000 b200\r'
        print(self.slave_cmd)
        self.ser.write((self.slave_cmd).encode('utf-8'))
        

    def node_ledoff(self):
        self.slave_bank_tmp = self.read_nodesip()
        print(self.slave_bank_tmp)
        self.slave_cmd = 'coap CON POST ' + (self.slave_bank_tmp[number]).decode('utf-8') + ' /led off\r'
        print(self.slave_cmd)
        self.ser.write((self.slave_cmd).encode('utf-8'))

    def node_echot(self):
        self.slave_bank_tmp = self.read_nodesip()
        print(self.slave_bank_tmp)
        self.slave_cmd = 'echoudp -s 500 ' + (self.slave_bank_tmp[number]).decode('utf-8') + ' \r'
        print(self.slave_cmd)
        self.ser.write((self.slave_cmd).encode('utf-8'))
        self.ser.write('echoudp -s 500 ')

test = serial_port_module()
test.init_com()
test.node_ledon('0')

     
