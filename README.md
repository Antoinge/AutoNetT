# AutoNetT
Final year OU Project.
This software can be used to discover logical topology of an IPv4 computer network. 
This software is meant to be a tool that can aid network engineers in mapping networks they have no 
previous knowledge of.
AutoNetT is split into several functions these are listed below:

1. an IPv4 validator function: this function takes a string as input and checks it is in the correct IPv4 format i.e. xxx.xxx.xxx.xxx.
the validator makes use of IPv4 format where there are four octets where each octet is >=0 and <=255. 
raw_input() was deprecated for Python 3 as a result the input must be converted from str to int prior to comparison. 
The code snippet below show the function.
 @staticmethod
    def validate_IPv4(ipv4addr):
        split_ipv4addr = ipv4addr.split(".")
        conv_ipaddr = []
        if len(split_ipv4addr) > 4:
            print("Invalid IPv4 address")
        else:
            for i in split_ipv4addr:
                i = int(i)
                if i < 0 or i > 255:
                    print("Invalid IPv4 address")
                else:
                    conv_ipaddr.append(i)
        return ipv4addr

2. A topology_map function: this function uses the third party Openpyxl module to create a spreadsheet where the topology
output will be stored. The purpose of this function is to create the spreadsheet and set the desired headings. The code for this
is below:
 @staticmethod
    def topology_Map(self):
        work_sheet = self.workbook.active
        work_sheet.title = "Test Output"
        work_sheet.cell(row=1, column=1, value="Device Type")
        work_sheet.cell(row=1, column=2, value="Device Name")
        work_sheet.cell(row=1, column=3, value="Interface")
        work_sheet.cell(row=1, column=4, value="IP Address")
        work_sheet.cell(row=1, column=5, value="Active Protocols")
        self.workbook.save("AutoNetT_Top_Map_Output.xlsx")
        return work_sheet

3. The is_Admin function is used to check users have administrator privileges before running the AutoNetT software. This is a 
security measure, as the potential for misuse with AutoNetT is high this will act as the first line of defence.
 def is_Admin(self, user):
        if Configuration.enable_session:
            conn_logs = sqlite3.connect(self.database_path)
            curs_logs = conn_logs.cursor()
            curs_logs.execute("SELECT USER_ID FROM ADMINS WHERE USER_ID=? AND USER_ID", (user, user))
            results = curs_logs.fetchone()
            if results is not None:
                return True
            return False
        return True

4. 