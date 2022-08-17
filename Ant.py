import ctypes
import os
from telnetlib import Telnet
from openpyxl import Workbook
from netmiko import ConnectHandler


class AutoNetT:
    def __init__(self, Workbook, is_Admin, user):
        self.Telnet = None
        self.host = input()
        self.user = user
        self.is_Admin = is_Admin
        self.workbook = Workbook()
        self.path = os.mkdir("AutoNetT")

    def is_admin(self):
        # Returns whether or not we're admin
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin     

    def coordinator(self, host):
        if self.is_admin() == True:
            self.validate_IPv4(host())
            self.work_sheet = self.topology_Map(self)
            Telnet.open(host, port=23)
        else:
            return f"Admin rights rquired to run this programme"

    @staticmethod
    def validate_IPv4(ipv4addr):
        split_ipv4addr = ipv4addr.split(".")
        conv_ipaddr = []
        if len(split_ipv4addr) > 4:
            return f'Invalid IPv4 address'
        else:
            for i in split_ipv4addr:
                i = int(i)
                if i < 0 or i > 255:
                    print("Invalid IPv4 address")
                else:
                    conv_ipaddr.append(i)
        return ipv4addr

    def topology_Map(self):
        work_sheet = Workbook()
        work_sheet.title = "Test Output"
        work_sheet.cell(row=1, column=1, value="Device Type")
        work_sheet.cell(row=1, column=2, value="Device Name")
        work_sheet.cell(row=1, column=3, value="Interface")
        work_sheet.cell(row=1, column=4, value="IP Address")
        work_sheet.cell(row=1, column=5, value="Active Protocols")
        self.workbook.save("AutoNetT_Top_Map_Output.xlsx")
        return Workbook

    def network_Search(self, file, workbook):
        file.load("AutoNetT_Top_Map_Output.xlsx", "w")
        sheet = workbook.active
        sheet['D1'] = self.host
        if self.is_admin():
            try:
                router = ConnectHandler(router_type='cisco_ios', ip=self.host, username=input(), password=input())
                output = router.send_command("enable", "configure terminal", "cdp enable", "show run")
                print(output)
            except Exception as err:
                print("Connection to router failed: " + str(err))
            pass
