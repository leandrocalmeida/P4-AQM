#!/usr/bin/env python3
import argparse
import sys
import socket
import random
import struct
import time

from time import sleep
from scapy.all import Packet, bind_layers, XByteField, FieldLenField, BitField, ShortField, IntField, PacketListField, Ether, IP, UDP, sendp, get_if_hwaddr, sniff


class InBandNetworkTelemetry(Packet):
    fields_desc = [ BitField("switchID_t", 0, 31),
                    BitField("ingress_port",0, 9),
                    BitField("egress_port",0, 9),
                    BitField("egress_spec", 0, 9),
                    BitField("ingress_global_timestamp", 0, 48),
                    BitField("egress_global_timestamp", 0, 48),
                    BitField("enq_timestamp",0, 32),
                    BitField("enq_qdepth",0, 19),
                    BitField("deq_timedelta", 0, 32),
                    BitField("deq_qdepth", 0, 19)
                  ]
    """any thing after this packet is extracted is padding"""
    def extract_padding(self, p):
                return "", p

class nodeCount(Packet):
  name = "nodeCount"
  fields_desc = [ ShortField("count", 0),
                  PacketListField("INT", [], InBandNetworkTelemetry, count_from=lambda pkt:(pkt.count*1))]

def getFields(pkt):
  field_names = []
  fields = {}

  for lengthInt in range(len(pkt[nodeCount].INT)):
    field_names = [field.name for field in pkt[nodeCount].INT[lengthInt].fields_desc]
    fields[lengthInt] = {field_name: getattr(pkt[nodeCount].INT[lengthInt], field_name) for field_name in field_names}
  
  return fields

def logInt(fields_value):
  line_values_temp = []
  for lenFieldsValue in range(len(fields_value)):
    sep = ','
    temp1 = sep.join(map(str,list(fields_value[lenFieldsValue].values())))
    line_values_temp.append(temp1)
  
  sep = ','
  line_values = sep.join(map(str,list(line_values_temp)))
  
  timestamp = int(time.time())
  log_str = str(timestamp) + ',' + line_values
  with open('logs/log_INT.txt','a+') as file:
    file.write(log_str + '\n')

def handle_pkt(pkt):
  
  fields_value = getFields(pkt)
  logInt(fields_value)
  

def main():
  ts = ['timestamp']
  header_fileLog = ['switchID_t', 'ingress_port', 'egress_port', 'egress_spec', 'ingress_global_timestamp', 'egress_global_timestamp', 'enq_timestamp', 'enq_qdepth', 'deq_timedelta', 'deq_qdepth' ]
  header_fileLog3 =  [f'{item}3' for item in header_fileLog]
  header_fileLog2 =  [f'{item}2' for item in header_fileLog]
  header_fileLog1 =  [f'{item}1' for item in header_fileLog]
  header = ", ".join(ts) + "," + ", ".join(header_fileLog3) + "," + ", ".join(header_fileLog2) + "," + ", ".join(header_fileLog1)  
  
  with open('logs/log_INT.txt','w+') as file:
      file.write( str(header) + '\n')

  iface = 'enp0s8'
  bind_layers(IP, nodeCount, proto = 253)
  sniff(filter = "ip proto 253", iface = iface, prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()